provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "hello_world_instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "HelloWorldInstance"
  }
}

output "public_ip" {
  value = aws_instance.hello_world_instance.public_ip
}
