# Easy
## 112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree 
has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,null,1], targetSum = 22
Output: true

Explanation:
The root-to-leaf path with the target sum is shown.

        5
       / \
      4   8
     /   / \
    11  13  4
   /  \      \
  7    2      1

Path: 5 → 4 → 11 → 2 = 22