import pywhatkit


class WhatsApp:
    def send_message(self, phone_number: str, message: str, hour: int, minute: int) -> str:
        try:
            pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
            return "WhatsApp message scheduled, Mr. Surya."
        except Exception as e:
            return f"WhatsApp scheduling failed: {str(e)}"
