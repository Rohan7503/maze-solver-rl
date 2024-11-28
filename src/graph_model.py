from config import MAX_REWARD, NUM_NODES
import random


def dfs(matrix: list, node: int, visited: list) -> None:
    """Perform Depth First Search (DFS) on the graph represented by the adjacency matrix

    Args:
        matrix (list): The adjacency matrix of the graph
        node (int): The starting node for DFS
        visited (list): A list to keep track of visited nodes. Initially, pass a list of False values of length equal to the number of nodes in the graph.
    """
    visited[node] = True
    for neighbor in range(len(matrix)):
        if matrix[node][neighbor] == 1 and not visited[neighbor]:
            dfs(matrix, neighbor, visited)



def is_connected(matrix: list) -> bool:
    """Check if the graph represented by the adjacency matrix is connected

    Args:
        matrix (list): The adjacency matrix of the graph to check for connectivity

    Returns:
        bool: Whether the graph is connected or not
    """
    visited = [False] * len(matrix)
    dfs(matrix, 0, visited)  # Start DFS from the first node
    return all(visited)



def generate_random_graph(N: int) -> list:
    """Generate a random unweighted adjacency matrix for a connected graph
    with at least one connection to the (N-1)th node.

    Args:
        N (int): The number of nodes in the graph.

    Returns:
        list: The adjacency matrix representing the graph.
    """
    while True:
        # Generate a random symmetric adjacency matrix
        matrix = [[0] * N for _ in range(N)]
        
        for i in range(N):
            for j in range(i + 1, N):  # Avoid diagonal elements
                # Randomly set 0 or 1 for edges (avoid self-loops)
                matrix[i][j] = matrix[j][i] = random.choice([0, 1])

        # Ensure the (N-1)th node is connected to at least one other node
        if random.choice([True, False]):
            matrix[random.randint(0, N-2)][N-1] = matrix[N-1][random.randint(0, N-2)] = 1

        # Check if the graph is connected
        if is_connected(matrix):
            matrix[N-1][N-1] = 1  # Set the goal node to be connected to itself
            return matrix



def get_reward_table(A: list) -> list:
    """Generate the reward table for the input graph. The reward table is a 2D list where each element is the reward for transitioning from one state to another.
    - -1, if there is no transition possible.
    - MAX_REWARD, if the transition is to the goal state (N-1).
    - 0, otherwise.

    Args:
        A (list): The adjacency matrix of the graph

    Returns:
        list: The reward table
    """
    R = [[-1 for i in range(NUM_NODES)] for j in range(NUM_NODES)]
    for i in range(NUM_NODES):
        for j in range(NUM_NODES):
            if A[i][j] == 1:
                R[i][j] = 0 if j != NUM_NODES-1 else MAX_REWARD
    
    return R
    
