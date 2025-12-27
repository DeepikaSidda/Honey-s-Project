# 🚀 Deploy ML Model API to AWS EC2 via GitHub

## ✅ Your EC2 Instance is Running!

- **Instance ID:** `i-0378940ba8efb9f6a`
- **Public IP:** `98.88.251.211`
- **Region:** `us-east-1`

---

## 📋 Step-by-Step Deployment (5 Minutes)

### Step 1: Push Your Code to GitHub

### Step 1: Push Your Code to GitHub

**On your local computer (in PowerShell or Git Bash):**

```bash
cd ML-Model-Serving-with-FastAPI-and-Docker-main

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "ML Model API with FastAPI and Docker"

# Create a new repository on GitHub, then:
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

**Note:** Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and repository name.

---

### Step 2: Connect to EC2 via AWS Console Browser SSH

1. **Go to AWS EC2 Console:**
   - Open: https://console.aws.amazon.com/ec2/

2. **Find Your Instance:**
   - Click "Instances" in the left menu
   - Find instance: `ml-model-api` (ID: `i-0378940ba8efb9f6a`)
   - Check the box next to it

3. **Connect:**
   - Click "Connect" button (top right)
   - Choose "EC2 Instance Connect" tab
   - Click "Connect" button
   - A browser terminal will open!

---

### Step 3: Deploy on EC2

**Copy and paste these commands into the EC2 browser terminal:**

```bash
# Install Docker and Git
sudo apt-get update -y
sudo apt-get install -y docker.io git
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu

# Log out and back in for docker group to take effect
exit
```

**Reconnect to EC2 (repeat Step 2), then:**

```bash
# Clone your GitHub repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# Build Docker image
docker build -t ml-fastapi-app .

# Run container
docker run -d --name ml-api --restart unless-stopped -p 8000:8000 ml-fastapi-app

# Check if running
docker ps

# View logs
docker logs ml-api
```

**Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual values!**

---

### Step 4: Test Your API

Your API is now live! Open these URLs in your browser:

- **Health Check:** http://98.88.251.211:8000/health
- **Interactive Docs:** http://98.88.251.211:8000/docs
- **API Endpoint:** http://98.88.251.211:8000/predict

---

## 🧪 Test with cURL

```bash
# Health check
curl http://98.88.251.211:8000/health

# Make a prediction
curl -X POST http://98.88.251.211:8000/predict \
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

---

## 🛠️ Useful Commands

```bash
# View logs
docker logs ml-api

# View real-time logs
docker logs -f ml-api

# Restart API
docker restart ml-api

# Stop API
docker stop ml-api

# Start API
docker start ml-api

# Update code and redeploy
cd YOUR_REPO_NAME
git pull
docker stop ml-api
docker rm ml-api
docker build -t ml-fastapi-app .
docker run -d --name ml-api --restart unless-stopped -p 8000:8000 ml-fastapi-app
```

---

## 🎉 You're Done!

Your ML Model API is now deployed and accessible at:
- **http://98.88.251.211:8000**

Share this link with anyone who needs to use your API!

---

## 💡 Tips

1. **Make your repo public** on GitHub so you don't need authentication to clone
2. **Or use SSH keys** if you want to keep it private
3. **Bookmark the Swagger docs** at http://98.88.251.211:8000/docs for easy testing
4. **Monitor logs** regularly with `docker logs ml-api`

---

## ❓ Troubleshooting

**Container not running?**
```bash
docker ps -a  # See all containers
docker logs ml-api  # Check error logs
```

**Port already in use?**
```bash
docker stop ml-api
docker rm ml-api
# Then run again
```

**Need to update code?**
```bash
cd YOUR_REPO_NAME
git pull
docker stop ml-api && docker rm ml-api
docker build -t ml-fastapi-app .
docker run -d --name ml-api --restart unless-stopped -p 8000:8000 ml-fastapi-app
```

---

**Need help? Let me know which step you're on!**
