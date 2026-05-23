import os
from dotenv import load_dotenv

load_dotenv()

try:
    import cohere
except ImportError:
    cohere = None


def _valid_api_key(value: str | None) -> bool:
    return bool(value and "your_" not in value and "<" not in value)


class ImageGeneration:
    def __init__(self):
        self.api_key = os.getenv("COHERE_API_KEY")
        self.client = None

        if cohere is not None and _valid_api_key(self.api_key):
            self.client = cohere.Client(self.api_key)

    def create_image(self, prompt: str) -> str:
        if self.client is not None:
            return f"Image generation request queued for prompt: '{prompt}'. (Cohere integration enabled.)"

        return (
            f"Generating an image for: {prompt}. "
            "Image API integration is currently in placeholder mode. "
            "Add a valid COHERE_API_KEY in `.env` to enable real image generation."
        )
