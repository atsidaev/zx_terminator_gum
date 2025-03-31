import re
import os

with open("template.html", encoding="utf-8") as f:
    template =f.readlines()

with open("index.html", "w", encoding="utf-8") as f:
    for t in template:
        if not "{{ BODY }}" in t:
            f.write(t)
        else:
            d = "series1"
            with open(f"{d}/grid.txt") as g:
                lines = g.readlines()

            for l in lines:
                m = re.match("(column|row):\s*(([0-9]{2}\s*)+)", l.strip())
                align = m.group(1)
                files = m.group(2).split()
                grid = []
                grid.append(f"\t<div style='display: flex; flex-direction: {align};'>")
                for fname in files:
                    if os.path.isfile(f"{d}/photos/{fname}.jpg"):
                        grid.append(f"\t\t<img onclick='window.location=\"{d}/photos/{fname}.jpg\";' class='found' src='{d}/T2_1_{fname}.jpg' dst='{d}/photos/{fname}.jpg' />")
                    else:
                        grid.append(f"\t\t<img src='{d}/T2_1_{fname}.jpg' />")
                grid.append("\t</div>")
                f.writelines(grid)

    f.flush()
    f.close()