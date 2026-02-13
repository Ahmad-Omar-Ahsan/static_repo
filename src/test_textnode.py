import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_link(self):
        node = TextNode("This is link", TextType.LINK)
        node2 = TextNode("This is another link", TextType.LINK)
        self.assertEqual(node.text_type, node2.text_type)



if __name__ == "__main__":
    unittest.main()