from Backend.Chatbot import VEDChatbot
from Backend.Automation import SystemControl
from Backend.ImageGeneration import ImageGeneration
from Backend.JobApply import JobAgent


class DecisionLayer:
    def __init__(self):
        self.chat = VEDChatbot()
        self.control = SystemControl()
        self.jobs = JobAgent()
        self.image = ImageGeneration()

    def route_query(self, query: str) -> str:
        q = query.lower()

        if "open" in q or "launch" in q:
            return self.control.open_app(q)
        elif "apply for jobs" in q or "job search" in q:
            return self.jobs.auto_apply()
        elif "generate image" in q or "image generation" in q:
            prompt = q.replace("generate image", "").replace("image generation", "").strip()
            prompt = prompt or "a futuristic AI dashboard with glowing holograms"
            return self.image.create_image(prompt)
        elif "demo" in q:
            return self.demo_sequence()
        else:
            return self.chat.get_ai_response(query)

    def demo_sequence(self) -> str:
        chat_demo = self.chat.get_ai_response("Hello V.E.D., provide a brief demo response.")
        image_demo = self.image.create_image("A high-tech AI control room with neon accents")
        return (
            "Demo Mode Initiated.\n"
            f"AI Response: {chat_demo}\n"
            f"Image Response: {image_demo}"
        )
