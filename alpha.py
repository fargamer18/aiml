# Global variables for maximum and minimum values
maximum, minimum = 1000, -1000

def fun_alphabeta(d, node, maxp, v, A, B):
    # Base case: when depth reaches 3 (leaf nodes)
    if d == 3:
        return v[node]
    
    # Max player's turn (maximizing player)
    if maxp:
        best = minimum  # Start with the lowest possible value
        for i in range(0, 2):  # Explore two child nodes
            # Recursively call with next depth, child node, and switched player
            value = fun_alphabeta(d+1, node*2+i, False, v, A, B)
            
            # Update best value to maximum of current best and new value
            best = max(best, value)
            
            # Update alpha (A)
            A = max(A, best)
            
            # Alpha-Beta pruning: if beta is less than or equal to alpha, break
            if B <= A:
                break
        return best
    
    # Min player's turn (minimizing player)
    else:
        best = maximum  # Start with the highest possible value
        for i in range(0, 2):  # Explore two child nodes
            # Recursively call with next depth, child node, and switched player
            value = fun_alphabeta(d+1, node*2+i, True, v, A, B)
            
            # Update best value to minimum of current best and new value
            best = min(best, value)
            
            # Update beta (B)
            B = min(B, best)
            
            # Alpha-Beta pruning: if beta is less than or equal to alpha, break
            if B <= A:
                break
        return best

# Main program
scr = []  # List to store leaf node values

# Input leaf node values
x = int(input("Enter total number of leaf node:"))
for i in range(x):
    y = int(input("Enter node value"))
    scr.append(y)

# Input depth and starting node
d = int(input("Enter depth value:"))
node = int(input("Enter node value:"))

# Call Alpha-Beta pruning algorithm and print result
print("The optimal value is:", fun_alphabeta(d, node, True, scr, minimum, maximum))
