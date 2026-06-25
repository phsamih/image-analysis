# Deploy to server

## 1) Clone repo
```bash
git clone https://github.com/phsamih/sz-satellite-image-analysis.git
cd sz-satellite-image-analysis
```

## 2) Add these files to the repo
Copy the deploy-ready files from this package into your repo.

## 3) Rename env
```bash
cp .env.example .env
```

## 4) Run with Docker
```bash
docker compose up -d --build
```

## 5) Open
- http://YOUR_SERVER_IP
