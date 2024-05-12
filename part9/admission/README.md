openssl genrsa -out ca.key 2048\nopenssl req -x509 -new -nodes -key ca.key -subj "/CN=example-ca" -days 10000 -out ca.crt\n
openssl genrsa -out server.key 2048\nopenssl req -new -key server.key -out server.csr -config server.conf\n
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 3650 -extensions v3_ca -extfile server.conf\n
docker build --platform linux/amd64 -t ttl.sh/mutating-webhook-server:24h
docker push ttl.sh/mutating-webhook-server:24h 