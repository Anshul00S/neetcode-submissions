class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        def addWord(node, word):
            cur = node
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            
            cur.isWord = True
        
        for word in words:
            addWord(root, word)
        
        res = set()
        visit = set()

        def dfs(r,c,word, node):
            if r >= len(board) or c >= len(board[0]) or r < 0 or c < 0 or board[r][c] not in node.children or (r,c) in visit:
                return False
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord:
                res.add(word)
            
            dfs(r+1, c, word, node)
            dfs(r, c+1, word, node)
            dfs(r-1, c, word, node)
            dfs(r, c-1, word, node)

            visit.remove((r,c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c, "", root)

        return list(res)
