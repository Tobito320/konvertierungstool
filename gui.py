import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def convert_binaer_to_dezimal(value: str) -> str :
    value = value.strip().replace(',', '.')
    return str()
    

class ConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Konvertierungs-Tool")
        self.geometry("900x500")

        self.nav_frame = ctk.CTkFrame(self, width=200)
        self.nav_frame.pack(side="left", fill="y")
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.frames = {}
        self.create_nav_buttons()
        self.create_frames()
        self.show_frame("home")

    def create_nav_buttons(self):
        buttons = [
            ("Home", lambda: self.show_frame("home")),
            ("Bin\u00e4r → Dezimal", lambda: self.show_frame("b2d")),
            ("Bin\u00e4r → Hex", lambda: self.show_frame("b2h")),
            ("Dezimal → Bin\u00e4r", lambda: self.show_frame("d2b")),
            ("Dezimal → Hex", lambda: self.show_frame("d2h")),
            ("Hex → Bin\u00e4r", lambda: self.show_frame("h2b")),
            ("Hex → Dezimal", lambda: self.show_frame("h2d")),
        ]
        for text, cmd in buttons:
            btn = ctk.CTkButton(self.nav_frame, text=text, command=cmd)
            btn.pack(padx=15, pady=5, fill="x")

    def create_frames(self):
        self.frames["home"] = HomeFrame(self.content_frame)
        self.frames["b2d"] = BinaryToDecimalFrame(self.content_frame)
        # self.frames["b2h"] = BinaryToHexFrame(self.content_frame)
        # self.frames["d2b"] = DecimalToBinaryFrame(self.content_frame)
        # self.frames["d2h"] = DecimalToHexFrame(self.content_frame)
        # self.frames["h2b"] = HexToBinaryFrame(self.content_frame)
        # self.frames["h2d"] = HexToDecimalFrame(self.content_frame)
        
    def show_frame(self, name: str):
        frame = self.frames[name]
        for f in self.frames.values():
            f.pack_forget()
        frame.pack(fill="both", expand=True)
        
class HomeFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        title = ctk.CTkLabel(self, text="🏠 Home")
        title.pack(pady=5)
        label = ctk.CTkLabel(self, text="W\u00e4hle eine Umwandlung im Men\u00fc links.")
        label.pack(pady=20)

class BaseConvertFrame(ctk.CTkFrame):
    prompt: str = ""
    convert_func = None
    
    def __init__(self, master):
        super().__init__(master)
        self.entry = ctk.CTkEntry(self, placeholder_text=self.prompt)
        self.entry.pack(pady=20)
        self.result = ctk.CTkLabel(self, text="")
        self.result.pack(pady=10)
        btn = ctk.CTkButton(self, text="Umwandeln", command=self.on_convert)
        btn.pack(pady=10)
    
    def on_convert(self):
        value = self.entry.get()
        try:
            result = self.convert_func(value) # type: ignore
            self.result.configure(text=result)
        except Exception as e:
            self.result.configure(text=str(e))

class BinaryToDecimalFrame(BaseConvertFrame):
    # title = ctk.CTkLabel(self,)
    prompt: str = 'bsp: 1101'
    convert_func = staticmethod(convert_binaer_to_dezimal)
    

if __name__ == "__main__":
    app = ConverterApp()
    app.mainloop()