import pyperclip

while True:
    name = input("    Class: ").strip()
    time = input("    Time: ").strip()
    weeks = input("    Weeks: ").strip()
    room = input("    Room: ").strip()

    if name == "" and time == "" and weeks == "" and room == "":
        break

    if len(name) > 20:
        midpoint = len(name) / 2
        spaces = [pos for pos, char in enumerate(name) if char == " "]
        best_to_split = sorted(spaces, key=lambda x: (x - midpoint) ** 2)[0]
        name = name[:best_to_split] + " \\newline " + name[best_to_split + 1 :]

    template = "\\textcolor{CtpMauve}{\\centering $$NAME$$} & \\textcolor{CtpPink}{$$TIME$$} & \\textcolor{CtpYellow}{$$WEEKS$$} & \\textcolor{CtpTeal}{$$ROOM$$} \\\\"
    template = template.replace("$$NAME$$", name)
    template = template.replace("$$TIME$$", time)
    template = template.replace("$$WEEKS$$", weeks)
    template = template.replace("$$ROOM$$", room)

    pyperclip.copy(template)
