# How to Run Repo-Archi-Graph

## Quick Start

1. **Start the FastAPI Backend Server:**
   ```bash
   python core/scanner.py
   ```
   This will start the API server at `http://127.0.0.1:8000`

2. **Access the Visualization:**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/template/
   ```
   
   OR open the file directly:
   ```
   file:///C:/Users/HP X360/repo-archi-graph/template/index.html
   ```

## Architecture

- **Backend**: FastAPI server (`core/scanner.py`) serves the API endpoint `/api/analyze`
- **Frontend**: Interactive visualization (`template/index.html`) fetches data from the API
- **Data**: Architecture analysis results stored in `output/architecture.json`

## Troubleshooting

- If you see 404 errors for `/api/analyze`, make sure the FastAPI server is running (step 1)
- The server must be running for the frontend to fetch data
- Port 8000 must be available