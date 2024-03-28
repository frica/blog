Title: Docker image for photolocator
Date: 2024-03-26 20:52
Category: Tech
Tags: docker
Lang: en
Status: draft

To declare the image:
Dockerfile

To build the docker image:
    
    :::bash
    docker build -t photolocator .

`-t` : tag

To run the docker container:
    
    :::bash
    docker run photolocator

First try: 750.54 MB
Second try with alpine: 674.33 MB

Reusable for any Flask based application!
