ARG distro=stretch
FROM resin/rpi-raspbian:$distro
RUN apt-get update && apt-get install -y git python-pip \
    build-essential \
    libssl-dev \
    libffi-dev \
    python-dev \
    libglib2.0-dev \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install git+https://github.com/namtung/ruuvitag.git
COPY ruuvi.py ./
RUN chmod +x ./ruuvi.py
CMD ["python","./ruuvi.py"]
