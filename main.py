import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import arpscan
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
import os
import asyncio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# This handles the path correctly whether you're on Windows, Linux, or Docker
script_dir = os.path.dirname(__file__)
frontend_path = os.path.join(script_dir, "frontend")
app.mount("/frontend", StaticFiles(directory=frontend_path), name="frontend")




@app.get("/")
async def read_index():
    return FileResponse('frontend/index.html')

@app.get("/scan")
async def run_network_scan(target: str = "192.168.1.0/24"):
    async def generate_logs():
        try:
            # 1. Start-up logs
            yield "data: [SYSTEM] Initializing ARP scan protocol...\n\n"
            await asyncio.sleep(0.5) 
            yield f"data: [INFO] Targeting range: {target}\n\n"
            
            # 2. Run the actual scan (The heavy lifting)
            # This calls your arpscan.py function
            devices = await arpscan.scan_network(target)
            
            yield f"data: [SUCCESS] Analysis complete. Found {len(devices)} active nodes.\n\n"
            await asyncio.sleep(0.3)
            
            # 3. The CRITICAL line that triggers the table
            # We must send the data with the 'result: ' prefix
            yield f"result: {json.dumps(devices)}\n\n"
            
        except Exception as e:
            yield f"data: [ERROR] Scan sequence interrupted: {str(e)}\n\n"

    return StreamingResponse(generate_logs(), media_type="text/event-stream")

@app.get("/graph")
async def read_graph():
    return FileResponse('frontend/graph.html')

