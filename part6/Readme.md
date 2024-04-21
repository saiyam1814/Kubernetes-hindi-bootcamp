
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
kubectl create deploy bootcamp --image nginx --replicas 3 --port 80
kubectl rollout status deployment bootcamp

Update image 
kubectl set image deploy bootcamp nginx=nginx:1.14.0 --record
kubectl rollout history
kubectl rollout history deploy/bootcamp --revision=2
kubectl rollout undo deployment/bootcamp --to-revision=1
kubectl scale deployment/bootcamp --replicas=6
kubectl rollout pause deployment/bootcamp

For Recreate strategy 
kubectl set image deploy/demo-deployment demo=nginx:14.0

Canary
kubectl get pods -o=custom-columns=NAME:.metadata.name,IMAGE:.spec.containers[*].image --watch

