class Node:
    def __init__(self, children=None, is_word=False, parent=None, parent_char=""):
        if children is None:
            children = dict()
        self.children = children  # mapping of the children
        self.is_word = is_word  # boolean to keep track if the current node is a word or a prefix
        self.parent = parent  # keeps track of the parent node. Needed only for delete operation
        self.parent_char = parent_char  # keeps track of the parent character mapping. Needed only for delete operation

    def is_empty(self):
        if self.children:
            return False
        return True

    def __repr__(self):
        return "Children: {}. Is word: {}".format(self.children, self.is_word)

    def __str__(self):
        return self.__repr__()

    def clear(self):
        self.__init__()
