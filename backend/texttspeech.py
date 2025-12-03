# backend/tts.py

from gtts import gTTS
import base64
import tempfile
from typing import Optional

def text_to_audio_base64(text: str, lang: str = "en") -> str:
    """
    Convert text to speech using gTTS and return base64 encoded MP3.
    """
   
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        filename = fp.name

    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

    with open(filename, "rb") as f:
        audio_bytes = f.read()
    return base64.b64encode(audio_bytes).decode("utf-8")
