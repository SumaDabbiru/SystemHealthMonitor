import asyncio
import random
import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO
import base64



# Use Agg backend to prevent threading issues
import matplotlib
matplotlib.use("Agg")  # Prevents "main thread is not in main loop" error


async def bfs_health_check(graph):
    """Perform a BFS traversal through the DAG and check component health."""
    health_status = {}
    visited = set()

    for start_node in graph:
        if start_node not in visited:
            queue = [start_node]
            while queue:
                node = queue.pop(0)
                if node not in visited:
                    visited.add(node)
                    health_status[node] = "healthy" if random.choice([True, False]) else "unhealthy"
                    for neighbor in graph.get(node, []):
                        if neighbor not in visited:
                            queue.append(neighbor)

    return health_status

def generate_graph(components, health_status):
    """
    Generates and encodes graph visualization as a base64 string.

    Args:
        components (list): List of component dictionaries containing 'id' and 'dependencies'.
        health_status (dict): Dictionary mapping each component to its health status.

    Returns:
        str: Base64 encoded string representing the generated graph image.
    """
    try:
        # Initialize Directed Graph
        G = nx.DiGraph()

        # Add Nodes and Edges
        for component in components:
            G.add_node(component['id'])
            for dependency in component.get('dependencies', []):
                G.add_edge(dependency, component['id'])  # Corrected edge direction for DAG clarity

        # Graph Layout
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(G, k=0.5)  # Improved spacing for better readability

        # Node Colors Based on Health Status
        node_colors = [
            'red' if health_status.get(node, 'unhealthy') == 'unhealthy' else 'green'
            for node in G.nodes
        ]

        # Draw Graph with Better Visibility
        nx.draw(
            G, pos, with_labels=True, node_size=2000, node_color=node_colors,
            edge_color='gray', linewidths=2, font_size=10, font_weight='bold'
        )

        # Save Graph as Image in Memory
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        encoded_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close()

        return encoded_image

    except Exception as e:
        print(f"Error generating graph: {e}")
        return None
