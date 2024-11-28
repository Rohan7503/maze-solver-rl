from config import MAX_REWARD, NUM_NODES


def generate_random_graph(num_nodes: int) -> list:
    """Generate a random graph with the given number of nodes. The graph is represented as an adjacency matrix.

    Args:
        num_nodes (int): The number of nodes in the graph

    Returns:
        list: The adjacency matrix of the generated graph
    """
    A = [[0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [1, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 1, 1]]
    return A



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
    
