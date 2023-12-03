from pathlib import Path

import typer
import requests
from anytree import RenderTree

from app_htmlgraph.app import build_tree


app = typer.Typer()

@app.command()
def local(page_path: Path):
    page = page_path.read_text()
    tree = build_tree(page)
    for pre, fill, node in RenderTree(tree):
            print(f"{pre}{node.name}")


@app.command()
def request(url: str):
    response = requests.get(url)
    response.raise_for_status()
    if response.status_code == 200:
        html = response.text
        root = build_tree(html)
        for pre, fill, node in RenderTree(root):
            print(f"{pre}{node.name}")



if __name__ == "__main__":
    app()