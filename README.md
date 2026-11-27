KUBERNETES PRODUCTION TEST SERVER
=================================

A simple Production Test Server application demonstrating the deployment of a decoupled frontend and backend service in a Kubernetes cluster.


SETUP STEPS
-----------

Step 1: Build Dockerfiles
Build linux/amd64 container images for both the frontend and backend services:

docker buildx build --platform linux/amd64 -t quirin1/k8s-frontend:0.0.1 --push ./frontend
docker buildx build --platform linux/amd64 -t quirin1/k8s-backend:amd64 --push ./backend


Step 2: Push Docker Images to Docker Hub
Push the built images to your Docker Hub repository:

docker push quirin1/k8s-backend:amd64
docker push quirin1/k8s-frontend:0.0.1


Step 3: Launch the Kubernetes Cluster
1. Launch a Kubernetes cluster with 3 nodes in your cluster service (Civo).
2. Download the kubeconfig file from Civo to your local project folder.


Step 4: Export KUBECONFIG
Set the path to your downloaded kubeconfig file as an environment variable:

export KUBECONFIG="$PWD/civo-k8s-test-kubeconfig"


Step 5: Deploy (or Redeploy) the Application
Apply the Kubernetes manifest to deploy the services:

kubectl apply -f guestbook-split.yaml

For redeployment after updating images:

kubectl rollout restart deployments -n default


Step 6: Check If Cluster Services Are Running
Verify that your nodes, services, and pods are active and healthy:

kubectl get nodes -o wide
kubectl get svc -A
kubectl get pods


Step 7: Configure Domain DNS
1. Get the Public IP from your cluster in Civo.
2. Create a new A-record for your domain pointing to that Public IP.


Step 8: Open the Application
Open your domain in a browser to verify the live deployment (e.g., http://quiquak.de or https://quiquak.de).