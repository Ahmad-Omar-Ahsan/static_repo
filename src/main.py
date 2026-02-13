from textnode import TextNode

def main():
    new_textnode = TextNode(text="This is an anchor text", text_type="link", url="bootdev.org")
    print(new_textnode)

if __name__=="__main__":
    main()