provider "aws" {
  region = "us-east-1"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "myeks-1"
  cluster_version = "1.30"

  vpc_id     = "vpc-09a23ce107252dc4b"
  subnet_ids = ["subnet-04a75877b20cf9bf4 "subnet-079b66fb0be7efc65"]

  enable_irsa = true

  eks_managed_node_groups = {
    default = {
      desired_size = 2
      max_size     = 2
      min_size     = 1
      instance_types = ["t2.medium"]
    }
  }
}

# 🔥 IMPORTANT: aws-auth mapping
resource "kubernetes_config_map_v1" "aws_auth" {
  metadata {
    name      = "aws-auth"
    namespace = "kube-system"
  }

  data = {
    mapRoles = yamlencode([
      {
        rolearn  = "arn:aws:iam::652942059461:role/myeks-1-role"
        username = "jenkins"
        groups   = ["system:masters"]
      }
    ])
  }
}
