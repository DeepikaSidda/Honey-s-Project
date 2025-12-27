# 💻 Local Deployment Guide

Run the ML Model API on your local machine for development and testing.

---

## 📋 Prerequisites

Before you start, make sure you have:

- **Python 3.11+** installed ([Download Python](https://www.python.org/downloads/))
- **Docker Desktop** (optional, for containerized deployment) ([Download Docker](https://www.docker.com/products/docker-desktop/))
- **Git** (to clone the repository) ([Download Git](https://git-scm.com/downloads))

---

## 🚀 Method 1: Run with Python (Recommended for Development)

### Step 1: Clone the Repository

```bash
# Clone from GitHub
git clone https://github.com/DeepikaSidda/Honey-s-Project.git
cd Honey-s-Project
```

Or if you already have the files locally:
```bash
cd ML-Model-Serving-with-FastAPI-and-Docker-main
```

### Step 2: Create Virtual Environment (Recommended)

**Windows (PowerShell):**
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Windows (Command Prompt):**
```cmd
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

**Expected output:**
```
Successfully installed fastapi uvicorn scikit-learn pandas requests
```

### Step 4: Run the API

```bash
# Start the FastAPI server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Expected output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Step 5: Access Your API

Open your browser and visit:

- **Health Check:** http://localhost:8000/health
- **Interactive Docs:** http://localhost:8000/docs
- **API Endpoint:** http://localhost:8000/predict

### Step 6: Test the API

**Option A: Using Swagger UI (Browser)**
1. Go to: http://localhost:8000/docs
2. Click on `/predict` endpoint
3. Click "Try it out"
4. Use the sample data or modify it
5. Click "Execute"

**Option B: Using cURL (Command Line)**
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "mean_radius": 14.2,
    "mean_texture": 20.1,
    "mean_perimeter": 92.3,
    "mean_area": 629.9,
    "mean_smoothness": 0.09,
    "mean_compactness": 0.10,
    "mean_concavity": 0.08,
    "mean_concave_points": 0.05,
    "mean_symmetry": 0.18,
    "mean_fractal_dimension": 0.06,
    "radius_error": 0.4,
    "texture_error": 1.2,
    "perimeter_error": 2.8,
    "area_error": 40.0,
    "smoothness_error": 0.007,
    "compactness_error": 0.02,
    "concavity_error": 0.03,
    "concave_points_error": 0.01,
    "symmetry_error": 0.02,
    "fractal_dimension_error": 0.003,
    "worst_radius": 16.0,
    "worst_texture": 25.0,
    "worst_perimeter": 105.0,
    "worst_area": 800.0,
    "worst_smoothness": 0.13,
    "worst_compactness": 0.25,
    "worst_concavity": 0.30,
    "worst_concave_points": 0.12,
    "worst_symmetry": 0.28,
    "worst_fractal_dimension": 0.08
  }'
```

**Option C: Using Python Client**
```bash
# Run the provided client script
python client.py
```

### Step 7: Stop the Server

Press `CTRL+C` in the terminal to stop the server.

### Step 8: Deactivate Virtual Environment (When Done)

```bash
deactivate
```

---

## 🐳 Method 2: Run with Docker (Recommended for Production-like Testing)

### Step 1: Install Docker Desktop

Download and install Docker Desktop:
- **Windows:** https://docs.docker.com/desktop/install/windows-install/
- **Mac:** https://docs.docker.com/desktop/install/mac-install/
- **Linux:** https://docs.docker.com/desktop/install/linux-install/

### Step 2: Clone the Repository

```bash
git clone https://github.com/DeepikaSidda/Honey-s-Project.git
cd Honey-s-Project
```

### Step 3: Build Docker Image

```bash
# Build the Docker image
docker build -t ml-fastapi-app .
```

**Expected output:**
```
Successfully built abc123def456
Successfully tagged ml-fastapi-app:latest
```

### Step 4: Run Docker Container

```bash
# Run the container
docker run -d --name ml-api -p 8000:8000 ml-fastapi-app

# Or run with auto-restart
docker run -d --name ml-api --restart unless-stopped -p 8000:8000 ml-fastapi-app
```

### Step 5: Check Container Status

```bash
# Check if container is running
docker ps

# View logs
docker logs ml-api

# Follow logs in real-time
docker logs -f ml-api
```

### Step 6: Access Your API

Same as Method 1:
- **Health Check:** http://localhost:8000/health
- **Interactive Docs:** http://localhost:8000/docs
- **API Endpoint:** http://localhost:8000/predict

### Step 7: Manage Docker Container

```bash
# Stop container
docker stop ml-api

# Start container
docker start ml-api

# Restart container
docker restart ml-api

# Remove container
docker rm ml-api

# Remove image
docker rmi ml-fastapi-app
```

---

## 🔧 Troubleshooting

### Issue 1: Port Already in Use

**Error:** `Address already in use`

**Solution:**
```bash
# Use a different port
uvicorn main:app --reload --host 0.0.0.0 --port 8080

# Or for Docker:
docker run -d --name ml-api -p 8080:8000 ml-fastapi-app
```

Then access at: http://localhost:8080

### Issue 2: Module Not Found

**Error:** `ModuleNotFoundError: No module named 'fastapi'`

**Solution:**
```bash
# Make sure virtual environment is activated
# Then reinstall dependencies
pip install -r requirements.txt
```

### Issue 3: Model File Not Found

**Error:** `Model file not found: model.pkl`

**Solution:**
```bash
# Make sure you're in the correct directory
cd Honey-s-Project

# Check if model files exist
ls -la model.pkl scaler.pkl

# On Windows:
dir model.pkl scaler.pkl
```

### Issue 4: Permission Denied (Windows)

**Error:** `cannot be loaded because running scripts is disabled`

**Solution:**
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue 5: Docker Not Running

**Error:** `Cannot connect to the Docker daemon`

**Solution:**
- Make sure Docker Desktop is running
- On Windows: Check system tray for Docker icon
- Restart Docker Desktop if needed

---

## 📊 Viewing Logs

### Python Method:
Logs appear directly in the terminal where you ran `uvicorn`.

### Docker Method:
```bash
# View all logs
docker logs ml-api

# View last 50 lines
docker logs --tail 50 ml-api

# Follow logs in real-time
docker logs -f ml-api

# View logs with timestamps
docker logs -t ml-api
```

---

## 🧪 Testing Your API

### Test Health Endpoint

**Browser:** http://localhost:8000/health

**cURL:**
```bash
curl http://localhost:8000/health
```

**Expected Response:**
```json
{"status":"API is running!"}
```

### Test Prediction Endpoint

**Using Swagger UI:**
1. Go to http://localhost:8000/docs
2. Expand `/predict` endpoint
3. Click "Try it out"
4. Click "Execute"

**Using cURL:**
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"mean_radius":14.2,"mean_texture":20.1,"mean_perimeter":92.3,"mean_area":629.9,"mean_smoothness":0.09,"mean_compactness":0.10,"mean_concavity":0.08,"mean_concave_points":0.05,"mean_symmetry":0.18,"mean_fractal_dimension":0.06,"radius_error":0.4,"texture_error":1.2,"perimeter_error":2.8,"area_error":40.0,"smoothness_error":0.007,"compactness_error":0.02,"concavity_error":0.03,"concave_points_error":0.01,"symmetry_error":0.02,"fractal_dimension_error":0.003,"worst_radius":16.0,"worst_texture":25.0,"worst_perimeter":105.0,"worst_area":800.0,"worst_smoothness":0.13,"worst_compactness":0.25,"worst_concavity":0.30,"worst_concave_points":0.12,"worst_symmetry":0.28,"worst_fractal_dimension":0.08}'
```

**Using Python:**
```python
import requests

response = requests.post(
    "http://localhost:8000/predict",
    json={
        "mean_radius": 14.2,
        "mean_texture": 20.1,
        # ... rest of features
    }
)

print(response.json())
```

---

## 🎯 Quick Reference

### Python Method
```bash
# Start
cd Honey-s-Project
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Stop
CTRL+C
deactivate
```

### Docker Method
```bash
# Start
docker build -t ml-fastapi-app .
docker run -d --name ml-api -p 8000:8000 ml-fastapi-app

# Stop
docker stop ml-api
docker rm ml-api
```

---

## 💡 Development Tips

1. **Use `--reload` flag** for auto-restart on code changes:
   ```bash
   uvicorn main:app --reload
   ```

2. **Check logs** to debug issues:
   ```bash
   # Python: logs appear in terminal
   # Docker: docker logs ml-api
   ```

3. **Test with Swagger UI** at http://localhost:8000/docs - it's the easiest way!

4. **Use virtual environment** to avoid dependency conflicts

5. **Keep Docker Desktop running** if using Docker method

---

## 📞 Need Help?

If you encounter issues:
1. Check the [Troubleshooting](#troubleshooting) section
2. View logs for error messages
3. Make sure all prerequisites are installed
4. Verify you're in the correct directory

---

**Your API is now running locally! 🎉**

Access it at: http://localhost:8000/docs
