from bs4 import BeautifulSoup, Tag, NavigableString, PageElement
from anytree import Node

def extract_text(node: NavigableString):
    # Extract inner text from HTML node
    text: NavigableString = node.string
    if text:
        return str(text).strip()
    return None

def build_tree(html: str):
    soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
    root = Node('Root')

    body: Tag = soup.body

    def add_node(parent: Node, element: Tag):
        true_parent = parent
        for child in element.children:
            if isinstance(child, Tag):
                if child.name in {"script", "style"}: continue
                add_node(parent, child)

            if isinstance(child, NavigableString):
                text = extract_text(child)
                if not text or not len(text): continue
                # parentship is hijacked if high-level string
                parent = Node(text, parent=true_parent)


    add_node(root, body)

    return root

