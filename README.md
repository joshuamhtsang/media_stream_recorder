# media_stream_recorder
Python scripts to record media streams.

# Deploying to Google Kubernetes Engine

1. Create a cluster in Google Kubernetes Engine: 
By default, a single node pool will be created, and Ubuntu 
nodes are recommended.  You can check the cluster is created
by using a Cloud Shell (see below) and typing:
```
kubectl get nodes
```

2. Add Dockerhub credentials to the cluster:
- Do this using the Google 'Cloud Shell' by clicking 'Connect' on the
GKE interface.
- Execute the auto-generate gcloud 'get-credentials' command.
- Create the secret using `kubectl` CLI:
```
kubectl create secret docker-registry joshua-dockerhub --docker-server=https://hub.docker.com/ --docker-username=<DOCKERHUB_USERNAME> --docker-password='<DOCKERHUB_PASSWORD>' --docker-email=<DOCKERHUB_EMAIL>
```
You can list the created secret(s):
```
kubectl get secrets
```

3. Create new repository on Dockerhub:
This is done on the Dockerhub UI after logging in with button 'Create Repository'.
In this case, give the repository the name 'media_stream_recorder'.

4. Build and push Docker image to Dockerhub registry:
- Login to Dockerhub on docker CLI:
```
docker login --username=<DOCKERHUB_USERNAME>
```
- Build the image locally and tag it:
```
docker build -t media_stream_recorder:latest .
docker images
docker tag <IMAGE_ID> <DOCKERHUB_USERNAME>/media_stream_recorder:latest
docker push <DOCKERHUB_USERNAME>/media_stream_recorder:latest
```

5. Apply the k8s deployment yaml:
- On your local machine, connect to the cluster with command-line access. Like
above, 'Connect' to your cluster and execute the 'get-credentials' command
it auto-generates.
- Check you see the GKE cluster with `kubectl get nodes`.
- Per stream, apply the corresponding yaml.  For example:
```
kubectl apply -f deploy_record_bbcradio4.yaml
```
Monitor with the following commands:
```
kubectl get deploy
kubectl describe deploy deploy-msr-bbcradio4
kubectl get pods
kubectl logs <POD_NAME>
```

Congratulations, you are now recording with a GKE cluster!
