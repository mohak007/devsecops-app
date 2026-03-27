# DevSecOps CI/CD Pipeline with Dashboard

An end-to-end DevSecOps project that demonstrates how to build, secure, and visualize a CI/CD pipeline using modern tools and best practices.

---

## Overview

This project implements a complete CI/CD pipeline with integrated security scanning and a custom-built dashboard to monitor pipeline status, security results, and application health.

---

## Features

- Automated CI pipeline using GitHub Actions  
- Dockerized Python (Flask) application  
- Dependency vulnerability scanning using `pip-audit`  
- Container image scanning using `Trivy`  
- Custom UI dashboard for pipeline visualization  
- Production-ready multi-stage Docker build  

---

## Architecture
Developer Push → GitHub Actions CI Pipeline → Dependency Scan (pip-audit) → Docker Build → Image Scan (Trivy) → Dashboard Visualization

---

## Tech Stack

- **Backend:** Python, Flask  
- **CI/CD:** GitHub Actions  
- **Containerization:** Docker  
- **Security:** Trivy, pip-audit  
- **Frontend:** HTML, CSS  

---

## DevSecOps Workflow

1. Code is pushed to `main` branch  
2. GitHub Actions pipeline is triggered  
3. Dependencies are scanned for vulnerabilities  
4. Docker image is built  
5. Trivy scans the image for security issues  
6. Pipeline fails if critical vulnerabilities are found  
7. Dashboard displays pipeline and security status  

---

##  Dashboard Preview

The dashboard provides:

- Pipeline Status  
- Last Build Time  
- Security Scan Results  
- Application Health  

---

## Run Locally

### 1. Clone the repository


git clone https://github.com/mohak007/devsecops-app.git
cd devsecops-app

### 2. Build Docker image
docker build -t devsecops-app .

### 3.Run the container
docker run -p 5000:5000 devsecops-app

### 4. Open in browser
http://localhost:5000

###5. CI Pipeline (GitHub Actions)
The pipeline includes:
  - Code checkout
  - Dependency installation
  - Security scanning (pip-audit)
  - Docker build
  - Container scanning (Trivy)


Key Learnings
  Handling Docker image tagging issues in CI pipelines
  Integrating security scanning into CI/CD workflows
  Building a DevSecOps-first pipeline
  Visualizing pipeline health through a UI dashboard
Future Improvements
  Integrate GitHub API for real-time pipeline status
  Add charts (Grafana-style visualization)
  Deploy on AWS (EC2 / ECS)
  Add alerts for failed builds or vulnerabilities

Contributing
Feel free to fork this repo and improve it. Contributions are welcome!  
