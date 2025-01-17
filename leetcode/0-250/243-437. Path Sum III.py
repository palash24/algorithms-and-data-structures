# 437. Path Sum III
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution:
    def pathSum2(self, root, sum):
        sums = []
        self.cnt = 0
        
        def helper(root):
            if not root: return
            for i in range(len(sums)):
                sums[i] += root.val
                if sums[i] == sum:
                    self.cnt += 1
                    
            if root.val == sum: self.cnt += 1
            sums.append(root.val)
            helper(root.left)
            helper(root.right)
            sums.pop()
            for i in range(len(sums)):
                sums[i] -= root.val  
        
        helper(root)
        return self.cnt

    def pathSum3(self, root, sum):
        self.sums = []

        def helper(root):
            if not root: return 0
            self.sums = list(map(lambda x: x + root.val, self.sums))
            self.sums.append(root.val)
            cnt = self.sums.count(sum)

            cnt += helper(root.left)
            cnt += helper(root.right)
            self.sums.pop()
            self.sums = list(map(lambda x: x - root.val, self.sums))

            return cnt
    
        return helper(root)

    def pathSum4(self, root, sum):
        def helper(root, sums):
            if not root: return 0
            cur_sums = list(map(lambda x: x + root.val, sums))
            cur_sums.append(root.val)
            cnt = cur_sums.count(sum)

            cnt += helper(root.left, cur_sums)
            cnt += helper(root.right, cur_sums)

            return cnt
    
        return helper(root, [])

    # leetcode
    def pathSum(self, root, target):
        self.result = 0
        self.cache = collections.defaultdict(int)
        self.cache[0] = 1

        self.dfs(root, target, 0)
        return self.result

    def dfs(self, root, target, currPathSum):
        if not root: return
        
        currPathSum += root.val
        oldPathSum = currPathSum - target
        self.result += self.cache[oldPathSum]
        self.cache[currPathSum] += 1

        self.dfs(root.left, target, currPathSum)
        self.dfs(root.right, target, currPathSum)
        self.cache[currPathSum] -= 1


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)
root.right.right = TreeNode(11)

sol = Solution()
print(sol.pathSum(root, 8))