# 🚀 FastAPI Todo App on AWS EKS with CI/CD

This project is a complete DevOps workflow demonstrating how to:
- Build a Python FastAPI app
- Containerize with Docker
- Automate CI/CD with GitHub Actions
- Deploy to AWS EKS (Kubernetes)
- Access via public LoadBalancer URL

---

## 🔧 Tech Stack

- 🐍 Python + FastAPI (CRUD API)
- 🐳 Docker
- ⚙️ GitHub Actions (CI/CD)
- ☸️ Kubernetes (EKS)
- ☁️ AWS (EKS, LoadBalancer, IAM)
- 📄 Swagger (OpenAPI Docs)

---

## 📁 Project Structure

```
.
├── app/
│   └── main.py              # FastAPI app
├── Dockerfile               # Container build
├── .github/workflows/
│   └── docker-publish.yml   # GitHub Actions pipeline
└── k8s/
    ├── configmap.yaml       # ConfigMap 
    ├── deployment.yaml      # K8s Deployment
    ├── service.yml          # K8s Service 
```

---

## 🚀 Public URL

After deployment, app is live at:

```
http://<AWS-LoadBalancer-URL>/docs
```

or

```
http://<your-domain.com>/docs
```

---

## 🛠️ Setup & Deployment Instructions

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/MukulB0412/todo-aws-devops.git
cd todo-aws-devops
```

### 2️⃣ Create Docker Image Locally (Optional)

```bash
docker build -t mukul0412/todo-aws-devops:latest .
docker push mukul0412/todo-aws-devops:latest
```

### 3️⃣ GitHub Actions Setup

On push to `main`, Docker image is built & pushed to Docker Hub using:

`.github/workflows/docker-publish.yml`

### 4️⃣ Kubernetes Deployment (AWS EKS)

Apply your manifests:

```bash
kubectl apply -f k8s/configmap.yaml  
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yml
```

### 5️⃣ Get LoadBalancer URL

```bash
kubectl get svc todo-service
```

Copy the `EXTERNAL-IP` and visit in browser.

---

## ✅ Sample API Endpoints

| Method | Path              | Description        |
|--------|-------------------|--------------------|
| GET    | `/todos`          | List all todos     |
| POST   | `/todo`           | Add a new todo     |
| DELETE | `/todo/{{index}}` | Delete todo by id  |
| GET    | `/docs`           | Swagger UI         |
| GET    | `/`               | Root test route    |

---

## 📄 Author

Mukul Bhardwaj  
GitHub: [mukul0412](https://github.com/mukul0412)  

---

## 🏁 Final Result

- ✅ Live on AWS EKS
- ✅ Docker + GitHub Actions CI/CD
- ✅ Public URL accessible
- ✅ Clean REST API with Swagger UI
