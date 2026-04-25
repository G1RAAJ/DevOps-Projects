#!/bin/bash
set -e

echo "Updating system..."
sudo dnf update -y

echo "Installing tools..."
sudo dnf install -y git wget curl unzip tar vim java-17-amazon-corretto docker awscli

echo "Starting Docker..."
sudo systemctl start docker
sudo systemctl enable docker

echo "Adding jenkins to docker group..."
sudo usermod -aG docker jenkins || true

echo "Installing kubectl..."
curl -o kubectl https://amazon-eks.s3.us-east-1.amazonaws.com/latest/bin/linux/amd64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

echo "Installing eksctl..."
curl --silent --location https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_Linux_amd64.tar.gz | tar xz
sudo mv eksctl /usr/local/bin/

echo "Installing Terraform..."
sudo dnf install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo dnf install terraform -y

echo "Setup completed!"
