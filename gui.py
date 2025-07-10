import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def convert_binaer_to_dezimal(value: str) -> str :
    # Leerzeichen entfernen und Komma zu Punkt machen
    value = value.strip().replace(',', '.')

    # Ganz- und Nachkommateil trennen
    if '.' in value:
        teile = value.split('.')  # z. B. "1011.01" → ["1011", "01"]
        ganzteil = teile[0]
        nachkomma = teile[1]
    else:
        ganzteil = value
        nachkomma = ""

    # Ganzzahl-Teil umrechnen
    dezimal_ganz = 0
    for i in range(len(ganzteil)):
        bit = ganzteil[-(i+1)]  # von rechts nach links
        if bit == '1':
            dezimal_ganz += 2 ** i

    # Nachkommabereich umrechnen
    dezimal_nachkomma = 0
    for i in range(len(nachkomma)):
        bit = nachkomma[i]
        if bit == '1':
            dezimal_nachkomma += 2 ** -(i+1)

    # Ergebnis zusammenrechnen und als String zurückgeben
    ergebnis = dezimal_ganz + dezimal_nachkomma
    return str(ergebnis)

def convert_binaer_to_hexadezimal(value: str) -> str:
    dezimal_str = convert_binaer_to_dezimal(value)
    dezimal = str(dezimal_str)

    hex_ergebnis = convert_dezimal_to_hexadezimal(dezimal)

    return hex_ergebnis

def convert_dezimal_to_binaer(value: str) -> str:
    # Erst: Dezimal zu Hex
    hex_wert = convert_dezimal_to_hexadezimal(value)

    # Dann: Hex zu Binär
    binaer = convert_hexadezimal_to_binaer(hex_wert)

    return binaer

def convert_dezimal_to_hexadezimal(value: str) -> str:
    value = value.strip().replace(',', '.')
    zahl = float(value)

    # Ganz- und Nachkommateil trennen
    ganzteil = int(zahl)
    nachkomma = zahl - ganzteil

    # Ganzteil in Hex umwandeln
    hex_ganz = hex(ganzteil)[2:].upper()

    # Nachkommateil in Hex umwandeln (max 10 Stellen)
    hex_nachkomma = ""
    if nachkomma > 0:
        hex_nachkomma = "."
        for _ in range(10):
            nachkomma *= 16
            stelle = int(nachkomma)
            if stelle < 10:
                hex_nachkomma += str(stelle)
            else:
                hex_nachkomma += chr(ord('A') + stelle - 10)
            nachkomma -= stelle
        
        hex_nachkomma = hex_nachkomma.rstrip("0")
        if hex_nachkomma == ".":
            hex_nachkomma = ""

    return hex_ganz + hex_nachkomma

def convert_hexadezimal_to_binaer(value: str) -> str:
    # return convert_dezimal_to_binaer(convert_hexadezimal_to_dezimal(value))
    value = value.strip().replace(',', '.').upper()

    # Ganz- und Nachkommateil trennen
    if '.' in value:
        teile = value.split('.')
        ganzteil = teile[0]
        nachkomma = teile[1]
    else:
        ganzteil = value
        nachkomma = ""

    # Hex-Zeichen zu Binär (Ganzteil)
    binaer_ganz = ""
    for zeichen in ganzteil:
        dez = int(zeichen, 16)
        binaer_teil = bin(dez)[2:].zfill(4)  # immer 4 Stellen
        binaer_ganz += binaer_teil

    # Hex-Zeichen zu Binär (Nachkommateil)
    binaer_nachkomma = ""
    for zeichen in nachkomma:
        dez = int(zeichen, 16)
        binaer_teil = bin(dez)[2:].zfill(4)
        binaer_nachkomma += binaer_teil

    if binaer_nachkomma:
        return binaer_ganz + "." + binaer_nachkomma
    else:
        return binaer_ganz

