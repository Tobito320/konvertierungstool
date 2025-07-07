# Projekt: Konvertierungs-Tool
# Name: Ahmed Abou Dmag
# Klasse: IT24B

# Module:
# 1: Binär zu Dezimal
# 2: Binär zu Hexadezimal
# 3: Dezimal zu Binär
# 4: Dezimal zu Hexadezimal
# 5: Hexadezimal zu Binär
# 6: Hexadezimal zu Dezimal
# 7: Programm beenden

def binaer_zu_dezimal():
    while True:
        s = input("Bitte gebe die Binärzahl ein (nur 0 und 1, Komma für Bruchteil): ").strip()
        if not s:
            print("Eingabe leer, bitte erneut eingeben.")
            continue
        s = s.replace(',', '.')
        vorzeichen = -1 if s.startswith('-') else 1
        if s[0] in '+-':
            s = s[1:]
        if s.count('.') > 1:
            print("Ungültiges Format: Mehrere Trennzeichen.")
            continue
        teil_ganz, *rest = s.split('.')
        teil_frac = rest[0] if rest else ''
        if any(c not in '01' for c in teil_ganz + teil_frac) or not (teil_ganz or teil_frac):
            print("Ungültige Binärziffern! Bitte nur 0 und 1 verwenden.")
            continue
        break
    dez_int = sum(int(bit) * (2 ** i) for i, bit in enumerate(reversed(teil_ganz)))
    dez_frac = sum(int(bit) * (2 ** -i) for i, bit in enumerate(teil_frac, start=1))
    ergebnis = vorzeichen * (dez_int + dez_frac)
    print(f"Dezimal: {ergebnis}")

def binaer_zu_hexadezimal():
    while True:
        s = input("Bitte gebe die Binärzahl ein (nur 0 und 1, Komma für Bruchteil): ").strip()
        if not s:
            print("Eingabe leer, bitte erneut eingeben.")
            continue
        s = s.replace(',', '.')
        vorzeichen = '-' if s.startswith('-') else ''
        if s[0] in '+-': s = s[1:]
        if s.count('.') > 1:
            print("Ungültiges Format: Mehrere Trennzeichen.")
            continue
        teil_ganz, *rest = s.split('.')
        teil_frac = rest[0] if rest else ''
        if any(c not in '01' for c in teil_ganz + teil_frac) or not (teil_ganz or teil_frac):
            print("Ungültige Binärziffern! Nur 0 und 1 erlaubt.")
            continue
        break
    
    dez_int = sum(int(bit) * (2 ** i) for i, bit in enumerate(reversed(teil_ganz)))
    dez_frac = sum(int(bit) * (2 ** -i) for i, bit in enumerate(teil_frac, start=1))
    
    hex_int = hex(dez_int)[2:].upper() if dez_int != 0 else '0'
    hex_frac = ''
    if dez_frac:
        hex_frac = '.'
        for _ in range(10):
            dez_frac *= 16
            digit = int(dez_frac)
            hex_frac += str(digit) if digit < 10 else chr(ord('A') + digit - 10)
            dez_frac -= digit
    print(f"Hexadezimal: {vorzeichen}{hex_int}{hex_frac}")


def dezimal_zu_binaer():
    s = input("Bitte gebe die Dezimalzahl ein: ").strip().replace(',', '.')
    try:
        num = float(s)
    except ValueError:
        print("Ungültige Dezimalzahl!")
        return
    vor = '-' if num < 0 else ''
    num = abs(num)
    ganz = int(num)
    frac = num - ganz
    binaer_ganz = bin(ganz)[2:] if ganz != 0 else '0'
    binaer_frac = ''
    if frac:
        binaer_frac = '.'
        for _ in range(10):
            frac *= 2
            bit = int(frac)
            binaer_frac += str(bit)
            frac -= bit
    print(f"Binär: {vor}{binaer_ganz}{binaer_frac}")

def dezimal_zu_hexadezimal():
    s = input("Bitte gebe die Dezimalzahl ein: ").strip().replace(',', '.')
    try:
        num = float(s)
    except ValueError:
        print("Ungültige Dezimalzahl!")
        return
    vor = '-' if num < 0 else ''
    num = abs(num)
    ganz = int(num)
    frac = num - ganz
    hex_ganz = hex(ganz)[2:].upper() if ganz != 0 else '0'
    hex_frac = ''
    if frac:
        hex_frac = '.'
        for _ in range(10):
            frac *= 16
            z = int(frac)
            hex_frac += str(z) if z < 10 else chr(ord('A') + z - 10)
            frac -= z
    print(f"Hexadezimal: {vor}{hex_ganz}{hex_frac}")

def hexadezimal_zu_binaer():
    s = input("Bitte gebe die Hexadezimalzahl ein: ").strip().replace(',', '.')
    vor = '-' if s.startswith('-') else ''
    if s[0] in '+-': s = s[1:]
    if s.count('.') > 1:
        print("Ungültiges Format: Mehrere Trennzeichen.")
        return
    teil_ganz, *rest = s.split('.')
    teil_frac = rest[0] if rest else ''
    if any(c not in '0123456789ABCDEFabcdef' for c in teil_ganz + teil_frac):
        print("Ungültige Hexadezimalziffern!")
        return
    binaer_ganz = ''.join(f"{int(c,16):04b}" for c in teil_ganz).lstrip('0') or '0'
    binaer_frac = '.' + ''.join(f"{int(c,16):04b}" for c in teil_frac) if teil_frac else ''
    print(f"Binär: {vor}{binaer_ganz}{binaer_frac}")

def hexadezimal_zu_dezimal():
    s = input("Bitte gebe die Hexadezimalzahl ein: ").strip().replace(',', '.')
    vorzeichen = -1 if s.startswith('-') else 1
    if s[0] in '+-': s = s[1:]
    if s.count('.') > 1:
        print("Ungültiges Format: Mehrere Trennzeichen.")
        return
    teil_ganz, *rest = s.split('.')
    teil_frac = rest[0] if rest else ''
    try:
        dez_ganz = int(teil_ganz, 16)
    except ValueError:
        print("Ungültige Hexadezimalstelle im Ganzteil!")
        return
    dez_frac = sum(int(d,16) * 16**-i for i, d in enumerate(teil_frac, start=1))
    print(f"Dezimal: {vorzeichen * (dez_ganz + dez_frac)}")

def main():
    abstand = "-"*50
    while True:
        print(abstand)
        print("1: Binär zu Dezimal")
        print("2: Binär zu Hexadezimal")
        print("3: Dezimal zu Binär")
        print("4: Dezimal zu Hexadezimal")
        print("5: Hexadezimal zu Binär")
        print("6: Hexadezimal zu Dezimal")
        print("7: Programm beenden")
        wahl = input("Wähle ein Modul (1-7): ")
        if wahl == '1':
            binaer_zu_dezimal()
        elif wahl == '2':
            binaer_zu_hexadezimal()
        elif wahl == '3':
            dezimal_zu_binaer()
        elif wahl == '4':
            dezimal_zu_hexadezimal()
        elif wahl == '5':
            hexadezimal_zu_binaer()
        elif wahl == '6':
            hexadezimal_zu_dezimal()
        elif wahl == '7':
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Auswahl, bitte erneut versuchen.")

if __name__ == "__main__":
    main()