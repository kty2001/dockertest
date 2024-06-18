# base image
FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu20.04

# working directory
WORKDIR /working

ENV DEBIAN_FRONTEND=noninteractive

# package install
RUN apt-get update && apt-get install -y \
    git \
    wget \
    build-essential \
    python3-pip \
    python3-dev \
    ninja-build \
    libyaml-dev \
    libfreetype6-dev \
    libpng-dev \
    pkg-config \
    libopenblas-dev \
    liblapack-dev
RUN ln -s /usr/bin/python3 /usr/bin/python

# requirements install
COPY requirements.txt requirements.txt
COPY check_gpu.py /working/check_gpu.py
COPY wait-for-it.sh /working/wait-for-it.sh

RUN chmod +x /working/wait-for-it.sh
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install torch==2.3.0 torchvision==0.18.0  --index-url https://download.pytorch.org/whl/cu118


# setting cuda
ENV CUDA_HOME=/usr/local/cuda-11.8
ENV PATH=${CUDA_HOME}/bin:${PATH}
ENV LD_LIBRARY_PATH=${CUDA_HOME}/lib64:${LD_LIBRARY_PATH}


# halpecocotools install
RUN git clone https://github.com/HaoyiZhu/HalpeCOCOAPI.git
WORKDIR /working/HalpeCOCOAPI/PythonAPI
RUN python setup.py build_ext --inplace
RUN python setup.py install

# AlphaPose install
WORKDIR /working
ENV TORCH_CUDA_ARCH_LIST="8.6"
RUN git clone https://github.com/MVIG-SJTU/AlphaPose.git
WORKDIR /working/AlphaPose
RUN python3 setup.py build develop --user

# MotionBERT
WORKDIR /working
RUN git clone https://github.com/Walter0807/MotionBERT.git

# command
CMD ["bash"]