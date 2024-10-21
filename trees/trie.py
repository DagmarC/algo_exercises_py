from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]  # indices of letters a-z
        self.wordCount = 0


def insert_word(root: TrieNode, word: str):
    word = word.lower()
    
    node = root  # current node
    for letter in word:
        index = ord(letter) - ord('a')
        
        if node.children[index] is None:
            newNode = TrieNode()
            node.children[index] = newNode  # keep the refference of the newly added node
            
        node = node.children[index]  # go to the children node
            
    node.wordCount += 1  # end of the word, increase the word count by 1
    
    
def print_trie(root: TrieNode):
    words = []
    print_trie_rec(root, "", words)
    for word in words:
        print(word)


def print_trie_rec(node: TrieNode, word: str, words: List[str]):
    if node is None:
        return

    if node.wordCount != 0:
        buff = "["
        for i in range(node.wordCount):
            buff += word
            buff += ", "
        buff += "] Count: " + str(i+1) + "."
        words.append(buff)
        
    for i, child in enumerate(node.children):
        if child is not None:
            word += chr(i + ord('a'))
            print_trie_rec(child, word, words)
            word = word[:len(word)-1]


def search_prefix(root: TrieNode, prefix: str):
    if root is None:
        return False
    prefix = prefix.lower()
    
    node = root
    for c in prefix:
        index = ord(c) - ord('a')
        if node.children[index] is None:
            return False
        node = node.children[index]
        
    return True


def delete_word(root: TrieNode, word: str):
    delete_word_rec(root, None, word, 0)
    
    
def delete_word_rec(node: TrieNode, parent: TrieNode, word: str, i: int):
    if node is None:
        return  # word does not exist in the Trie data structure
    
    if i < len(word):
        char_index = ord(word[i]) - ord('a')
        delete_word_rec(node.children[char_index], node, word, i+1)
    
    # 1st case: prefix of other words in the Trie T[and, ant, dog] -> delete[an] (decrease the word count)
    if i == len(word) and node.wordCount > 0:
        node.wordCount -= 1
        print("decrease word count for node:", word[i-1])

    # 2nd case: shares a common prefix with other words T[and, ant, dog] -> delete[and] (delete node d - from the bottom of the trie)
    # 3rd case: does not share any common prefix with other words T[and, ant, dog] -> delete[dog] (delete all nodes g, o, d - from the bottom of the trie)
    if node.wordCount == 0 and isLeaf(node):
        if parent is not None:  # if node is not a root node
            char_index = ord(word[i-1]) - ord('a')
            parent.children[char_index] = None  # remove refference of current node from parent
            print("remove node", word[i-1])
    

def isLeaf(node: TrieNode):
    return all(child is None for child in node.children)

    
if __name__ == '__main__':
    root = TrieNode()
    insert_word(root, "andu")
    insert_word(root, "and")
    insert_word(root, "ant")
    insert_word(root, "and")
    insert_word(root, "geek")

    print_trie(root)
    
    print("===Remove===")
    
    delete_word(root, "and")
    delete_word(root, "geek")
    delete_word(root, "andu")
    delete_word(root, "anduaa")

    print_trie(root)

    