import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer
from gtts import gTTS
from io import BytesIO
import base64
import graphviz

@st.cache_resource
def load_model():
    model_name = "google/flan-t5-small"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()


# CORE INSTRUCTION ENGINE
def run_instruction(text: str, mode: str, level: str = "6th grade") -> str:
    """
    Unified function: simplify / summarize / explain / examples / steps.
    """

    if mode == "simplify":

        grade_rules = {
            "3rd grade": (
                "Use ONLY simple everyday words. "
                "No sentence may be longer than 8–10 words. "
                "Explain ideas slowly and clearly. "
                "Remove advanced vocabulary. "
                "If a word is hard, replace it with an easy word a child would know. "
                "Pretend you are teaching a 9-year-old who is still learning English."
            ),
            "5th grade": (
                "Use simple language. "
                "Sentences must be 10–12 words. "
                "Use examples to explain ideas. "
                "Avoid complex or academic vocabulary."
            ),
            "8th grade": (
                "Use clear middle-school language. "
                "Keep sentences under 14 words. "
                "Explain concepts with simple logic but include some detail."
            ),
            "high school": (
                "Use clear, academic English appropriate for high school. "
                "You may use mild technical terms but explain them. "
                "Sentences should be 14–18 words."
            ),
            "college": (
                "Use formal, academic English. "
                "You may use technical terms but define them clearly. "
                "Focus on accuracy and clarity."
            ),
            "Explain like I'm 5": (
                "Explain this idea to a 5-year-old child. "
                "Use extremely simple words. "
                "Use short sentences (6–8 words). "
                "Use friendly, gentle examples."
            )
        }

        constraints = grade_rules.get(level, "")

        prompt = (
            f"Simplify the text using these rules:\n"
            f"{constraints}\n\n"
            f"Text:\n{text}\n\n"
            f"Simplified ({level} version):"
        )

    elif mode == "summarize":
        prompt = f"Write a short, clear summary for a beginner:\n\n{text}"

    elif mode == "explain10":
        prompt = f"Explain the following in simple terms as if teaching a 10-year-old:\n\n{text}"

  
    elif mode == "example":
        prompt = f"Give a simple real-life example that helps explain this topic:\n\n{text}"


    elif mode == "steps":
        prompt = (
            "Break the following idea into 5–7 simple steps that a middle school student can follow:\n\n"
            f"{text}"
        )

    else:
        prompt = text

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(
        **inputs,
        max_length=250,
        temperature=0.6,
        num_beams=4,
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# DIAGRAM (FLOWCHART)
def extract_steps(text: str) -> list[str]:
    """
    Use 'steps' mode to turn text into 4–7 simple steps.
    """
    steps_text = run_instruction(text, mode="steps", level="8th grade")
    raw_lines = steps_text.splitlines()

    steps = []
    for line in raw_lines:
        line = line.strip()
        if not line:
            continue
        # remove numbering like "1. something"
        if line[0].isdigit() and "." in line:
            line = line.split(".", 1)[1].strip()
        if line.startswith("- "):
            line = line[2:].strip()
        steps.append(line)

    return steps[:7]


def build_flowchart(steps: list[str]) -> graphviz.Digraph:
    dot = graphviz.Digraph()
    dot.attr(rankdir="TB", fontsize="12", nodesep="0.5", ranksep="0.6")
    dot.attr("node", shape="box", style="rounded,filled", fillcolor="#111827",
             fontcolor="white", color="#00e6c3", penwidth="1.5")

    for i, step in enumerate(steps):
        dot.node(str(i), step)

    for i in range(len(steps) - 1):
        dot.edge(str(i), str(i + 1), color="#00e6c3")

    return dot

# TEXT-TO-SPEECH VIA gTTS
def text_to_audio_bytes(text: str) -> BytesIO:
    """
    Convert text to speech and return a BytesIO MP3 stream.
    """
    tts = gTTS(text=text, lang="en")
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp



# STREAMLIT UI
st.set_page_config(page_title="LearnEasy – Cloud", layout="wide")

st.markdown(
    "<h1 style='text-align:center;'>LearnEasy <span style='color:#00e6c3;'>Cloud</span></h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align:center;color:#9ca3af;'>Make school text more accessible with simplified explanations, diagrams, and read-aloud.</p>",
    unsafe_allow_html=True,
)

text = st.text_area("Paste your text here:", height=200)

col1, col2 = st.columns(2)

with col1:
    mode = st.selectbox(
        "Choose transformation:",
        ["simplify", "summarize", "explain10", "example", "steps"],
        index=0,
    )

with col2:
    level = st.selectbox(
        "Reading level (for simplify):",
        ["3rd grade", "5th grade", "8th grade", "high school", "college", "Explain like I'm 5"],
        index=2,
    )

if "last_output" not in st.session_state:
    st.session_state["last_output"] = ""

if st.button("⚡ Transform Text"):
    if not text.strip():
        st.warning("Please paste some text first.")
    else:
        with st.spinner("Thinking..."):
            out = run_instruction(text, mode=mode, level=level)
        st.session_state["last_output"] = out

if st.session_state["last_output"]:
    st.markdown("---")
    st.subheader("Output:")
    st.write(st.session_state["last_output"])

    st.markdown("---")
    st.subheader("Accessibility Tools")

    tcol1, tcol2 = st.columns(2)

    # Text-to-Speech
    with tcol1:
        if st.button("🔊 Read Aloud"):
            with st.spinner("Generating audio..."):
                audio_fp = text_to_audio_bytes(st.session_state["last_output"])
            st.audio(audio_fp, format="audio/mp3")

    # Diagram
    with tcol2:
        if st.button("📊 Generate Diagram"):
            with st.spinner("Building diagram..."):
                steps = extract_steps(st.session_state["last_output"])
                if not steps:
                    st.warning("Could not extract steps for a diagram.")
                else:
                    dot = build_flowchart(steps)
                    st.graphviz_chart(dot)
                    st.markdown("**Steps extracted:**")
                    for i, step in enumerate(steps, start=1):
                        st.write(f"{i}. {step}")
