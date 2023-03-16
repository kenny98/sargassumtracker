HOW TO RUN CODE
minikube start
minikube image build -t python-docker -f ./dockerfile .
kubectl run python-docker --image=python-docker --image-pull-policy=Never --restart=Never --expose=true
kubectl expose pod python-docker --port=5000 --name=python-docker
minikube service python-docker --url
