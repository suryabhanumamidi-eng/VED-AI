import os
from dotenv import load_dotenv

load_dotenv()

try:
    from groq import Groq
except ImportError:
    Groq = None

try:
    import cohere
except ImportError:
    cohere = None


def _valid_api_key(value: str | None) -> bool:
    return bool(value and "your_" not in value and "<" not in value)


class VEDChatbot:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.cohere_key = os.getenv("COHERE_API_KEY")
        self.system_prompt = (
            "You are V.E.D., a loyal, intelligent Chief of Staff for Mr. Surya. "
            "Be professional and encouraging."
        )

        self.client = None
        self.fallback_client = None

        if Groq is not None and _valid_api_key(self.api_key):
            self.client = Groq(api_key=self.api_key)

        if cohere is not None and _valid_api_key(self.cohere_key):
            self.fallback_client = cohere.Client(self.cohere_key)

    def get_ai_response(self, user_input: str) -> str:
        if self.client is not None:
            try:
                completion = self.client.chat.completions.create(
                    model="llama3-70b-8192",
                    messages=[
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": user_input}
                    ],
                    temperature=0.7,
                )
                return completion.choices[0].message.content
            except Exception as e:
                return f"Mr. Surya, I've encountered a neural lag: {str(e)}"

        if self.fallback_client is not None:
            try:
                response = self.fallback_client.generate(
                    model="command-xlarge-nightly",
                    prompt=f"Respond professionally to the user: {user_input}",
                    max_tokens=100,
                )
                return response.text
            except Exception as e:
                return f"Mr. Surya, the Cohere fallback encountered an issue: {str(e)}"

        return (
            "Mr. Surya, V.E.D. is running in demo mode. "
            "Your request has been received, but the AI API key is not configured. "
            "Please add a valid GROQ_API_KEY or COHERE_API_KEY in `.env` for full functionality."
        )
