# main.py

from config import NUM_NODES
from q_learning import train_agent
from graph_model import generate_random_graph


def main():
    A = generate_random_graph(NUM_NODES)
    print("Generated graph:")
    for row in A:
        print(row)
    
    Q = train_agent(A)
    print("\nQ-table after training:")
    for row in Q:
        print(row)
    
    print("\nTraining complete!")

if __name__ == "__main__":
    main()