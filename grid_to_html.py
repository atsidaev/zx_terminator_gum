import re
import os

def generate_ribbon(snum):
    d = "series" + str(snum)
    with open(f"{d}/grid.txt") as g:
        lines = g.readlines()

    grid = []
    for l in lines:
        m = re.match("(column|row):\s*(([0-9]{2}\s*)+)", l.strip())
        align = m.group(1)
        files = m.group(2).split()
        grid.append(f"\t<div style='display: flex; flex-direction: {align};'>")
        for fname in files:
            if os.path.isfile(f"{d}/photos/{fname}.jpg"):
                grid.append(f"\t\t<img onclick='window.location=\"{d}/photos/{fname}.jpg\";' class='found' src='{d}/T2_{snum}_{fname}.jpg' dst='{d}/photos/{fname}.jpg' />")
            else:
                grid.append(f"\t\t<img src='{d}/T2_{snum}_{fname}.jpg' />")
        grid.append("\t</div>")
    return grid

with open("template.html", encoding="utf-8") as f:
    template = f.readlines()

with open("index.html", "w", encoding="utf-8") as f:
    for t in template:
        if "{{ BODY1 }}" in t:
            f.writelines(generate_ribbon(1))
        elif "{{ BODY2 }}" in t:
            f.writelines(generate_ribbon(2))
        else:
            f.write(t)

    f.flush()
    f.close()