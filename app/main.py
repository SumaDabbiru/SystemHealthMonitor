from fastapi import FastAPI
from app.endpoints import healthcheck, healthcheck_ui, root

app = FastAPI()

# Include endpoints with prefixes for proper routing
app.include_router(healthcheck.router, prefix="/healthcheck")
app.include_router(healthcheck_ui.router, prefix="/healthcheckui")
app.include_router(root.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
