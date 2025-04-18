import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("This is an html node", "<p>")
        node2 = HTMLNode("This is an html node", "<p>")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
