#
# set-up
pip install -r requirements.txt
enable Google Cloud Translation API in the GCP Console
#to do - permissions for Translate API only
docker run -d -p 5000:5000 google-translate


alternatively you can run: docker pull anners/google-translate
kubectl create secret generic translate-key --from-file=key.json=<path-to-key>.json
