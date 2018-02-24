# translate-be
This is the backend service for my quick kubernetes demo, it can also be ran as a stand alone service. It simply takes a language code and returns hello world in that language. It relies on Google Translate, which needs to be enabled in the GCP Console. You will also need to set-up a service account and download the private JSON key. More information setting up Google Translate AP can be found [here](https://cloud.google.com/translate/docs/quickstart?csw=1).

## docker set-up
This can be ran locally as a docker container.
```
pip3 install -r requirements.txt
docker run -d -p 5000:5000 google-translate
```
alternatively you can run: ```docker pull anners/google-translate```

## python set-up
This can also just be ran as a python/flask app.
```
python3 hello.py
```

## kubernetes quick and dirty set-up
Set up cluster with GKE (or any other way you prefer)
```
gcloud container clusters create translate
```
Create a secret with your private key
```
kubectl create secret generic translate-key --from-file=key.json=<path-to-key>.json
```
Create the deployment and service
```
kubectl create -f deployment/translate-app.yaml
kubectl create -f deployment/translate-service.yaml
```
Your service should now be available. You can use various kubectl commands to see what is running.
```
kubectl [get|describe] deployments
kubectl [get|describe] pods
kubectl [get|describe] services
```
