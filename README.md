# Openshift as Infrastructure with NGINX + Proxy & OpenVino 
# OpenVino Model used

This project related to setting up Openshift as infrastructure, specifically focusing on integrating it with NGINX, a proxy, and OpenVino. The repository contains several files including a README, an image, and other unspecified files, suggesting it provides configuration and instructions for this setup. The content includes commands for setting up a virtual machine, managing subscriptions, installing software, and using Podman with an OpenVino container. A link to a video is also included.

The key technologies and software components being utilized and integrated include:

*   **Openshift**: This is highlighted as the infrastructure platform.
*   **NGINX + Proxy**: These are mentioned together as part of the infrastructure setup within Openshift.
*   **OpenVino**: This is a central component, indicated by the repository title. A specific **OpenVino model** is referenced from **Hugging Face**, and an **Intel OpenVINO runtime container** image is pulled and utilized.
*   **Podman**: This container management tool is used to run and interact with the OpenVino runtime container.
*   **GitHub**: The entire project is hosted on this platform, which provides features for code hosting, collaboration (issues, pull requests, discussions), automation (actions), and security.
*   **RHEL 9**: Commands related to package management (`dnf`, `yum`) and subscription management (`subscription-manager`) suggest that **Red Hat Enterprise Linux 9** is the operating system environment being used.
*   Various development tools and languages: The project involves installing development tools like `cmake`, `gcc`, `gcc-c++`, and `make`. The code itself is written using **Python**, **JavaScript**, **CSS**, and **HTML**. Command-line tools like `oc` (likely for interacting with Openshift), `ssh`, `sudo`, `wget`, and `unzip` are also used.

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



