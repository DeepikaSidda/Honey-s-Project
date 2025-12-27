# 🚀 Quick Start - Deploy to AWS EC2

## ✅ EC2 Instance Ready!

- **Public IP:** `98.88.251.211`
- **Instance ID:** `i-0378940ba8efb9f6a`

---

## 📋 3-Step Deployment

### 1️⃣ Push to GitHub

```bash
cd ML-Model-Serving-with-FastAPI-and-Docker-main
git init
git add .
git commit -m "ML Model API"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 2️⃣ Connect to EC2

1. Go to: https://console.aws.amazon.com/ec2/
2. Select instance: `ml-model-api`
3. Click "Connect" → "EC2 Instance Connect" → "Connect"

### 3️⃣ Deploy

```bash
# Install Docker & Git
sudo apt-get update -y && sudo apt-get install -y docker.io git
sudo systemctl start docker && sudo usermod -aG docker ubuntu
exit

# Reconnect, then:
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
docker build -t ml-fastapi-app .
docker run -d --name ml-api --restart unless-stopped -p 8000:8000 ml-fastapi-app
docker logs ml-api
```

---

## 🔗 Your API

- **Health:** http://98.88.251.211:8000/health
- **Docs:** http://98.88.251.211:8000/docs
- **API:** http://98.88.251.211:8000/predict

---

**See EASY-DEPLOYMENT-STEPS.md for detailed instructions!**
