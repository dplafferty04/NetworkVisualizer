Net_Sentinel

Net_Sentinel is a network discovery and mapping tool. It uses FastAPI and Scapy to perform network reconnaissance and visualizes the results through a web-based interface.

Features:
ARP discovery: Performs network scans to identify active devices using the Scapy library.

Live logging: Streams real-time system logs to a draggable terminal window using FastAPI StreamingResponse.

Topology mapping: Generates a star-topology graph of the network using Vis.js.

Containerization: Includes Docker configuration for simplified deployment and network interface management.

Technical Stack
Backend: Python 3.11, FastAPI

Frontend: HTML5, Tailwind CSS, JavaScript

Networking: Scapy

Visualization: Vis.js

Installation via Docker
Docker is the recommended installation method as it manages system dependencies and network permissions.

Clone the repository: git clone https://github.com/dplafferty04/NetworkVisualizer.git cd Net-Sentinel

Start the container: docker-compose up --build

Access the interface: Navigate to http://localhost:8000 in a web browser.

Manual Installation
To run the application without Docker, ensure Python 3.10 or higher is installed along with Npcap (Windows) or libpcap (Linux/macOS).

Install Python dependencies: pip install -r requirements.txt

Run the application: uvicorn main:app --reload

Note: Administrative or root privileges are required for Scapy to perform hardware-level network scanning.

Usage Instructions
Target Input: Enter a valid CIDR range (e.g., 192.168.1.0/24) into the target field.

Execution: Click the execute scan button to begin discovery.

Logs: Monitor the terminal window for real-time status updates and discovery counts.

Visualization: Once the scan is complete, use the render topology button to view the network map.

Project Structure
frontend/: Contains the HTML and JavaScript files for the dashboard and graph.

main.py: The FastAPI application handling routing and data streaming.

arpscan.py: The scanning logic utilizing Scapy.

Dockerfile: Instructions for building the container image.

docker-compose.yml: Configuration for running the container with host network access.

Legal Disclaimer
This tool is designed for authorized network analysis and educational purposes only. Unauthorized scanning of networks is strictly prohibited and may be illegal. The developer assumes no liability for misuse of this software.

License:
This project is licensed under the MIT License.