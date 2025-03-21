import json
import os

def load_dag_graph():
    """Loads the DAG JSON structure from the file."""
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'dag_graph.json')
    try:
        with open(file_path) as f:
            data = json.load(f)
        return data.get('components', [])
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ Error: '{file_path}' file not found!")




