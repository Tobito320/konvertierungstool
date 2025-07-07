import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class KonverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Konvertierungs-Tool")
        self.geometry("900x500")

        self.nav_frame = ctk.CTkFrame(self, width=200)
        self.nav_frame.pack(side="left", fill="y")

app = KonverterApp()
app.mainloop()