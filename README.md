# translate-be
This is the backend service for my quick kubernetes demo, it can also be ran as a stand alone service. It simply takes a language code and returns hello world in that language. It relies on Google Translate, which needs to be enabled in the GCP Console. You will also need to set-up a service account and download the private JSON key. More information setting up Google Translate AP can be found [here](https://cloud.google.com/translate/docs/quickstart?csw=1).

The frontend code can be found [here](https://github.com/anners/translate-fe).

## docker set-up
This can be ran locally as a docker container.
```
pip3 install -r requirements.txt
docker run -d -p 5001:5001 translate-be
```
alternatively you can run: ```docker pull anners/translate-be:latest```

## python set-up
This can also just be ran as a python/flask app.
```
pip3 install -r requirements.txt
python3 hello.py
```

## kubernetes quick and dirty set-up
Set up cluster with GKE (or any other way you prefer)
```
gcloud container clusters create translate
```
Create a secret with your private key, the deployment file assumes the key is named key.json. 
If not, update the deployment file.
```
kubectl create secret generic translate-key --from-file=key.json=<path-to-key>.json
```
Create the deployment and service
```
kubectl create -f deployment/translate-be-app.yaml
kubectl create -f deployment/translate-be-service.yaml
```
Your service should now be available. You can use various kubectl commands to see what is running.
```
kubectl [get|describe] deployments
kubectl [get|describe] pods
kubectl [get|describe] services
```

## skaffold
Skaffold is a ridiculously easy command line tool that facilitates continuous development for Kubernetes.
For information on installing skaffold check out it's [GitHub page](https://github.com/GoogleContainerTools/skaffold).

To use it for this project change the image name in skaffold.yaml and deployment/tanslate-be-app.yaml to match your docker repo and simply run ```skaffold dev```
