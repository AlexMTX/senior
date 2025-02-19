import os

"""
Generates the full contents in README.md

<!-- TOC --> block is expected to be automatically generated with PyCharm when headers change
https://www.jetbrains.com/help/pycharm/markdown.html#table-of-contents
"""

toc = list()
for filename in sorted(os.listdir(f"./chapters")):
    with open(f"./chapters/{filename}") as f:
        # skip first line with <!-- TOC -->
        while True:
            line = f.readline()
            if "<!-- TOC -->" in line:
                break
        # accumulate toc block content
        while True:
            line = f.readline()
            if "<!-- TOC -->" in line:
                break
            else:
                line = line.replace("(#", f"(chapters/{filename}#")
                toc.append(line)

with open("README.md", "w") as f:
    f.write("# Python Questions for Senior and Lead roles\n")
    f.write("""<img src="https://user-images.githubusercontent.com/67960818/159924991-ad7ac6de-facf-4cb0-a8c9-31a7407fb9e4.png" alt="python-logo-master-v3-TM-flattened" style="max-width: 100%;">\n\n""")
    f.writelines(toc)
