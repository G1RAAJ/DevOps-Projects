module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "20.0.0"

  cluster_name    = "eks"
  cluster_version = "1.30"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  # ✅ FIX: Enable public access
  cluster_endpoint_public_access  = true
  cluster_endpoint_private_access = true

  # ✅ For practice (allow all)
  cluster_endpoint_public_access_cidrs = ["0.0.0.0/0"]

  eks_managed_node_groups = {
    default = {
      desired_size = 1
      max_size     = 2
      min_size     = 1

      # ✅ FIX: use supported instance
      instance_types = ["t3.micro"]

      # Optional but safe
      ami_type = "AL2_x86_64"
    }
  }
}
