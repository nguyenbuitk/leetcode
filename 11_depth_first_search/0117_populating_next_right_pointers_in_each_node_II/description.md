# Medium
## 117. Populating Next Right Pointers in Each Node II
```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:
Input: root = `[1,2,3,4,5,null,7]`\
Output: `[1,#,2,3,#,4,5,7,#]`\
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

# Key Idea
## Approach 1 - BFS
**`O(n) time, O(n) space`**
#### [Self scirpt](./self.py) || [Optimize scirpt](./bfs.py)
Similar to approach 1, problem 0116 [[Link]](../0116_populating_net_right_pointer_in_each_node/description.md)