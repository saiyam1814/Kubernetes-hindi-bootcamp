

# What happens when a pod runs - namespace 

```
apiVersion: v1
kind: Pod
metadata:
  name: shared-namespace
spec:
  containers:
    - name: p1
      image: busybox
      command: ['/bin/sh', '-c', 'sleep 10000']
    - name: p2
      image: nginx
```
Commands 

```
ip netns list

```
### how to check pause container 
```
kubectl run nginx --image=nginx
lsns | grep nginx
```
copy the process IP from above and run 
```
lsns -p <pid>

```

### check the network namespace (this gives list of all network namespaces)
`ls -lt /var/run/netns`

### exec into the namespace or into the pod to see the IP links

```
ip netns exec <namespace> ip link
kubectl exec -it shared-namespace -- ip addr 
```
Now you will see `eth@9` -> after `@` there will be a number and you can then search its corresponding link on the node using 
`ip link | grep -A1 ^9`
you will be able to see the same network namespace after link
These are the veth pairs or based on the CNI 



## Services 

```
kubectl run nginx --image=nginx
kubectl run nginx2 --image=nginx
kubectl label pod nginx2 run=nginx --overwrite

kubectl expose pod nginx --port 80 --dry-run=client -oyaml
kubectl expose pod nginx --port 80  
kubectl get ep

```



##Headless Service
```
kubectl create -f tatefulset.yaml
kubectl apply -f svc.yaml
```
Check 
`kubectl exec -it postgres-0 -- psql -U postgres`

## ExternalName
Create database and app namespaces 
```
kubectl create ns database-ns
kubectl create ns application-ns
```
Create the databas pod and service
```
kubectl apply -f db.yaml
kubectl apply -f db_svc.yaml
```
Create ExternalName service
```
kubectl apply -f externam-db_svc.yaml
```
Create Application to access the service
Docker build
`docker build --no-cache --platform=linux/amd64 -t ttl.sh/saiyamdemo:1h . `

Docker push 
`docker push ttl.sh/saiyamdemo:1h`

`kubectl apply -f apppod.yaml`

Check the pod logs to see if the connection was successful 

`kubectl logs my-application -n application-ns`



## Ingres controller
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.9.4/deploy/static/provider/cloud/deploy.yaml
```
Deploy all in Ingress folder after creating below config map 

`kubectl create configmap nginx-config --from-file=nginx.conf`

ssh onto the node where the pod is deployed and the change the /etc/hosts file.



## Nodeport check via iptables
```
sudo iptables -t nat -L -n -v | grep -e NodePort -e KUBE
sudo iptables -t nat -L -n -v | grep 31188
```