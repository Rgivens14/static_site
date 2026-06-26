class HTMLNode:
    def __init__(self, tag: str = None, value: str=None, children: list=None, props: dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        # Formats dict into 'key="value" key2="value2"'
        return "".join([f' {key}="{val}"' for key, val in self.props.items()])

    def __repr__(self):
        return (f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})")
    

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        
        if self.tag == None:
            return self.value
        
        result = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return result
    
        def __repr__(self) -> str:
            return f"LeafNode({self.tag}, {self.value}, {self.props})"
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("This object does not have a tag")
        
        if self.children == None:
            raise ValueError("This object does not have children. It is a leaf node")
        
        result = ""

        for child in self.children:
            result += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"