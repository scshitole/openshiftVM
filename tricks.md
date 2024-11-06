```
oc debug node/ac-1f-6b-ca-4b-74

```
Once you're in the debug pod, you need to chroot to access the host's filesystem:

```
chroot /host

mkdir -p /mnt/data
chmod 755 /mnt/data
```

```
oc expose pod virt-launcher-rhel4nginx-l5mfx --port=80 --target-port=80 --name=nginx-service
```

```
# Create new edge route (OpenShift handles SSL termination)
oc create route edge nginx-route \
    --service=nginx-service \
    --hostname=nginx-plus.f5intel.bd.f5.com \
    --port=80
```
```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
-keyout /path/to/llama.f5intel.bd.f5.com.key \
-out /path/to/llama.f5intel.bd.f5.com.crt

```
