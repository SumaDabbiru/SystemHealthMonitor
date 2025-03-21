from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home():
    """
    Displays the homepage with instructions for accessing endpoints.

    Returns:
        str: HTML content with navigation instructions.
    """
    return """
    <html>
        <head>
            <title>System Health Monitor</title>
        </head>
        <body>
            <h1>Welcome to the System Health Monitor 🚀</h1>
            <p>Go to <a href="/healthcheckui">/healthcheckui</a> for DAG health visualization.</p>
            <p>For JSON output, use:</p>
            <code>curl -X GET http://localhost:8000/healthcheck</code>
        </body>
    </html>
    """
