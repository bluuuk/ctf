# Supercluster

### Prerequisites
To run the challenge locally install
* Docker
* Minikube
* kubectl

### Setup Steps
1. Start the challenge environment: `./start.sh`
2. Forward the SSH port: `kubectl port-forward -n entrypoint service/entrypoint 2022:`
3. Establish SSH Connection: `ssh -p 2022 -L 127.0.0.1:8080:supercluster.flag:80 ctf@localhost`
    Here you have the same environment as on the remote instance.

Note: Minikube sets up a kubeconfig which allows `kubectl` locally to work with cluster admin permissions.
