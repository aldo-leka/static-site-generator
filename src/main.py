import os
import shutil
import sys

from generatepage import generate_pages_recursive

basepath = "/"
if len(sys.argv) > 1:
    basepath = sys.argv[1]

def main():
    source = "static"
    destination = "docs"
    if os.path.exists(destination):
        shutil.rmtree(destination)
    copy(source, destination)
    generate_pages_recursive("content", "template.html", destination, basepath)

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