# openshiftVM


#### Replace <pod-name> with the actual pod name from above command
oc port-forward pod/rhel9-vm-100g-<pod-name> 2222:22

ssh -p 2222 cloud-user@localhost
sudo subscription-manager register --username user --password passed

# Switch to root
sudo -i

# Update the system
dnf update -y

# Install required packages
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

# Install Python dependencies
pip3 install --upgrade pip

pip3 install openvino

https://docs.openvino.ai/2024/get-started/install-openvino/install-openvino-yum.html
