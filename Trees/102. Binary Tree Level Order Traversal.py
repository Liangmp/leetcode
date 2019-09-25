# The solution below is from gabbu https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/discuss/33550/Python-Solution-with-Detailed-Explanation

class Solution(object):
    def levelOrder(self, root):
        q, result = [], []
        if root:
            q.append(root)
        while len(q):
            level = []
            # Using BFS, at any instant only L1 and L1+1 nodes are in the queue.
            # for _ in range(len(q)) allows us to dequeue L1 nodes one by one and add L2 children one by one.
            for _ in range(len(q)):
                x = q.pop(0)
                level.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            result.append(level)
        return result