# RuuviTag
> Raspberry Pi compatible Docker base image for collecting Ruuvitag data based on [Kipe's work](https://github.com/kipe/ruuvitag)

## Installation

Build Docker image
```sh
docker build -t <image-name> .
```
Or pull the image from Docker Hub
```sh
docker pull namtung/rpi-ruuvitag
```

## Usage
For basic usage:

```sh
docker run -it --cap-add=NET_ADMIN --net=host rpi-ruuvitag:latest
```
