# Docker and Kubernetes to run code in Containerized Environment

<!-- Start Minikube -->
### Start Minikube
```
minikube start
```

<!-- Build Docker Container -->
### Build Docker Container
```
minikube image build -t python-docker -f ./dockerfile .
```

<!-- Run Container Pod in Kubernetes -->
### Run Container Pod in Kubernetes
```
kubectl run python-docker --image=python-docker --image-pull-policy=Never --restart=Never --expose=true
```

<!-- Expose the Pod to be accessed from outside of Pod -->
### Expose the Pod to be accessed from outside of Pod
```
kubectl expose pod python-docker --port=5000 --name=python-docker
```

<!-- Get Access URL for Pod -->
### Get Access URL for Pod
```
minikube service python-docker --url
```

# Run Local Server without Containerized Environment

<!-- Run Server -->
### Run Server
```
python app.py
```