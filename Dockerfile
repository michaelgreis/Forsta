FROM amazonlinux
RUN yum update -y
RUN yum install python3 -y
RUN yum install nano -y
RUN yum install zip -y
RUN yum install unzip -y

#AWS CLI Installation
#RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
#RUN unzip awscliv2.zip
#RUN ./aws/install

#create working directory
ADD . /user/src 
RUN pip3 install boto3 -t /user/src/Forsta/Parser

#v1
#Pull base image
#FROM ubuntu:latest

#Installation packages
#RUN apt-get update
#RUN apt-get install -y curl
#RUN apt-get install -y unzip
#RUN apt-get install -y python3
#RUN apt-get update
#RUN apt-get install -y python3-pip
#RUN pip3 install boto3
#RUN apt-get install nano

#AWS CLI installation
#RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
#RUN unzip awscliv2.zip
#RUN ./aws/install



#Add's current directory into container home directory.
#ADD . /home