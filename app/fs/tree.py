import json


class FSTreeNode:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.children = []

    def find_parent(self, target_node):
        if target_node in self.children:
            return self
        for child in self.children:
            parent = child.find_parent(target_node)
            if parent:
                return parent
        return None

    def __str__(self):
        attributes = [
            f"{key}: {getattr(self, key)}"
            for key in dir(self)
            if not key.startswith("__") and not callable(getattr(self, key))
        ]
        return f"{', '.join(attributes)}"


def build_tree(data):
    children = data.pop("children", None)
    node = FSTreeNode(**data)
    if children:
        for child in children:
            child_node = build_tree(child)
            node.children.append(child_node)
    return node

with open("db.json") as f:
    data = json.load(f)

tree = build_tree(data)
