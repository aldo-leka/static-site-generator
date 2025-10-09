import os
import shutil

from generatepage import generate_pages_recursive


def main():
    source = "static"
    destination = "public"
    if os.path.exists(destination):
        shutil.rmtree(destination)
    copy(source, destination)
    generate_pages_recursive("content", "template.html", "public")

def copy(source, destination):
    os.mkdir(destination)
    entries = os.listdir(source)
    for entry in entries:
        path = os.path.join(source, entry)
        dest_path = os.path.join(destination, entry)
        if os.path.isfile(path):
            shutil.copy(path, dest_path)
        else:
            copy(path, dest_path)

main()