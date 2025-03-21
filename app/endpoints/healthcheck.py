from fastapi import APIRouter, HTTPException, Query  # For API routing and error handling
from fastapi.responses import JSONResponse  # JSON response format for API output
from pydantic import BaseModel  # For data validation
import asyncio  # For async functionality
import random  # For simulating health checks
import json
import os

# Create a router instance for organizing endpoints
router = APIRouter()

# --------------------------------------------
# Data Model for Input Validation
# --------------------------------------------
class DAGInput(BaseModel):
    """
    DAGInput class defines the expected input format for the `/healthcheck` endpoint.
    
    Args:
        components (list): List of dictionaries representing DAG nodes and their dependencies.
        
    Example Input:
    {
        "components": [
            {"id": "A", "dependencies": []},
            {"id": "B", "dependencies": ["A"]},
            {"id": "C", "dependencies": ["B"]}
        ]
    }
    """
    components: list

# --------------------------------------------
# Function to Load DAG JSON File
# --------------------------------------------
def load_dag_graph(dag_file: str = "dag_graph.json") -> dict:
    """
    Loads a DAG JSON file and returns its content as a dictionary.

    Args:
        dag_file (str): The file path of the DAG JSON input.

    Returns:
        dict: Parsed JSON content.

    Raises:
        HTTPException: If the file is not found.
    """
    if not os.path.exists(dag_file):
        print(f"⚠️ Warning: DAG file '{dag_file}' not found! Returning an empty graph.")
        return {"components": []}  # Return an empty graph instead of throwing 404

    with open(dag_file, "r") as file:
        return json.load(file)

# --------------------------------------------
# Simulated Health Check Function
# --------------------------------------------
async def check_health(component_id: str) -> str:
    """
    Simulates a health check for a given component.
    
    Args:
        component_id (str): The ID of the component to be checked.

    Returns:
        str: 'healthy' or 'unhealthy' (randomized for demonstration)
    """
    await asyncio.sleep(0.5)  # Simulate a delay for health check
    return "healthy" if random.choice([True, False]) else "unhealthy"

# --------------------------------------------
# BFS Traversal with Async Health Check
# --------------------------------------------
async def bfs_health_check(graph: dict) -> dict:
    """
    Performs BFS traversal on the given graph and checks the health of each node asynchronously.

    Args:
        graph (dict): Dictionary where keys are node IDs and values are lists of dependent nodes.

    Returns:
        dict: Dictionary with node IDs as keys and their corresponding health status.
    """
    health_status = {}  # Store health status of each node
    visited = set()  # Track visited nodes to prevent cycles

    # Iterate through nodes to ensure all are covered
    for start_node in graph:
        if start_node not in visited:
            queue = [start_node]  # Initialize BFS queue with the start node
            while queue:
                node = queue.pop(0)
                if node not in visited:
                    visited.add(node)
                    health_status[node] = await check_health(node)  # Perform async health check

                    # Enqueue dependencies (unvisited nodes)
                    for neighbor in graph.get(node, []):
                        if neighbor not in visited:
                            queue.append(neighbor)

    return health_status

# --------------------------------------------
# Healthcheck Endpoint (GET Method)
# --------------------------------------------

@router.get("/", response_class=JSONResponse)
async def healthcheck_json(dag_file: str = Query("dag_graph.json", description="Path to DAG JSON file")):
    """
    Healthcheck endpoint that accepts a DAG JSON file as input via query parameter.

    Args:
        dag_file (str, optional): Path to the DAG JSON file. Defaults to `"dag_graph.json"`.

    Returns:
        JSONResponse: Health status details.
    """
    data = load_dag_graph(dag_file)
    components = data.get("components", [])
    graph = {comp["id"]: comp["dependencies"] for comp in components}

    # Perform BFS-based async health check
    health_status = await bfs_health_check(graph)

    return {
        "status": "healthy" if all(status == "healthy" for status in health_status.values()) else "unhealthy",
        "components": health_status
    }
