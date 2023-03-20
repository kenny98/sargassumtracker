# How to run Docker & Kubernetes

```
<!-- Start Minikube -->
minikube start

<!-- Build Docker Container -->
minikube image build -t python-docker -f ./dockerfile .

<!-- Run Container Pod in Kubernetes -->
kubectl run python-docker --image=python-docker --image-pull-policy=Never --restart=Never --expose=true

<!-- Expose the Pod to be accessed from outside -->
kubectl expose pod python-docker --port=5000 --name=python-docker

<!-- Get Access URL for Pod -->
minikube service python-docker --url
```

# Run Local Server without containerized environment

```
<!-- Run Server -->
python app.py
```