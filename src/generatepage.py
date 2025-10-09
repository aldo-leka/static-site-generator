import os

from markdowntohtml import markdown_to_html_node
from extracttitle import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = ""
    with open(from_path, encoding="utf-8") as f:
        markdown = f.read()

    template = ""
    with open(template_path, encoding="utf-8") as f:
        template = f.read()

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    html_content = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w', encoding="utf-8") as f:
        f.write(html_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entries = os.listdir(dir_path_content)
    for entry in entries:
        path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry.replace(".md", ".html"))
        if os.path.isfile(path) and path.endswith(".md"):
            generate_page(path, template_path, dest_path)
        else:
            generate_pages_recursive(path, template_path, dest_path)