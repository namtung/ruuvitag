ARG distro=stretch
FROM resin/rpi-raspbian:$distro
RUN apt-get update && apt-get install -y python python-setuptools git python-pip build-essential libssl-dev libffi-dev python-dev libglib2.0-dev
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install git+https://github.com/namtung/ruuvitag.git
COPY ruuvi.py ./
RUN hcitool scan
RUN chmod +x ./ruuvi.py
CMD ["python","./ruuvi.py"]
