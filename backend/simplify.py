from transformers import T5ForConditionalGeneration, T5Tokenizer

model_name = "google/flan-t5-base"

print("Loading model... this may take a minute the first time.")
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def run_instruction(text, mode, level="6th grade"):
    """
    text: input string
    mode: one of ["simplify", "summarize", "explain10", "example", "steps"]
    level: reading-level string for simplify mode
    """


    if mode == "simplify":

        grade_rules = {
            "3rd grade": (
                "Use ONLY simple everyday words. "
                "No sentence may be longer than 8–10 words. "
                "Explain ideas slowly and clearly. "
                "Remove advanced vocabulary. "
                "If a word is hard, replace it with an easy word a child would know. "
                'Pretend you are teaching a 9-year-old who is still learning English.'
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

    # Generate output
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(
        **inputs,
        max_length=250,
        temperature=0.6,
        num_beams=4,
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
