import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Repo-Archi-Graph API", version="1.0.0")

# Configure CORS to allow frontend requests from any local origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/analyze")
async def get_architecture():
    """
    Dynamic API endpoint that serves AI-generated architectural analysis data.
    Reads from output/architecture.json and returns structured JSON response.
    """
    file_path = os.path.join("output", "architecture.json")
    
    # Check if the architecture data file exists
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="Architecture data not found. Please ensure output/architecture.json exists."
        )
    
    try:
        # Read and parse the JSON file
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Invalid JSON format in architecture.json: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error reading architecture data: {str(e)}"
        )

@app.get("/")
async def root():
    """Root endpoint providing API information"""
    return {
        "message": "Repo-Archi-Graph API",
        "version": "1.0.0",
        "endpoints": {
            "/api/analyze": "Get architectural analysis data"
        }
    }

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8080,
        log_level="info"
    )

# Made with Bob
