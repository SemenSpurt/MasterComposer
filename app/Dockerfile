#syntax=docker/dockerfile:1

FROM ubuntu:20.04

ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /home/app

# Install.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y curl pip net-tools arp-scan && \
  rm -rf /var/lib/apt/lists/*

# Copy from ./app to /home/app/
COPY . . 

# EXPOSE 4444

# Install dependencies
RUN pip install -r requirements.txt