import os
from graphviz import Digraph

def visualize_graph(A: list, show_weights: bool = True, filename: str = "graph") -> None:
    """Visualize a graph from an adjacency matrix using Graphviz.

    Args:
        A (list): The adjacency matrix of the graph.
        show_weights (bool, optional): Whether to display edge weights on the graph. Defaults to True.
        filename (str, optional): The filename to save the graph image. Defaults to "graph".
    """
    # Create a directed graph with custom settings
    dot = Digraph(format="png", engine="dot")

    # Set global graph attributes
    dot.attr(dpi='300', size='8,8', nodesep='0.5', ranksep='0.5')  # Adjust size, node separation, etc.
    dot.attr(directed='true')  # Ensure it's a directed graph

    # Set layout direction to top-to-bottom and add additional attributes to make it more 2D
    dot.attr('graph', rankdir='LR', style='solid')  # 'LR' for left-to-right layout

    # Add edges with weights
    num_nodes = len(A)
    for i in range(num_nodes):
        for j in range(num_nodes):
            if A[i][j] != 0:
                if show_weights:
                    if A[i][j] == max(A[i]):
                        dot.edge(str(i), str(j), color='red')
                else:
                    dot.edge(str(i), str(j))

    # Get the path of the current script (maze_solver_rl directory)
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Define the path to the images folder
    images_folder = os.path.join(current_dir, "images")

    # Ensure the images folder exists
    os.makedirs(images_folder, exist_ok=True)

    # Render the graph and save it in the images folder
    dot.render(filename=os.path.join(images_folder, filename), cleanup=True)

