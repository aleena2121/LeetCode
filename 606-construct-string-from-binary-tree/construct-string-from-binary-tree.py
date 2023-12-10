class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # Check if the tree is empty
        if not root:
            return ""
        
        # Initialize an empty result string
        res = ""
        # Initialize a stack for iterative traversal
        stack = [root]
        # Use a set to track visited nodes
        visited = set()
        
        # Iterate through the tree using a stack
        while stack:
            # Get the current node from the top of the stack
            cur = stack[-1]
            
            # If the current node is already visited, pop it from the stack and close the parenthesis
            if cur in visited:
                stack.pop()
                res += ")"
            else:
                # If the current node is not visited, mark it as visited and add its value to the result
                visited.add(cur)
                res += f"({cur.val}"
                
                # If the current node has no left child and a right child, add an empty pair of parentheses
                if not cur.left and cur.right:
                    res += "()"
                
                # Add the right child to the stack if it exists
                if cur.right:
                    stack.append(cur.right)
                # Add the left child to the stack if it exists
                if cur.left:
                    stack.append(cur.left)
                
        # Return the result string with leading '(' and trailing ')' removed
        return res[1:-1]