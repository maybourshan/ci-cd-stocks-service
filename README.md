# CI/CD Stocks Microservices System

## 📌 Overview
This project implements a distributed financial system composed of multiple microservices, integrated with a full CI/CD pipeline using GitHub Actions.

The system includes:
- A Stocks Service for managing stock data
- A Capital Gains Service that communicates with the Stocks Service
- A MongoDB database for persistent storage

The project demonstrates how to build, test, and run a multi-service application using modern DevOps practices.

---

## 🧩 Architecture
The system consists of three services:
- **Stocks Service** – handles stock operations and data storage
- **Capital Gains Service** – calculates portfolio and gains using the stocks service
- **MongoDB** – stores stock data

The services are containerized and orchestrated using Docker Compose.

---

## 🚀 CI/CD Pipeline
The CI/CD pipeline is implemented using GitHub Actions and includes three stages:

1. **Build Stage**
   - Builds Docker images for all services

2. **Test Stage**
   - Runs the system using Docker Compose
   - Executes automated tests using `pytest`

3. **Query Stage**
   - Sends HTTP requests to the running system
   - Collects and stores responses in output files

---

## 🛠️ Technologies
- Python
- Docker & Docker Compose
- GitHub Actions
- MongoDB
- REST APIs
- pytest

---

## 📈 Key Features
- Multi-service architecture (microservices)
- Automated CI/CD pipeline
- Containerized deployment
- End-to-end testing with pytest
- Automated query execution and result logging

---

## 👩‍💻 Author
May Bourshan
