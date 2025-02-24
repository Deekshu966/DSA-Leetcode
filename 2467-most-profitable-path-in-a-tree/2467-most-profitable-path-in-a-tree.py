from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges, bob, amount):
        # Step 1: Construct the tree as an adjacency list
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Step 2: Find Bob's path and store the time taken to reach each node
        bob_time = {}  # Stores Bob's arrival time at each node
        
        def dfs_bob(node, parent, time):
            bob_time[node] = time
            if node == 0:  # Stop once Bob reaches the root (node 0)
                return True
            for neighbor in tree[node]:
                if neighbor != parent and dfs_bob(neighbor, node, time + 1):
                    return True  # Propagate the success upwards
            return False
        
        dfs_bob(bob, -1, 0)

        # Step 3: DFS for Alice to maximize profit
        max_profit = float('-inf')  # Track maximum profit

        def dfs_alice(node, parent, time, current_profit):
            nonlocal max_profit  # Correct use of nonlocal

            # Compute Alice's profit at this node
            if node in bob_time:
                if bob_time[node] > time:  # Alice arrives first
                    current_profit += amount[node]
                elif bob_time[node] == time:  # Both arrive simultaneously
                    current_profit += amount[node] // 2
            else:  # Alice alone
                current_profit += amount[node]

            # If Alice reaches a leaf node, update max_profit
            is_leaf = True
            for neighbor in tree[node]:
                if neighbor != parent:
                    is_leaf = False
                    dfs_alice(neighbor, node, time + 1, current_profit)

            if is_leaf:
                max_profit = max(max_profit, current_profit)

  
