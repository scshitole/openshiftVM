# openshiftVM


# Replace <pod-name> with the actual pod name from above command
oc port-forward pod/rhel9-vm-100g-<pod-name> 2222:22

ssh -p 2222 cloud-user@localhost
# password: default
