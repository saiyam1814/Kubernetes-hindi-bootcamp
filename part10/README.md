In this part learned about Kubernetes volumes and its importance. 

## emptyDir
Temporary volumes that lives tills the lifespan of a pod. 

```
apiVersion: v1
kind: Pod
metadata:
  name: emptydir-pod
spec:
  containers:
    - name: busybox
      image: busybox
      command: ['sh', '-c', 'echo "Writing data to /data/emptydir-volume..."; echo "Hello from Kubesimplify" > /data/emptydir-volume/hello.txt; sleep 3600']
      volumeMounts:
        - name: temp-storage
          mountPath: /data/emptydir-volume
  volumes:
    - name: temp-storage
      emptyDir: {}

```
This pod created a container busyboz and creates emptyDir, mounts it inside the pod under /tmp/emptydir-volume and data is getting inserted from the pod with the shell script into hello.txt to the mounted location. 

## hostpath 
`kubectl apply -f hostpath.yaml`
