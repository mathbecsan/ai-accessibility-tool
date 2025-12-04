# API Documentation

## Overview

LearnEasy provides a REST API built with FastAPI that exposes all core functionality. This document provides detailed information about all available endpoints.

## Base URL

```
http://localhost:8000
```

## Interactive API Documentation

Once the backend is running, visit:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

## Authentication

Currently, no authentication is required. For production deployments, consider implementing API key authentication or JWT tokens.

---

## Endpoints

### 1. Health Check

**GET** `/`

Returns basic server status.

**Response:**

```json
{
  "message": "LearnEasy backend is running"
}
```

---

### 2. Text Transformation

**POST** `/transform`

Transform text using various modes (simplify, summarize, explain, etc.).

#### Request Body

```json
{
  "text": "Your complex text here",
  "mode": "simplify",
  "level": "6th grade"
}
```

#### Parameters

| Parameter | Type   | Required | Default     | Description                       |
| --------- | ------ | -------- | ----------- | --------------------------------- |
| `text`    | string | Yes      | -           | Input text to transform           |
| `mode`    | string | No       | "simplify"  | Transformation mode               |
| `level`   | string | No       | "6th grade" | Reading level (for simplify mode) |

#### Mode Options

| Mode        | Description                                          | Use Case                                                      |
| ----------- | ---------------------------------------------------- | ------------------------------------------------------------- |
| `simplify`  | Reduce text complexity to specified reading level    | Adapting content for younger readers or lower literacy levels |
| `summarize` | Create a concise summary of the text                 | Getting quick overview of long documents                      |
| `explain10` | Generate detailed explanation (approx. 10 sentences) | Deep understanding of complex concepts                        |
| `example`   | Generate relevant real-world examples                | Understanding through concrete examples                       |
| `steps`     | Break down process into step-by-step instructions    | Learning procedural content                                   |

#### Reading Levels (for simplify mode)

- `3rd grade` – Very simple language, short sentences
- `5th grade` – Simple language, moderate sentence length
- `6th grade` – Standard school reading level
- `8th grade` – More complex vocabulary and sentence structure
- `High school` – Advanced reading level

#### Response

```json
{
  "original": "Your complex text here",
  "transformed": "Simplified version of text",
  "mode": "simplify"
}
```

#### Example Request

```bash
curl -X POST "http://localhost:8000/transform" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Photosynthesis is the process by which plants convert light energy into chemical energy through the synthesis of glucose from carbon dioxide and water.",
    "mode": "simplify",
    "level": "3rd grade"
  }'
```

#### Example Response

```json
{
  "original": "Photosynthesis is the process by which plants convert light energy into chemical energy through the synthesis of glucose from carbon dioxide and water.",
  "transformed": "Plants use sunlight to make food. They take in air and water. The sun's energy helps them change these into food energy.",
  "mode": "simplify"
}
```

---

### 3. Text-to-Speech Conversion

**POST** `/tts`

Convert text to audio in MP3 format.

#### Request Body

```json
{
  "text": "Text to convert to audio",
  "lang": "en"
}
```

#### Parameters

| Parameter | Type   | Required | Default | Description               |
| --------- | ------ | -------- | ------- | ------------------------- |
| `text`    | string | Yes      | -       | Text to convert to speech |
| `lang`    | string | No       | "en"    | Language code (ISO 639-1) |

#### Supported Languages

- `en` – English
- `es` – Spanish
- `fr` – French
- `de` – German
- `it` – Italian
- `ja` – Japanese
- `ko` – Korean
- `zh` – Chinese (Mandarin)

#### Response

```json
{
  "audio_base64": "SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU5LjI3LjEwMAAAAAAAAAAAAGQ=",
  "format": "mp3"
}
```

#### Example Request

```bash
curl -X POST "http://localhost:8000/tts" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello, this is LearnEasy",
    "lang": "en"
  }'
```

#### Playing Audio

To play the returned audio:

```python
import requests
import base64
from pydub import AudioSegment
from io import BytesIO

response = requests.post("http://localhost:8000/tts",
                        json={"text": "Hello, this is LearnEasy"})
data = response.json()

audio_bytes = base64.b64decode(data["audio_base64"])
audio = AudioSegment.from_mp3(BytesIO(audio_bytes))
audio.export("output.mp3", format="mp3")
```

---

### 4. Diagram Generation

**POST** `/diagram`

Generate visual diagrams for step-by-step processes.

#### Request Body

```json
{
  "text": "Step-by-step process description"
}
```

#### Parameters

| Parameter | Type   | Required | Description                      |
| --------- | ------ | -------- | -------------------------------- |
| `text`    | string | Yes      | Process description to visualize |

