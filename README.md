# 🤖 ML Model Serving with FastAPI and Docker

> Production-ready machine learning model deployment with comprehensive error handling, logging, and health monitoring.

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Live Demo:** http://98.88.251.211:8000/docs

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Monitoring & Logging](#monitoring--logging)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

This project demonstrates a **production-ready** machine learning model deployment using FastAPI and Docker. It serves a pre-trained scikit-learn classification model through a REST API with enterprise-grade features including:

- ✅ Comprehensive error handling
- ✅ Structured logging with timestamps
- ✅ Docker health checks for container orchestration
- ✅ Interactive API documentation (Swagger UI)
- ✅ Graceful failure handling
- ✅ Auto-restart on failures

The system loads a pre-trained scikit-learn classification model and scaler from pickle files, exposes REST endpoints for predictions and health checks, and runs in a Docker container with proper health monitoring.

---

## ✨ Features

### 🚀 Core Features

- **Pre-trained Model Serving**: Loads and serves scikit-learn classification models
- **RESTful API**: FastAPI-based REST endpoints for predictions
- **Input Validation**: Automatic validation using Pydantic models
- **Interactive Documentation**: Auto-generated Swagger UI at `/docs`
- **Health Monitoring**: Built-in health check endpoint for orchestration tools

### 🛡️ Production-Ready Features

- **Error Handling**: Comprehensive try-catch blocks with descriptive error messages
- **Structured Logging**: Timestamped logs for debugging and monitoring
- **Docker Health Checks**: Automatic container health monitoring
- **Auto-Restart**: Container automatically restarts on failures
- **Graceful Degradation**: Fails fast with clear error messages if models are missing

### 📊 Monitoring & Observability

- **Request Logging**: Every prediction request is logged with metadata
- **Error Tracking**: All errors logged at ERROR level with full stack traces
- **Model Metadata**: Logs model type and loading status on startup
- **Container Health**: Docker HEALTHCHECK runs every 30 seconds

---

## 🏗️ Architecture

The application follows a clean three-layer architecture:

```
┌─────────────────────────────────────────┐
│         Client Applications             │
│    (Browser, cURL, Python, etc.)        │
└──────────────┬──────────────────────────┘
               │ HTTP/JSON
               ▼
┌─────────────────────────────────────────┐
│         FastAPI Application             │
│  ┌─────────────────────────────────┐   │
│  │  /health endpoint               │   │
│  │  /predict endpoint              │   │
│  │  /docs (Swagger UI)             │   │
│  └─────────────────────────────────┘   │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│      Model Service Layer                │
│  ┌─────────────────────────────────┐   │
│  │  Model Loader                   │   │
│  │  Prediction Handler             │   │
│  │  Error Handler                  │   │
│  │  Logger                         │   │
│  └─────────────────────────────────┘   │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│      Pickle Files (Disk)                │
│  - model.pkl (Trained Model)            │
│  - scaler.pkl (Data Scaler)             │
└─────────────────────────────────────────┘
```

### Layer Responsibilities

1. **API Layer (FastAPI)**
   - HTTP request/response handling
   - Input validation using Pydantic
   - Response formatting
   - Auto-generated documentation

2. **Service Layer**
   - Model loading with error handling
   - Prediction logic
   - Data transformation (scaling)
   - Logging and monitoring

3. **Infrastructure Layer**
   - Docker containerization
   - Health check monitoring
   - Auto-restart on failures
   - Log aggregation

---

## 🚀 Quick Start

### Prerequisites

- Docker installed ([Get Docker](https://www.docker.com/get-started))
- Python 3.11+ (for local development)
- Git

### Option 1: Using Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/DeepikaSidda/Honey-s-Project.git
cd Honey-s-Project

# Build the Docker image
docker build -t ml-fastapi-app .

# Run the container
docker run -d --name ml-api --restart unless-stopped -p 8000:8000 ml-fastapi-app

# Check if running
docker ps

# View logs
docker logs ml-api
```

### Option 2: Local Development

```bash
# Clone the repository
git clone https://github.com/DeepikaSidda/Honey-s-Project.git
cd Honey-s-Project

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Access the API

- **Health Check:** http://localhost:8000/health
- **Interactive Docs:** http://localhost:8000/docs
- **API Endpoint:** http://localhost:8000/predict

---

## 📚 API Documentation

### Endpoints

#### 1. Health Check

**GET** `/health`

Check if the API is running and healthy.

**Response:**
```json
{
  "status": "API is running!"
}
```

#### 2. Make Prediction

**POST** `/predict`

Make a prediction using the trained model.

**Request Body:**
```json
{
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
}
```

**Response:**
```json
{
  "prediction": 1
}
```

**Status Codes:**
- `200 OK`: Prediction successful
- `422 Unprocessable Entity`: Invalid input data
- `500 Internal Server Error`: Prediction failed

### Interactive Documentation

Visit http://localhost:8000/docs for interactive Swagger UI where you can:
- View all endpoints
- Test API calls directly from browser
- See request/response schemas
- Download OpenAPI specification

---

## 🌐 Deployment

### AWS EC2 Deployment

**Live Instance:** http://98.88.251.211:8000

#### Deploy to Your Own EC2

1. **Launch EC2 Instance**
   - AMI: Ubuntu 22.04 LTS
   - Instance Type: t2.micro (free tier) or t2.small
   - Security Group: Allow port 8000 from 0.0.0.0/0

2. **Connect and Deploy**
   ```bash
   # SSH into your instance
   ssh -i your-key.pem ubuntu@YOUR_IP
   
   # Install Docker
   sudo apt-get update -y
   sudo apt-get install -y docker.io git
   sudo systemctl start docker
   sudo usermod -aG docker ubuntu
   
   # Clone and deploy
   git clone https://github.com/DeepikaSidda/Honey-s-Project.git
   cd Honey-s-Project
   docker build -t ml-fastapi-app .
   docker run -d --name ml-api --restart unless-stopped -p 8000:8000 ml-fastapi-app
   ```

3. **Access Your API**
   - Health: http://YOUR_IP:8000/health
   - Docs: http://YOUR_IP:8000/docs

---

## 📊 Monitoring & Logging

### Log Format

All logs follow this structured format:
```
YYYY-MM-DD HH:MM:SS - module_name - LEVEL - message
```

### Log Levels

- **INFO**: Normal operations (model loading, predictions)
- **ERROR**: Errors with full stack traces
- **WARNING**: Non-critical issues

### Example Logs

```
2024-12-27 10:30:15 - __main__ - INFO - Loading model from model.pkl...
2024-12-27 10:30:15 - __main__ - INFO - Model loaded successfully. Type: LogisticRegression
2024-12-27 10:30:15 - __main__ - INFO - Loading scaler from scaler.pkl...
2024-12-27 10:30:15 - __main__ - INFO - Scaler loaded successfully. Type: StandardScaler
2024-12-27 10:30:20 - __main__ - INFO - Received prediction request with 30 features
2024-12-27 10:30:20 - __main__ - INFO - Prediction completed successfully. Result: 1
```

### View Logs

```bash
# View all logs
docker logs ml-api

# Follow logs in real-time
docker logs -f ml-api

# View last 100 lines
docker logs --tail 100 ml-api
```

### Docker Health Check

The container includes automatic health monitoring:

- **Interval:** 30 seconds
- **Timeout:** 10 seconds
- **Start Period:** 5 seconds
- **Retries:** 3

```bash
# Check container health
docker ps

# View detailed health status
docker inspect ml-api | grep -A 10 Health
```

---

## 🛠️ Troubleshooting

### Common Issues

#### 1. Model File Not Found

**Error:** `Model file not found: model.pkl`

**Solution:**
```bash
# Ensure model files are in the correct location
ls -la model.pkl scaler.pkl
```

#### 2. Container Unhealthy

**Error:** Container shows as "unhealthy"

**Solution:**
```bash
# Check logs for errors
docker logs ml-api

# Restart container
docker restart ml-api
```

#### 3. Prediction Errors

**Error:** `500 Internal Server Error`

**Solution:**
```bash
# View detailed error logs
docker logs ml-api

# Check if model loaded correctly
docker logs ml-api | grep "Model loaded"
```

#### 4. Port Already in Use

**Error:** `Address already in use`

**Solution:**
```bash
# Use a different port
docker run -d --name ml-api -p 8080:8000 ml-fastapi-app

# Or stop the conflicting service
docker stop ml-api
```

### Useful Commands

```bash
# Restart API
docker restart ml-api

# Stop API
docker stop ml-api

# Remove container
docker rm ml-api

# Rebuild and redeploy
docker stop ml-api && docker rm ml-api
docker build -t ml-fastapi-app .
docker run -d --name ml-api --restart unless-stopped -p 8000:8000 ml-fastapi-app

# Update from GitHub
cd Honey-s-Project
git pull
docker stop ml-api && docker rm ml-api
docker build -t ml-fastapi-app .
docker run -d --name ml-api --restart unless-stopped -p 8000:8000 ml-fastapi-app
```

---

## 📁 Project Structure

```
Honey-s-Project/
├── main.py                 # FastAPI application
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
├── model.pkl             # Trained ML model
├── scaler.pkl            # Data scaler
├── client.py             # Sample client script
├── README.md             # This file
├── DEPLOY-NOW.md         # Deployment guide
└── .gitignore            # Git ignore rules
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👥 Authors

- **Deepika Sidda** - [GitHub](https://github.com/DeepikaSidda)

---

## 🙏 Acknowledgments

- FastAPI for the amazing web framework
- scikit-learn for machine learning tools
- Docker for containerization
- AWS for cloud hosting

---

## 📞 Support

For issues, questions, or contributions, please:
- Open an issue on GitHub
- Check the [Troubleshooting](#troubleshooting) section
- Review the [API Documentation](#api-documentation)

---

**⭐ If you find this project useful, please consider giving it a star!**
