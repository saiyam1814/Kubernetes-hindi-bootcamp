## Configmaps
Creating config map 
Example 1 demonstrates how you can have a user for the database passed in as a config map as an env:

```
kubectl apply -f cm1.yaml
kubectl apply -f pod1.yaml

kubectl exec -it mysql-pod -- mysql -u root -p
SELECT user FROM mysql.user;
SHOW DATABASES;


```

Example 2 demonstrates a practicle use case where the dev/prod properties can be defined and used for the application when required. In prod your application should be able to read config from the file located at /etc/config/settings.properties. This could mean parsing the file on startup or dynamically reading values when required.

```
kubectl aply -f cm2.yaml
kubectl apply -f pod2.yaml
kubectl exec -it <pod-name> -- cat /etc/config/settings.properties
```

Exmaple 3 How can you make it run programatically 

```
cd example3
docker build -t ttl.sh/hindi-boot:1h .
docker push ttl.sh/hindi-boot:1h
kubectl apply -f app.yaml
kubectl logs -l app=config-reader
```


Secrets 
kubectl create secret generic my-opaque-secret --from-literal=password=supersecret

```
apiVersion: v1
kind: Secret
metadata:
  name: my-opaque-secret
type: Opaque
data:
  password: c3VwZXJzZWNyZXQ=  # base64 encoded value of 'supersecret'

```
```
kubectl create secret generic my-basic-auth-secret \
--from-literal=username=myuser \
--from-literal=password=mypassword \
--type=kubernetes.io/basic-auth
```

```
kubectl create secret generic my-ssh-key-secret \
--from-file=ssh-privatekey=/path/to/.ssh/id_rsa \
--type=kubernetes.io/ssh-auth

```
```
kubectl create secret tls my-tls-secret \
--cert=path/to/cert/file \
--key=path/to/key/file
```


### mysql example again 
Create CM , then create secrets 
```
kubectl create secret generic mysql-root-pass --from-literal=password='abc123'
kubectl create secret generic mysql-user-pass --from-literal=password='saiyampass'

#OR
apiVersion: v1
kind: Secret
metadata:
  name: mysql-root-pass
type: Opaque
data:
  password: base64encoded  


```


### Image pull secrets

```
docker buildx build --platform linux/amd64 -t saiyam911/bootcamp-demo:v1 . --push
kubectl create secret docker-registry pullsec --docker-username saiyam911 --docker-password $SECRET --docker-email saiyam911@gmail.com
```
