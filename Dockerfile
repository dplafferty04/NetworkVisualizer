# 1. Use a lightweight Python base
FROM python:3.11-slim

# 2. Install system dependencies for Scapy and Networking
RUN apt-get update && apt-get install -y \
    libpcap-dev \
    tcpdump \
    && rm -rf /var/lib/apt/lists/*

# 3. Set the working directory
WORKDIR /app

# 4. Copy and install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your code
COPY . .

# 6. Expose the port FastAPI runs on
EXPOSE 8000

# 7. Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]