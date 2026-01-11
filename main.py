from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import arpscan

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_index():
    return FileResponse('frontend/index.html')

@app.get("/scan")
async def run_network_scan(target: str = "192.168.1.0/24"):
    try:
        # AND THIS IS THE SECOND CRITICAL LINE
        devices = await arpscan.scan_network(target)
        return {"status": "success", "data": devices}
    except Exception as e:
        print(f"SERVER ERROR: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/graph")
async def read_graph():
    return FileResponse('frontend/graph.html')

