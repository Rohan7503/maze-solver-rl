# main.py

from config import NUM_NODES
from q_learning import train_agent
from graph_model import generate_random_graph
from utils import visualize_graph


def main():
    # Generate a random graph
    A = generate_random_graph(NUM_NODES)

    # Print the adjacency matrix and visualize the generated graph
    print("Generated graph:")
    for row in A:
        print(row)
    visualize_graph(A, show_weights=False, filename="input_graph")
    
    # Train the agent to learn the optimal path
    Q = train_agent(A)

    # Print the Q-table after training and visualize the graph with Q-values
    print("\nQ-table after training:")
    for row in Q:
        print(row)
    print("\nTraining complete!")
    visualize_graph(Q, show_weights=True, filename="output_graph")

if __name__ == "__main__":
    main()