import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        print(html_node.props_to_html())

    def test_repr(self):
        html_node = HTMLNode(
            tag = "<l>",
            value = "something something google.com",
            props={
            "href": "https://www.google.com",
            "target": "_blank",
        }
        )
        print(html_node)