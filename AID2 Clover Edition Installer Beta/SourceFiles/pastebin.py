from urllib import request
import re
import os
from pathlib import Path

fnamesSoFar = {}


def filename(s):
    fname = re.sub("-$", "", re.sub("^-", "", re.sub("[^a-zA-Z0-9_-]+", "-", s)))
    n = 1
    fname2 = fname
    while fname2 in fnamesSoFar:
        n += 1
        fname2 = fname + "-" + str(n)
    fnamesSoFar[fname2] = True
    return fname2


paste = request.urlopen("https://pastebin.com/raw/KD4yN2Gc").read().decode("utf-8")
paste = re.sub(r'\nTAGS:.*\n', '\n', paste)
#pipe is never used in paste so use it as a seperator
paste = re.sub("=====+", "|", paste)
paste = re.sub("\r", "", paste)
paste = re.sub("\n\s*\n\s*", "\n\n", paste)
sections = re.findall(r"[^|]+", paste)
for sect in sections[2:][:-1]:
    category = re.search(r"\*\*\*([^\*]+)\*\*\*", sect).group(1)
    category = re.sub(".[pP]rompts?$", "", category)
    category = filename(category)
    Path("prompts", category).mkdir(exist_ok=True)
    print(category)
    for story in [x for x in filter(None, sect.split("\n\n"))][1:]:
        title = re.search(r"^\(([^\)]+)", story)
        if bool(title):
            title = title.group(1)
        else:
            title = story[:30]
        title = filename(title) + ".txt"
        with Path("prompts", category, title).open("w", encoding="UTF-8") as f:
            f.write(re.sub(r"^\([^\)]+\)\n", "", story))
