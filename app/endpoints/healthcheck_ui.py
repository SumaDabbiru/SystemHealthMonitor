from fastapi import APIRouter, HTTPException 
from fastapi.responses import HTMLResponse
from app.services.dag_service import load_dag_graph
from app.services.graph_service import bfs_health_check, generate_graph
import json

router = APIRouter()
@router.get("/", response_class=HTMLResponse)
async def healthcheck_ui():
    """
    Endpoint: `/healthcheckui`
    
    Description:
        This endpoint loads the DAG structure from a JSON file (`dag_graph.json`),
        performs a BFS-based health check on the components, and generates a graphical 
        representation of the system health.

    Returns:
        - **HTMLResponse**: An HTML page displaying the system health status in 
          a tabular format along with a graph visualization.

    Exceptions:
        - **500 Internal Server Error**: Raised when the JSON file is improperly formatted 
          or missing required data fields.
    """
    try:
        with open('dag_graph.json') as f:
            data = json.load(f)

        if not isinstance(data, dict) or 'components' not in data:
            raise ValueError("Invalid JSON structure. Ensure it's a dictionary with 'components' key.")

        components = data['components']
        graph = {comp['id']: comp['dependencies'] for comp in components}
        health_status = await bfs_health_check(graph)
        graph_image = generate_graph(components, health_status)

        overall_status = "healthy" if all(status == "healthy" for status in health_status.values()) else "unhealthy"

        # Generate HTML Table
        result_html = f"""
        <h1>System Health Status: {overall_status.upper()}</h1>
        <table border="1">
            <tr>
                <th>Component</th>
                <th>Status</th>
            </tr>
        """
        for component, status in health_status.items():
            color = 'green' if status == 'healthy' else 'red'
            result_html += f"<tr><td>{component}</td><td style='color:{color}'>{status}</td></tr>"
        result_html += "</table>"

        result_html += f"<h2>Graph Visualization</h2><img src='data:image/png;base64,{graph_image}'/>"

        return result_html

    except (json.JSONDecodeError, ValueError) as e:
        raise HTTPException(status_code=500, detail=f"Error loading JSON data: {str(e)}")
