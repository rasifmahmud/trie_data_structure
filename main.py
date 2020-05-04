from trie import Trie

if __name__ == "__main__":
    trie = Trie()
    words = ["cat", "car", "do", "dog", "done", "trie"]

    print("################## Add Function Testing ##################")
    trie.batch_insert(words)
    trie.print()

    print("################## Delete Function Testing ##################")
    trie.word_delete(trie.root, "do")
    trie.word_delete(trie.root, "trie")
    trie.word_delete(trie.root, "ca")
    trie.word_delete(trie.root, "dog")
    trie.print()

    print("################## Search Function Testing ##################")
    print(trie.word_search("dog"))
    print(trie.word_search("ca"))
    print(trie.word_search("do"))
    print(trie.word_search("trie"))
    print(trie.word_search("cat"))
    print(trie.word_search("car"))
    print(trie.word_search("done"))

    trie.prefix_delete(trie.root, "")
    trie.print()