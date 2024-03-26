docker run -d --name my-nginx-container --memory 512m --cpus 1 nginx
ps aux | grep '[n]ginx' | sort -n -k 2 | head -n 1 | awk '{print $2}'
lsns -p pid
systemd-cgls --no-pager
cat /sys/fs/cgroup/memory/system.slice/docker-5ba642ac2146b6d7f2c538d673a480f2ab6a4cec8142eae034286fdefcb5d024.scope/memory.stat

Kubernetes 
=========
kubectl run nginx --image=nginx 
