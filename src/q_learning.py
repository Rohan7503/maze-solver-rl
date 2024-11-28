# q_learning.py

from config import MAX_REWARD, NUM_NODES
from graph_model import get_reward_table
import random



def initialize_q_table() -> list:
    """Initialize the Q-table with zeros

    Returns:
        list: The initialized Q-table
    """
    return [[0 for i in range(NUM_NODES)] for j in range(NUM_NODES)]


def random_action(state: int, R: list) -> int:
    """Get a random action from the given state

    Args:
        state (int): The state to get the action from
        R (list): The reward table

    Returns:
        int: The random action
    """
    return random.choice([i for i in range(NUM_NODES) if R[state][i] != -1])


def update_q_table(state: int, action: int, Q: list, R: list, gamma: float = 0.8) -> None:
    """Update the Q-table using the Q-learning algorithm

    Args:
        state (int): The state to update the Q-table for
        action (int): The action to update the Q-table for
        Q (list): The Q-table to update
        R (list): The reward table
        gamma (float): The discount factor. Defaults to 0.8.
    """
    Q[state][action] = int(R[state][action] + gamma * max(Q[action]))
    Q[state][action] = min(Q[state][action], MAX_REWARD)
    

def train_agent(A: list, episodes: int = 1000) -> list:
    """Trains the agent using the Q-learning algorithm

    Args:
        A (list): The adjacency matrix of the graph
        episodes (int, optional): The number of episodes to train for. Defaults to 1000.

    Returns:
        list: The Q-table after training
    """
    Q = initialize_q_table()
    R = get_reward_table(A)
    for _ in range(episodes):
        state = random.randrange(NUM_NODES)  # Randomly select a state
        action = random_action(state, R)  # Randomly select an action
        update_q_table(state, action, Q, R)  # Update the Q-table
    
    return Q
    

