def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.lstrip("# ").rstrip()

    raise Exception("missing h1 header")