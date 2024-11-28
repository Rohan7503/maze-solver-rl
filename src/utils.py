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
                    dot.edge(str(i), str(j), label=str(A[i][j]))
                else:
                    dot.edge(str(i), str(j))

    # Save the graph as a PNG image in "../images" directory
    dot.render(filename=f"../images/{filename}", cleanup=True)

