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
            prefix = word[:i+1] # generate prefix

            if prefix not in curr_node:
                curr_node[prefix] = {}

            curr_node = curr_node[prefix]

            if i == len(word)-1:
                curr_node['\n'] = None
            i += 1

        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        print("search {}".format(word))

        #prefix_list = [word[:i] for i in range(1, len(word)+1)]
        
        i = 0
        curr_node = self.root

        while i < len(word):
            #prefix = prefix_list[i]
            prefix = word[:i+1]
            
            if prefix not in curr_node:
                return False
            else:
                curr_node = curr_node[prefix]
                i += 1

        #print(curr_node)
        if i == len(word) and '\n' in curr_node:
            return True
        else:
            return False
            
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        print("start with {}".format(prefix))

        i = 0
        curr_node = self.root

        while i < len(prefix):
            _prefix = prefix[:i+1]
            
            if _prefix not in curr_node:
                break
            else:
                curr_node = curr_node[_prefix]
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

