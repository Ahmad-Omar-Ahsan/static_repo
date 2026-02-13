
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
    
    