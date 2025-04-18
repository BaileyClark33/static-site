from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
    node = TextNode("test", TextType.LINK, "https://www.boot.dev")
    node2 = HTMLNode(
        "This is an html node",
        "<p>",
        None,
        {
            "href": "https://www.google.com",
            "target": "_blank",
        },
    )

    print(node.__repr__())
    print(node2.__repr__())
    print(node2.props_to_html())


main()
