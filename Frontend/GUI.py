import customtkinter as ctk


class VED_GUI(ctk.CTk):
    def __init__(self, process_command):
        super().__init__()
        self.process_command = process_command
        
        self.title("V.E.D. // VASTLY EVOLVED DIGITAL INTELLIGENCE")
        self.geometry("1000x700")
        ctk.set_appearance_mode("dark")
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text="V.E.D. SYSTEM ACTIVE",
            font=("Orbitron", 28),
            text_color="#00d4ff"
        )
        self.title_label.pack(pady=20)

        self.console = ctk.CTkTextbox(
            self,
            width=900,
            height=450,
            border_color="#00d4ff",
            border_width=1,
            font=("Share Tech Mono", 16)
        )
        self.console.pack(pady=10)
        self.console.insert("0.0", "V.E.D.: Authorized access granted. Welcome back, Mr. Surya.\n\n")

        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.pack(fill="x", side="bottom", padx=20, pady=20)

        self.entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Enter command for V.E.D...",
            width=750,
            border_color="#00d4ff"
        )
        self.entry.pack(side="left", padx=10)
        self.entry.bind("<Return>", self.execute)

        self.btn = ctk.CTkButton(
            self.input_frame,
            text="EXECUTE",
            fg_color="#00d4ff",
            text_color="black",
            command=self.execute
        )
        self.btn.pack(side="right", padx=10)

    def execute(self, event=None):
        query = self.entry.get()
        if not query:
            return
        
        self.console.insert("end", f"Mr. Surya: {query}\n")
        response = self.process_command(query)
        self.console.insert("end", f"V.E.D.: {response}\n\n")
        self.entry.delete(0, 'end')
        self.console.see("end")
