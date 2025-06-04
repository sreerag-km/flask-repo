## This file not related to the deploment pipeline. Since there was a requirement "Configure cloud infrastructure with Terraform" i have added a terraform code for creating s3 bucket in aws.
------------------------------------------------


provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "bucket-created-using-terraform-123" 
}
