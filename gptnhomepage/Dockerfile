# base image
FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu20.04

# working directory
WORKDIR /working

COPY check_gpu.py /working/check_gpu.py
COPY wait-for-it.sh /working/wait-for-it.sh
COPY requirements.txt /working/requirements.txt

RUN chmod +x /working/wait-for-it.sh
RUN apt-get update && apt-get install -y git wget build-essential python3-pip python3-dev ninja-build
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118


# command
CMD ["python", "check_gpu.py"]