ARG distro=stretch
FROM resin/rpi-raspbian:$distro
RUN apt-get update && apt-get install -y python-pip \
    build-essential \
    libssl-dev \
    libffi-dev \
    python-dev \
    libglib2.0-dev \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*
RUN python -m pip install --upgrade pip setuptools wheel
COPY . ./
RUN pip install setup.py
RUN chmod +x ./ruuvi.py
CMD ["python","./ruuvi.py"]
