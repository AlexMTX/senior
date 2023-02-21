import os

toc = list()
for filename in sorted(os.listdir(f"./chapters")):
    with open(f"./chapters/{filename}") as f:
        f.readline()  # skip first line with <!-- TOC -->
        while True:
            line = f.readline()
            if "<!-- TOC -->" in line:
                break
            else:
                line = line.replace("#", f"chapters/{filename}#")
                toc.append(line)

with open("full_content.md", "w") as f:
    f.write("# Full content\n")
    f.writelines(toc)
