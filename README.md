# Multi-Orchestrator-Application-Deployment

This project demonstrates deploying a containerized web application on **Amazon EKS**, pulling images from **Amazon ECR**, exposing the app using an **AWS LoadBalancer**, and enabling **autoscaling**.

---

## 🏗 Architecture

- Amazon ECR – stores Docker images
- Amazon EKS – Kubernetes cluster
- Managed Node Group / Auto Mode
- Kubernetes Deployment & Service
- Horizontal Pod Autoscaler (HPA)
- AWS Load Balancer (HTTP)

---

## 🚀 Deployment Steps

### 1. Push Image to ECR
```bash
docker build -t multi-platform-app .
docker tag multi-platform-app:latest \
793491548829.dkr.ecr.us-east-1.amazonaws.com/multi-platform-app:latest
docker push 793491548829.dkr.ecr.us-east-1.amazonaws.com/multi-platform-app:latest
2. Configure EKS Access
bash
Copy code
aws eks update-kubeconfig --region us-east-1 --name eks-demo-cluster
3. Deploy Application
bash
Copy code
kubectl apply -f eks-deployment.yaml
4. Enable Autoscaling
bash
Copy code
kubectl apply -f autoscaling/hpa.yaml
5. Access Application
bash
Copy code
kubectl get svc web-service
Open in browser:

pgsql
Copy code
http://<load-balancer-dns-name>
📈 Autoscaling
Min pods: 2

Max pods: 10

CPU target: 50%

Node autoscaling enabled via managed node group

🔐 IAM Requirements
Node role must include:

AmazonEKSWorkerNodePolicy

AmazonEKS_CNI_Policy

AmazonEC2ContainerRegistryReadOnly

Trust policy must allow:

sts:AssumeRole

sts:TagSession

✅ Status
ECR image pull: ✅

LoadBalancer created: ✅

Autoscaling enabled: ✅
