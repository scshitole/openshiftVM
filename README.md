# Openshift as Infrastructure with NGINX + Proxy & OpenVino 
# OpenVino Model used
https://huggingface.co/OpenVINO/open_llama_3b_v2-fp16-ov

#### Replace <pod-name> with the actual pod name from above command
oc port-forward pod/rhel9-vm-100g-<pod-name> 2222:22

ssh -p 2222 cloud-user@localhost

```
sudo subscription-manager register --username user --password passed
```


### Switch to root
sudo -i

### Update the system
dnf update -y

### Install required packages
dnf groupinstall -y "Development Tools"
dnf install -y \
    python3-pip \
    python3-devel \
    cmake \
    gcc \
    gcc-c++ \
    make \
    wget \
    unzip \
    git

### Install Python dependencies
pip3 install --upgrade pip

sudo subscription-manager repos --enable=rhel-9-for-x86_64-baseos-rpms
sudo subscription-manager repos --enable=rhel-9-for-x86_64-appstream-rpms

sudo yum install podman

podman pull registry.connect.redhat.com/intel/openvino-runtime:2024.4.0

```
podman run -d --name openvino-container registry.connect.redhat.com/intel/openvino-runtime:2024.4.0 /bin/bash -c "while true; do sleep 30; done;"

podman exec -it openvino-container /bin/bash

```
### Video Link below
https://drive.google.com/file/d/18VGkRJ1nbBAEj2wDNDEGSQ6gFxsVaGHO/view?usp=sharing

![image](https://github.com/user-attachments/assets/d19a339f-50bf-42c6-97c1-88046c0cc20b)
![image](https://github.com/user-attachments/assets/9cc4b6dd-992d-4279-9174-08d857a5ce84)



