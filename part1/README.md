# Kubernetes-hindi-bootcamp Part-1

## Docker Setup

1. Run the following command to create a Docker container named "my-nginx-container" with specified memory and CPU resources:

```bash
docker run -d --name my-nginx-container --memory 512m --cpus 1 nginx
```
**This command launches a Docker container named "my-nginx-container" using the NGINX image with a memory limit of 512 megabytes and one CPU core.**
<p>&nbsp;</p>

2. Retrieve the process ID (PID) of the NGINX process running inside the container:
```bash
ps aux | grep '[n]ginx' | sort -n -k 2 | head -n 1 | awk '{print $2}'
```
**This command searches for the NGINX process, sorts the results based on the second column (PID), and prints the PID of the first process found.**
<p>&nbsp;</p>

3. List the namespaces associated with the NGINX process using its PID:

```bash 
lsns -p <pid>
```
**Replace <pid> with the PID obtained in the previous step. This command displays the namespaces associated with the NGINX process.**
<p>&nbsp;</p>

4. View the control groups (cgroups) hierarchy for the NGINX container:

```bash
systemd-cgls --no-pager
```
**This command shows the cgroups hierarchy, allowing you to inspect the resource usage of the NGINX container.**
<p>&nbsp;</p>

5. Display memory statistics for the NGINX container's cgroup:

```bash
cat /sys/fs/cgroup/memory/system.slice/docker-5ba642ac2146b6d7f2c538d673a480f2ab6a4cec8142eae034286fdefcb5d024.scope/memory.stat
```
**This command provides memory usage statistics for the NGINX container's cgroup.**
<p>&nbsp;</p>

## Kubernetes Setup

### To deploy NGINX on Kubernetes:

1. Execute the following command to create a Kubernetes deployment named "nginx" using the NGINX image:
```bash
kubectl run nginx --image=nginx
```
**This command creates a Kubernetes deployment named "nginx" using the NGINX image.**


<p>&nbsp;</p>

### For More you can Visit 
- Blog & Newsletter <https://kubesimplify.com/>
- YouTube [Kubesimplify Hindi](https://www.youtube.com/watch?v=F8FcWV56sp4&list=PL2z28C0cnXhMSIN0JyZkI1XBg1K3VZ3cV)
