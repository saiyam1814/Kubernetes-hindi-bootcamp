## NFS server install on node01 of Killercoda or any public instance 
```
sudo apt update
sudo apt install -y nfs-kernel-server

```
Export directory
```
sudo mkdir -p /srv/nfs/kubedata
sudo chown nobody:nogroup /srv/nfs/kubedata
sudo chmod 777 /srv/nfs/kubedata

```
Configuring export 

```
echo "/srv/nfs/kubedata *(rw,sync,no_subtree_check,no_root_squash)" | sudo tee -a /etc/exports

```

Exporting the share 
```
sudo exportfs -rav

```

Start the sever

```
sudo systemctl restart nfs-kernel-server

```