def convert_hexadezimal_to_dezimal(value: str) -> str:
    value = value.strip().replace(',', '.').upper()

    # Ganz- und Nachkommateil trennen
    if '.' in value:
        teile = value.split('.')
        ganzteil = teile[0]
        nachkomma = teile[1]
    else:
        ganzteil = value
        nachkomma = ""

    # Ganzteil umrechnen
    dezimal_ganz = 0
    for i in range(len(ganzteil)):
        stelle = ganzteil[-(i+1)]
        if stelle.isdigit():
            wert = int(stelle)
        else:
            wert = ord(stelle) - ord('A') + 10
        dezimal_ganz += wert * (16 ** i)

    # Nachkommabereich umrechnen
    dezimal_nachkomma = 0
    for i in range(len(nachkomma)):
        stelle = nachkomma[i]
        if stelle.isdigit():
            wert = int(stelle)
        else:
            wert = ord(stelle) - ord('A') + 10
        dezimal_nachkomma += wert * (16 ** -(i+1))

    # Ergebnis zusammenfassen
    ergebnis = dezimal_ganz + dezimal_nachkomma
    return str(ergebnis)

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
        # self.nav_buttons = []
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
            # , fg_color="grey"
            btn = ctk.CTkButton(self.nav_frame, text=text, command=cmd)
            btn.pack(padx=15, pady=5, fill="x")
            # self.nav_buttons.append((text, btn))

    def create_frames(self):
        self.frames["home"] = HomeFrame(self.content_frame)
        self.frames["b2d"] = BinaryToDecimalFrame(self.content_frame)
        self.frames["b2h"] = BinaryToHexFrame(self.content_frame)
        self.frames["d2b"] = DecimalToBinaryFrame(self.content_frame)
        self.frames["d2h"] = DecimalToHexFrame(self.content_frame)
        self.frames["h2b"] = HexToBinaryFrame(self.content_frame)
        self.frames["h2d"] = HexToDecimalFrame(self.content_frame)
        
    def show_frame(self, name: str):
        frame = self.frames[name]
        for f in self.frames.values():
            f.pack_forget()
        frame.pack(fill="both", expand=True)
        # for label, btn in self.nav_buttons()
        
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
    
    def __init__(self, master, system: str):
        super().__init__(master)
        
        self.system = system
        
        vcmd = (self.register(self.validate_input), "%P")
        self.entry = ctk.CTkEntry(self, placeholder_text=self.prompt, validate="key", validatecommand=vcmd)
        self.entry.pack(pady=20)
        
        # self.entry = ctk.CTkEntry(self, placeholder_text=self.prompt)
        # self.entry.pack(pady=20)
        
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
            
    def validate_input(self, new_value: str) -> bool:
        new_value = new_value.upper()

        if new_value.count(".") > 1 or new_value.startswith("."):
            return False

        if self.system == "binary":
            allowed = "01."
        elif self.system == "decimal":
            allowed = "0123456789."
        elif self.system == "hex":
          allowed = "0123456789ABCDEF."
        else:
            return False

        return all(c in allowed for c in new_value)

class BinaryToDecimalFrame(BaseConvertFrame):
    # title = ctk.CTkLabel(self,)
    prompt: str = 'bsp: 1101,01'
    
    def __init__(self, master):
        super().__init__(master, system="binary")
        self.convert_func = staticmethod(convert_binaer_to_dezimal)
    
class BinaryToHexFrame(BaseConvertFrame):
    prompt = "z.B. 1011,01"
    
    def __init__(self, master):
        super().__init__(master, system="binary")
        self.convert_func = staticmethod(convert_binaer_to_hexadezimal)

class DecimalToBinaryFrame(BaseConvertFrame):
    prompt = "z.B. 10,75"
    def __init__(self, master):
        super().__init__(master, system="decimal")
        self.convert_func = staticmethod(convert_dezimal_to_binaer)

class DecimalToHexFrame(BaseConvertFrame):
    prompt = "z.B. 10,75"
    def __init__(self, master):
        super().__init__(master, system="decimal")
        self.convert_func = staticmethod(convert_dezimal_to_hexadezimal)

class HexToBinaryFrame(BaseConvertFrame):
    prompt = "z.B. A1"
    def __init__(self, master):
        super().__init__(master, system="hex")
        self.convert_func = staticmethod(convert_hexadezimal_to_binaer)

class HexToDecimalFrame(BaseConvertFrame):
    prompt = "z.B. A1"
    def __init__(self, master):
        super().__init__(master, system="hex")
        self.convert_func = staticmethod(convert_hexadezimal_to_dezimal)

if __name__ == "__main__":
    app = ConverterApp()
    app.mainloop()