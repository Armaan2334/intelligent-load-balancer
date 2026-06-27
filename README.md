# Intelligent Load Balancing System with Auto-Scaling and Real-Time Monitoring

## Overview
This project demonstrates a cloud-native application deployed on AWS using Docker, Kubernetes (k3s), Prometheus, Grafana, and Horizontal Pod Autoscaler (HPA).

## Technologies Used
- AWS EC2 (Ubuntu)
- Python Flask
- Docker
- Kubernetes (k3s)
- Prometheus
- Grafana
- Helm
- Locust

## Features
- Containerized Flask application
  ![Docker container](docs/p_docker_container.png)
- Kubernetes Deployment
  ![Kubernetes Deployment](docs/p_k8s_cluster.png)
- Auto Scaling using HPA
  ![Auto Scaling using HPA](docs/p_hpa_output.png)
- Real-Time Monitoring
  ![Real-Time Monitoring](docs/p_system_metrics_grafana.png)
- Load Testing with Locust
  ![Load Testing with Locust](docs/p_locust_load_testing.png)
- Self-Healing Pods

## Project Structure

```
intelligent-load-balancer/
├── app/
├── kubernetes/
├── monitoring/
├── nginx/
├── load-testing/
└── README.md
```

## Deployment

1. Build Docker Image
2. Deploy to Kubernetes
3. Expose Service
4. Configure HPA
5. Install Prometheus & Grafana
6. Perform Load Testing

## Author

Armaandeep Singh
B.Tech CSE
I.K. Gujral Punjab Technical University
