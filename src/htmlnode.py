
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag 
        self.value = value 
        self.children = children 
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        formatted_str = ""
        if self.props is None:
            return formatted_str
        for key, item in self.props.items():
            formatted_str += f' {key}="{item}"'
        return formatted_str
    

    def __repr__(self):
        return f"Tag: {self.tag},\nValue: {self.value},\nChildren: {self.children},\nProps: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return f"{self.value}"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>" if self.props is None else f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"Tag: {self.tag},\nValue: {self.value}, \nProps: {self.props}"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        

    def to_html(self):
        if self.tag is None:
            raise ValueError
        if self.children is None:
            raise ValueError("")
        else:
            combined_str = ""
            for child in self.children:
                combined_str += child.to_html()
            return f"<{self.tag}>{combined_str}</{self.tag}>"
