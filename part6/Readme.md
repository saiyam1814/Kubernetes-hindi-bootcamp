
## ReplicaSet
Create ReplicaSet
Delete RS

```
kubectl proxy --port=8080

curl -X DELETE 'http://localhost:8080/apis/apps/v1/namespaces/default/replicasets/nginx-rs' \
     -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Foreground"}' \
     -H "Content-Type: application/json"

```

```
curl -X DELETE 'http://localhost:8080/apis/apps/v1/namespaces/default/replicasets/nginx-rs' \
     -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Background"}' \
     -H "Content-Type: application/json"

```

```
curl -X DELETE 'http://localhost:8080/apis/apps/v1/namespaces/default/replicasets/nginx-rs' \
     -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Orphan"}' \
     -H "Content-Type: application/json"

```
## Deployments 
Create deployment
```
kubectl create deploy bootcamp --image nginx --replicas 3 --port 80
kubectl rollout status deployment bootcamp
```
Update image 
```kubectl set image deploy bootcamp nginx=nginx:1.14.a --record````
See the rollout history 
```
kubectl rollout history deploy/bootcamp
kubectl rollout history deploy/bootcamp --revision=2
```
Rollback deployment when something foes wrong, you can also pause a rollout
```
kubectl rollout undo deployment/bootcamp --to-revision=1
```
Scale deployment, you can also do `kubectl edit deployment`

```
kubectl scale deployment/bootcamp --replicas=6
kubectl rollout pause deployment/bootcamp
```

For Recreate strategy
```
kubectl apply -f recreate.yaml
```
Update the image
```
kubectl set image deploy/demo-deployment demo=nginx:14.0
```
You will all getting terminated and new ones getting created leading to little downtime.

Canary Deployment - Usually its done with Gateway API, service mesh etc but with deployment you can simulate like below:
```
kubectl apply -f canary-svc.yaml
kubectl apply -f deploy-canary.yaml
kubectl apply -f deploy -canary-v2.yaml
kubectl get pods -o=custom-columns=NAME:.metadata.name,IMAGE:.spec.containers[*].image --watch
```
Check the endpoints for the service created and you will see all in the endpoints ready to be served traffic. 

## Probes 
Probes you can test by deploying probe.yaml and then deleting that, edit the yaml with port 8080 in the probe check and wait for sometime to see it fail. 
