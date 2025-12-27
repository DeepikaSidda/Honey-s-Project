# 💻 Run ML Model API Locally (Python Method)

The easiest way to run the ML Model API on your local laptop.

---

## ⚡ Quick Start (2 Minutes)

### Step 1: Open PowerShell in Your Project Folder

**Option A: Using File Explorer**
1. Open File Explorer
2. Navigate to: `C:\Users\sidda\Downloads\ML-Model-Serving-with-FastAPI-and-Docker-main\ML-Model-Serving-with-FastAPI-and-Docker-main`
3. Click on the address bar and type: `powershell`
4. Press Enter

**Option B: Using PowerShell**
```powershell
cd C:\Users\sidda\Downloads\ML-Model-Serving-with-FastAPI-and-Docker-main\ML-Model-Serving-with-FastAPI-and-Docker-main
```

---

### Step 2: Install Required Packages

Copy and paste this command:

```powershell
pip install fastapi uvicorn scikit-learn pandas requests
```

**Expected output:**
```
Successfully installed fastapi uvicorn scikit-learn pandas requests
```

**Note:** If you see "Requirement already satisfied" - that's perfect! It means the packages are already installed.

---

### Step 3: Start the API Server

Copy and paste this command:

```powershell
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Expected output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Application startup complete.
```

**✅ Your API is now running!**

---

### Step 4: Open Your Browser

Click on any of these links:

- **Interactive API Docs:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/health
- **API Endpoint:** http://localhost:8000/predict

---

## 🧪 Test Your API

### Method 1: Using Swagger UI (Easiest)

1. Open: http://localhost:8000/docs
2. Click on **POST /predict**
3. Click **"Try it out"**
4. You'll see sample data pre-filled
5. Click **"Execute"**
6. See the prediction result!

### Method 2: Using the Client Script

Open a **new PowerShell window** (keep the server running in the first one):

```powershell
cd C:\Users\sidda\Downloads\ML-Model-Serving-with-FastAPI-and-Docker-main\ML-Model-Serving-with-FastAPI-and-Docker-main
python client.py
```

**Expected output:**
```
Status Code: 200
Raw Response: {"prediction":1}
```

### Method 3: Using cURL

```powershell
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{\"mean_radius\":14.2,\"mean_texture\":20.1,\"mean_perimeter\":92.3,\"mean_area\":629.9,\"mean_smoothness\":0.09,\"mean_compactness\":0.10,\"mean_concavity\":0.08,\"mean_concave_points\":0.05,\"mean_symmetry\":0.18,\"mean_fractal_dimension\":0.06,\"radius_error\":0.4,\"texture_error\":1.2,\"perimeter_error\":2.8,\"area_error\":40.0,\"smoothness_error\":0.007,\"compactness_error\":0.02,\"concavity_error\":0.03,\"concave_points_error\":0.01,\"symmetry_error\":0.02,\"fractal_dimension_error\":0.003,\"worst_radius\":16.0,\"worst_texture\":25.0,\"worst_perimeter\":105.0,\"worst_area\":800.0,\"worst_smoothness\":0.13,\"worst_compactness\":0.25,\"worst_concavity\":0.30,\"worst_concave_points\":0.12,\"worst_symmetry\":0.28,\"worst_fractal_dimension\":0.08}'
```

---

## 🛑 Stop the Server

When you're done testing:

1. Go back to the PowerShell window where the server is running
2. Press **CTRL+C**
3. The server will stop

---

## 🔧 Troubleshooting

### Issue 1: "Port 8000 is already in use"

**Solution:** Use a different port:
```powershell
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

Then access at: http://localhost:8080/docs

### Issue 2: "uvicorn: command not found"

**Solution:** Make sure Python is installed and in your PATH:
```powershell
python --version
pip --version
```

If Python is installed, try:
```powershell
python -m pip install uvicorn
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Issue 3: "ModuleNotFoundError: No module named 'fastapi'"

**Solution:** Install the dependencies again:
```powershell
pip install fastapi uvicorn scikit-learn pandas requests
```

### Issue 4: "Model file not found"

**Solution:** Make sure you're in the correct directory:
```powershell
# Check if model files exist
dir model.pkl
dir scaler.pkl

# If they don't exist, you're in the wrong folder
# Navigate to the correct folder
cd C:\Users\sidda\Downloads\ML-Model-Serving-with-FastAPI-and-Docker-main\ML-Model-Serving-with-FastAPI-and-Docker-main
```

---

## 📊 What You'll See

### In PowerShell (Server Logs):
```
2024-12-27 10:30:15 - __main__ - INFO - Loading model from model.pkl...
2024-12-27 10:30:15 - __main__ - INFO - Model loaded successfully. Type: LogisticRegression
2024-12-27 10:30:15 - __main__ - INFO - Loading scaler from scaler.pkl...
2024-12-27 10:30:15 - __main__ - INFO - Scaler loaded successfully. Type: StandardScaler
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### In Browser (Swagger UI):
- Interactive API documentation
- "Try it out" buttons to test endpoints
- Request/response examples
- Schema definitions

---

## 💡 Pro Tips

1. **Keep the PowerShell window open** while testing - you'll see logs of all requests

2. **Use Swagger UI** (http://localhost:8000/docs) - it's the easiest way to test

3. **Watch the logs** in PowerShell to see what's happening:
   - Model loading
   - Prediction requests
   - Any errors

4. **Test with different data** in Swagger UI by modifying the values

5. **The `--reload` flag** means the server will automatically restart when you change the code

---

## 🎯 Quick Reference

### Start Server:
```powershell
cd C:\Users\sidda\Downloads\ML-Model-Serving-with-FastAPI-and-Docker-main\ML-Model-Serving-with-FastAPI-and-Docker-main
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Access API:
- **Docs:** http://localhost:8000/docs
- **Health:** http://localhost:8000/health

### Stop Server:
- Press **CTRL+C** in PowerShell

---

## ✅ Success Checklist

- [ ] PowerShell opened in project folder
- [ ] Dependencies installed (`pip install ...`)
- [ ] Server started (`uvicorn main:app ...`)
- [ ] Browser opened to http://localhost:8000/docs
- [ ] Tested `/predict` endpoint
- [ ] Saw prediction result

---

**🎉 Congratulations! Your ML Model API is running locally!**

You can now:
- Test predictions with different data
- Share http://localhost:8000/docs with others on your network
- Develop and modify the code (it will auto-reload)
- Use it for demos and presentations

---

**Need help?** Check the [Troubleshooting](#troubleshooting) section above.
