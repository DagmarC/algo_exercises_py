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
    
    
def suggestions_from_w(node: TrieNode, search_word: str, max_words=3) -> List[str]:
    words = []
    get_suggestions_rec(node, "", words, search_word, max_words)
    return words


def get_suggestions_rec(node: TrieNode, word: str, words: List[str], search_word: str, max_words: int):
    if node is None:
        return
    
    if len(words) == max_words:
        return
    
    if node.wordCount != 0:
        for _ in range(node.wordCount):
            if max_words > 0:
                words.append(search_word+word)
        
    for i, child in enumerate(node.children):
        if child is not None:
            word += chr(i + ord('a'))
            get_suggestions_rec(child, word, words, search_word, max_words)
            word = word[:len(word)-1]
            
            
def search_prefix_node(root: TrieNode, prefix: str) -> TrieNode:
    if root is None:
        return None
    prefix = prefix.lower()
    
    node = root
    for c in prefix:
        index = ord(c) - ord('a')
        if node.children[index] is None:
            return None
        node = node.children[index]
    
    return node


class Solution:
    def suggested_products_trie(self, products: List[str], search_word: str) -> List[List[str]]:
        root = TrieNode()
        for p in products:
            insert_word(root, p)
        
        result = []
        
        for i in range(len(search_word)):
            prefix_node = search_prefix_node(root, search_word[:i+1])
            prefix_result = suggestions_from_w(prefix_node, search_word[:i+1])
            result.append(prefix_result)
#            print(searchWord[:i+1], prefix_result)
        
        return result
    
    def suggested_products_bin_search(self, products: List[str], search_word: str):
        products.sort()
        suggestions = []
        max_suggestions = 3
                
        def binary_search(prefix_len: int, start: int, end: int):
            if start == end:
                return start
            
            mid = (start+end) // 2
            if products[mid] >= search_word[:prefix_len]:  # this comparison ensures that even if the prefix in word e.g. m == m, you will find the 1st word occurrence
                return binary_search(prefix_len, start, mid)  # go left
            else:
                return binary_search(prefix_len, mid+1, end)
            
        for i in range(len(search_word)):
            prefix = search_word[:i+1]
            prefix_result = []
            
            product_index = binary_search(i+1, 0, len(products))
            
            for s in range(max_suggestions):
                if (product_index+s) >= len(products):
                    break
                if products[product_index+s].startswith(prefix):
                    prefix_result.append(products[product_index+s])
                    
            suggestions.append(prefix_result)
            
        return suggestions
              
                    
if __name__ == '__main__':
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    # products = ["tatiana"]

    search_word = "mouse"
    
    solution = Solution()
    suggestions = solution.suggested_products_bin_search(products, searchWord=search_word)
        
    print(f"Suggestions for search word '{search_word}' are '{suggestions}'")
