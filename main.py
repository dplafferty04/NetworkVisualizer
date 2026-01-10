from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import arpscan # This imports your existing script logic

app = FastAPI()

# This part is CRITICAL. It allows your React/HTML frontend 
# to talk to this API without being blocked by browser security.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Network Scanner API is Running"}

@app.get("/scan")
def run_network_scan(target: str = "192.168.1.0/24"):
    try:
        # We call the function you wrote in arpscan.py
        devices = arpscan.scan_network(target)
        return {"status": "success", "data": devices}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))