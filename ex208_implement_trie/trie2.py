"""

Trie implementation.

Here I used dictionaries of dictionaries as my data structure.

character-based.
"""
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        print("insert {}".format(word))
        i = 0
        curr_node = self.root

        while i < len(word):
            c = word[i] # generate prefix

            if c not in curr_node:
                curr_node[c] = {}

            curr_node = curr_node[c]

            if i == len(word)-1:
                curr_node['\n'] = None
            i += 1

        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        print("search {}".format(word))

        i = 0
        curr_node = self.root

        while i < len(word):
            c = word[i]
            
            if c not in curr_node:
                break
            else:
                curr_node = curr_node[c]
                i += 1

        return i == len(word) and '\n' in curr_node
            
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        print("start with {}".format(prefix))

        i = 0
        curr_node = self.root

        while i < len(prefix):
            c = prefix[i]
            
            if c not in curr_node:
                break
            else:
                curr_node = curr_node[c]
                i += 1

        return i == len(prefix)        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':

    input_list = [
        [("insert", "apple"), ("search", "apple"), ("search", "app"), ("start", "app"), ("insert", "app"), ("search", "app")],
        [("insert", "apple"), ("start", "b")] 
    ]

    for inp in input_list:
        trie = Trie()

        for cmd in inp:
            if cmd[0] == "insert":
                trie.insert(cmd[1])
            if cmd[0] == "search":
                result = trie.search(cmd[1])
                print(result)
            if cmd[0] == "start":
                result = trie.startsWith(cmd[1])
                print(result)
        print(trie.root)
        print("------------")

