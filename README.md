This is a simple guestbook application to demonstrate
the deployment of a backend and frontend service in a kubernetes 
cluster.

Steps for setup:

Step 1:
build dockerfiles:

docker buildx build --platform linux/amd64 -t quirin1/k8s-frontend:0.0.1 --push ./frontend  

docker buildx build --platform linux/amd64 -t quirin1/k8s-backend:amd64 --push ./backend

Step 2:

push dockerfiles to docker hub

docker push  quirin1/k8s-backend:amd64

docker push  quirin1/k8s-frontend:0.0.1

Step 3:
launch a cluster with 3 nodes and download kubeconfig file from cluster service (civo)

Step 5:
export link to kubeconfig file as environment variable

export KUBECONFIG="$PWD/civo-k8s-test-kubeconfig"

Step 5:

apply 

kubectl apply -f guestbook-split.yaml

Step 6:
check if cluster services are running

 kubectl get nodes -o wide

 kubectl get svc -A

 kubectl get pods

 Step 7: 
 get public IP from cluster in civo and create a new A-record for your domain with the public IP

 Step 8: 
 open domain (in this case it was quiquak.de)