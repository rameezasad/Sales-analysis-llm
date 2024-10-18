from fastapi import FastAPI
from app.api.endpoints import router as endpoint_router  # Import the router from the endpoint module

app = FastAPI()

# Include the API router from the endpoint module
app.include_router(endpoint_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
