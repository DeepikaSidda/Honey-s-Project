# 🤖 ML Model Serving with FastAPI and Docker

> Production-ready machine learning model deployment with comprehensive error handling, logging, and health monitoring.

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Live Demo:** http://98.88.251.211:8000/docs

---



## 🎯 Overview

This project demonstrates a **production-ready** machine learning model deployment using FastAPI and Docker. It serves a pre-trained scikit-learn classification model through a REST API with enterprise-grade features including:

- Comprehensive error handling
- Structured logging with timestamps
- Docker health checks for container orchestration
- Interactive API documentation (Swagger UI)
- Graceful failure handling
- Auto-restart on failures

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




### Access the API

- **Health Check:** http://localhost:8000/health
- **Interactive Docs:** http://localhost:8000/docs
- **API Endpoint:** http://localhost:8000/predict
---

# 💻 Local Deployment Guide

Run the ML Model API on your local machine for development and testing.

---

## 📋 Prerequisites

Before you start, make sure you have:

- **Python 3.11+** installed ([Download Python](https://www.python.org/downloads/))
- **Docker Desktop** (optional, for containerized deployment) ([Download Docker](https://www.docker.com/products/docker-desktop/))
- **Git** (to clone the repository) ([Download Git](https://git-scm.com/downloads))

---

## 🚀 Local Deployment

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


**Windows (Command Prompt):**
```cmd
# Create virtual environment
python -m venv venv
# Activate virtual environment
venv\Scripts\activate.bat
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
