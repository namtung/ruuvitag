# RuuviTag
> Raspberry Pi compatible Docker base image for collecting Ruuvitag data based on [Kipe] (https://github.com/kipe/ruuvitag)

## Installation

Build Docker image
```sh
docker build -t <image-name> .
```

## Usage
For basic usage:

```sh
docker run -it --privileged --net=host <image-name>:latest
```
