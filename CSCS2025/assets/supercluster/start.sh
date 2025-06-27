#!/bin/sh

docker build -t kube-ssh -f ssh/Dockerfile.ssh ssh
minikube start --driver=docker --kubernetes-version=v1.31.5
minikube image load busybox:1.37.0-uclibc
minikube image load kube-ssh

kubectl create -f deploy/minikube-0-namespace.yaml -f deploy/minikube-1-permissions.yaml -f  deploy/minikube-1-ssh.yaml
kubectl create configmap -n flag supercluster-html --from-file deploy/web
kubectl create secret generic -n flag flag --from-file deploy/flag
kubectl create -f deploy/minikube-2-challenge.yaml
