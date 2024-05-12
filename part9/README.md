## Authentication
```
kubectl config view
find the cluster name from the kubeconfig file
export CLUSTER_NAME=

export APISERVER=$(kubectl config view -o jsonpath='{.clusters[0].cluster.server}')
curl --cacert /etc/kubernetes/pki/ca.crt $APISERVER/version
curl --cacert /etc/kubernetes/pki/ca.crt $APISERVER/v1/deployments
```
The above didn't work and we need to authenticate, so let's use the first client cert. Before that create the client and the key file base64 -d from kubeconfig file
```
curl --cacert /etc/kubernetes/pki/ca.crt --cert client --key key $APISERVER/apis/apps/v1/deployments 
```
above you can have the client and the key from the kubeconfig file
```
echo "<client-certificate-data_from kubeconfig>" | base64 -d > client
echo "<client-key-data_from kubeconfig>" | base64 -d > key
```
Now using the sA Token 1.24 onwards you need to create the secret for the SA
```
TOKEN=$(kubectl create token default)
curl --cacert /etc/kubernetes/pki/ca.crt $APISERVER/apis/apps/v1 --header "Authorization: Bearer $TOKEN"
```
from inside pod you can use var/run/secrets/kubernetes.io/serviceaccount/token path for the token to call the kubernetes service
```
proxy

kubectl proxy --port=8080 &s
curl localhost:8080/apis/apps/v1/deployments
```
## RBAC
Cluster role to create deployment and daemonset
```
kubectl create ns app
kubectl create sa demo-sa -n app
kubectl create clusterrole my-rules --verb=create --resource=deployments
--resource=daemonsets -o yaml --dry-run=client > my-rules.yaml
```

```
kubectl create ns dev1
kubectl create serviceaccount demo2-sa -n dev1
kubectl create role demo2-deployment-creator --verb=create
--resource=deployments.apps -n dev1
kubectl create rolebinding demo2-sa-deployment-binder
--role=demo2-deployment-creator --serviceaccount=dev1:demo2-sa -n dev1
kubectl auth can-i create deployments --namespace dev1
--as=system:serviceaccount:dev1:demo2-sa
kubectl create token demo2-sa -n dev1
APISERVER=$(kubectl config view --minify -o
jsonpath='{.clusters[0].cluster.server}')
curl -k -X POST $APISERVER/api/v1/namespaces/dev1/secrets \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
        "apiVersion": "v1",
        "kind": "Secret",
        "metadata": {
            "name": "demo-secret"
        },
        "data": {
            "key": "'$SECRET_DATA'"
} }'
```

## Service Account 
kubectl create ns demo 
kubectl get sa -n demo 

kubectl create serviceaccount my-service-account
serviceaccount/my-service-account created
controlplane $ kubectl get secrets -o json | jq -r '.items[] | select(.type=="kubernetes.io/service-account-token" and .metadata.annotations."kubernetes.io/service-account.name" == "my-service-account")'


## Valideing admission policy
```
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingAdmissionPolicy
metadata:
  name: "demo-policy.example.com"
spec:
  failurePolicy: Fail
  matchConstraints:
    resourceRules:
    - apiGroups:   ["apps"]
      apiVersions: ["v1"]
      operations:  ["CREATE", "UPDATE"]
      resources:   ["deployments"]
  validations:
    - expression: "object.spec.replicas <= 5"

---

apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingAdmissionPolicyBinding
metadata:
  name: "demo-binding-test.example.com"
spec:
  policyName: "demo-policy.example.com"
  validationActions: [Deny]
  matchResources:
    namespaceSelector:
      matchLabels:
        environment: test
```
Label and test 
```
kubectl label ns default environment=test
kubectl create deploy nginx --image=nginx --replicas=6
```

## Imagepolicywebhook
git clone https://github.com/saiyam1814/imagepolicy.git
mkdir /etc/kubernetes/demo
cp -r imagepolicy/ /etc/kubernetes/demo
cd /etc/kubernetes/demo
ls


```
- --admission-control-config-file=/etc/kubernetes/demo/admission.json
- --enable-admission-plugins=NodeRestriction,ImagePolicyWebhook
```

```
  volumeMounts:
  - mountPath: /etc/kubernetes/demo
    name: admission
    readOnly: true
volumes:
- hostPath:
    path: /etc/kubernetes/demo
  name: admission

``` 

Test and Verify
```
kubectl run nginx --image=nginx
```

## exmaple folder
```
kubectl auth can-i create deployments --as=system:serviceaccount:default:deployment-manager
kubectl auth can-i create secrets --as=system:serviceaccount:default:deployment-manager
kubectl auth can-i list services --as=system:serviceaccount:default:deployment-manager

```