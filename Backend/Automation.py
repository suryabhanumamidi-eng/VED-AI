import subprocess
import platform


class SystemControl:
    def __init__(self):
        self.os_name = platform.system().lower()

    def open_app(self, query: str):
        # Simple desktop application launcher stub
        if "chrome" in query or "browser" in query:
            return self._launch_browser()
        elif "notepad" in query or "text editor" in query:
            return self._launch_text_editor()
        else:
            return "Mr. Surya, I can open your browser or text editor for now."

    def _launch_browser(self):
        try:
            if "windows" in self.os_name:
                subprocess.Popen(["start", "chrome"], shell=True)
            elif "darwin" in self.os_name:
                subprocess.Popen(["open", "-a", "Google Chrome"])
            else:
                subprocess.Popen(["xdg-open", "https://www.google.com"])
            return "Launching browser for you, Mr. Surya."
        except Exception as e:
            return f"Unable to launch browser: {str(e)}"

    def _launch_text_editor(self):
        try:
            if "windows" in self.os_name:
                subprocess.Popen(["notepad"])
            elif "darwin" in self.os_name:
                subprocess.Popen(["open", "-a", "TextEdit"])
            else:
                subprocess.Popen(["xdg-open", "/tmp"])
            return "Opening your editor, Mr. Surya."
        except Exception as e:
            return f"Unable to open editor: {str(e)}"