#### Response

```json
{
  "diagram_svg": "<svg>...</svg>",
  "steps": ["step1", "step2", "step3"]
}
```

#### Example Request

```bash
curl -X POST "http://localhost:8000/diagram" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "First prepare ingredients. Then mix in a bowl. Finally bake at 350 degrees for 30 minutes."
  }'
```

#### Example Response

```json
{
  "diagram_svg": "<svg width=\"400\" height=\"300\">...</svg>",
  "steps": [
    "Prepare ingredients",
    "Mix in bowl",
    "Bake at 350°F for 30 minutes"
  ]
}
```

#### Using the Diagram

To display the SVG diagram:

```python
import requests

response = requests.post("http://localhost:8000/diagram",
                        json={"text": "Your process here"})
data = response.json()

# Save SVG to file
with open("diagram.svg", "w") as f:
    f.write(data["diagram_svg"])
```

---

## Error Handling

The API returns standard HTTP status codes:

| Status Code | Meaning          | Example                                |
| ----------- | ---------------- | -------------------------------------- |
| 200         | Success          | Text successfully transformed          |
| 400         | Bad Request      | Invalid mode or missing required field |
| 422         | Validation Error | Invalid data type or format            |
| 500         | Server Error     | Internal server error                  |

### Error Response Format

```json
{
  "detail": "String describing the error"
}
```

### Example Error

```json
{
  "detail": [
    {
      "loc": ["body", "text"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

---

## Rate Limiting

Currently, no rate limiting is implemented. For production, implement:

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.post("/transform")
@limiter.limit("100/minute")
async def transform(request: Request, req: TransformRequest):
    # endpoint logic
```

---

## Code Examples

### Python Client

```python
import requests

BASE_URL = "http://localhost:8000"

class LearnEasyClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def simplify(self, text, level="6th grade"):
        """Simplify text to specified reading level"""
        response = requests.post(
            f"{self.base_url}/transform",
            json={"text": text, "mode": "simplify", "level": level}
        )
        return response.json()["transformed"]

    def summarize(self, text):
        """Summarize text"""
        response = requests.post(
            f"{self.base_url}/transform",
            json={"text": text, "mode": "summarize"}
        )
        return response.json()["transformed"]

    def explain(self, text):
        """Generate detailed explanation"""
        response = requests.post(
            f"{self.base_url}/transform",
            json={"text": text, "mode": "explain10"}
        )
        return response.json()["transformed"]

    def text_to_speech(self, text, lang="en"):
        """Convert text to speech"""
        response = requests.post(
            f"{self.base_url}/tts",
            json={"text": text, "lang": lang}
        )
        return response.json()["audio_base64"]

# Usage
client = LearnEasyClient()
simplified = client.simplify("Complex text here")
print(simplified)
```

### JavaScript/Node.js Client

```javascript
const LEARN_EASY_URL = "http://localhost:8000";

async function simplifyText(text, level = "6th grade") {
  const response = await fetch(`${LEARN_EASY_URL}/transform`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text: text,
      mode: "simplify",
      level: level,
    }),
  });

  const data = await response.json();
  return data.transformed;
}

async function convertToSpeech(text, lang = "en") {
  const response = await fetch(`${LEARN_EASY_URL}/tts`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text: text,
      lang: lang,
    }),
  });

  const data = await response.json();
  return data.audio_base64;
}

// Usage
const simplified = await simplifyText("Your complex text here");
console.log(simplified);
```

---

## Pagination

Not applicable for current endpoints. Consider implementing for future bulk operations.

---

## Versioning

Currently using v1 (implicit). For future versioning:

```
GET /api/v1/transform
GET /api/v2/transform
```

---

## CORS Configuration

For frontend integration, CORS is configured in `backend/main.py`:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Performance Notes

- Model loading: ~2-3 seconds on first request
- Text transformation: 0.5-2 seconds depending on text length
- Consider caching results for identical inputs
- Use async endpoints for high-concurrency scenarios

---

## Troubleshooting

### Model Download Issues

If the FLAN-T5 model fails to download:

```bash
python -c "from transformers import T5Tokenizer, T5ForConditionalGeneration; T5Tokenizer.from_pretrained('google/flan-t5-small')"
```

### CUDA/GPU Issues

For CPU-only execution:

```bash
export CUDA_VISIBLE_DEVICES=""
```

### Port Already in Use

```bash
lsof -i :8000  # Find process using port 8000
kill -9 <PID>   # Kill the process
```

---

## Support

For API-related questions:

- Check this documentation
- Review GitHub Issues
- Ask in GitHub Discussions

---

**Last Updated:** December 2024
