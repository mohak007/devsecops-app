resource "aws_instance" "jenkins_server" {
  ami           = "ami-0f58b397bc5c1f2e8" # Ubuntu (ap-south-1)
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public_subnet_1.id

  tags = {
    Name = "devsecops-ec2"
  }
}
