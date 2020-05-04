from node import Node


class Trie:
    def __init__(self, node=None):
        if node is None:
            node = Node()
        self.root = node

    def insert(self, word):
        current_node = self.root
        for character in word:
            if character not in current_node.children:
                new_node = Node(parent=current_node, parent_char=character)
                current_node.children[character] = new_node
                current_node = new_node
            else:
                current_node = current_node.children[character]
        current_node.is_word = True

    def word_search(self, word):
        current_node = self.root
        for character in word:
            if character not in current_node.children:
                return False
            current_node = current_node.children[character]
        return current_node.is_word

    def prefix_search(self, word):
        current_node = self.root
        for character in word:
            if character not in current_node.children:
                return False
            current_node = current_node.children[character]
        return True

    def generate_all_words(self, current_node, current_word, output_list):
        if current_node.is_word:
            output_list.append(current_word)
        for child_character, child_node in current_node.children.items():
            new_word = current_word + child_character
            self.generate_all_words(child_node, new_word, output_list)

    def print(self):
        words = list()
        self.generate_all_words(self.root, "", words)
        for word in words:
            print(word)

    def batch_insert(self, words):
        for word in words:
            self.insert(word)

    def word_delete(self, current_node, word):
        for character in word:
            if character not in current_node.children:
                # If there is no such word in the data structure
                return
            current_node = current_node.children[character]
        if not current_node.is_word and not current_node.is_empty():
            # if the key is not a valid word in the data structure
            return
        elif current_node.is_word and not current_node.is_empty():
            # if the word has children
            current_node.is_word = False
            return
        else:
            # if the word is a leaf
            parent_node = current_node.parent
            parent_char = current_node.parent_char
            del parent_node.children[parent_char]
            del current_node
            # delete other unnecessary words
            self.word_delete(parent_node, parent_char)

    def prefix_delete(self, current_node, word):
        for character in word:
            if character not in current_node.children:
                # If there is no such word in the data structure
                return
            current_node = current_node.children[character]
        parent_node = current_node.parent
        parent_char = current_node.parent_char
        if not parent_node:
            current_node.clear()
            return
        del parent_node.children[parent_char]
        del current_node
        # delete other unnecessary words
        self.prefix_delete(parent_node, parent_char)
