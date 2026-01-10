from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import arpscan # This imports your existing script logic

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Serve the index.html file at the root URL (http://127.0.0.1:8000/)
@app.get("/")
async def read_index():
    # This sends the HTML file directly to the browser
    return FileResponse('frontend/index.html')

@app.get("/scan")
def run_network_scan(target: str = "192.168.1.0/24"):
    try:
        devices = arpscan.scan_network(target)
        return {"status": "success", "data": devices}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))