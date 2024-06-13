# base image
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

# working directory
WORKDIR /working

# package install
RUN apt-get update && apt-get install -y git wget build-essential python3-pip python3-dev python3.7
RUN ln -s /usr/bin/python3.7 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip

# requirements install
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118


# cudatoolkit install
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
RUN mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
RUN wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda-repo-wsl-ubuntu-11-8-local_11.8.0-1_amd64.deb
RUN dpkg -i cuda-repo-wsl-ubuntu-11-8-local_11.8.0-1_amd64.deb
RUN cp /var/cuda-repo-wsl-ubuntu-11-8-local/cuda-*-keyring.gpg /usr/share/keyrings/
RUN apt-get update
RUN apt-get -y install cuda

ENV CUDA_HOME=/usr/local/cuda
ENV PATH=${CUDA_HOME}/bin:$PATH
ENV LD_LIBRARY_PATH=${CUDA_HOME}/lib64:${LD_LIBRARY_PATH}

RUN apt-get install -y libyaml-dev


# halpecocotools install
RUN git clone https://github.com/HaoyiZhu/HalpeCOCOAPI.git
WORKDIR /working/HalpeCOCOAPI/PythonAPI
RUN python setup.py build_ext --inplace
RUN python setup.py install


# AlphaPose install
WORKDIR /working
RUN git clone https://github.com/MVIG-SJTU/AlphaPose.git
WORKDIR /working/AlphaPose
RUN python setup.py build develop

WORKDIR /working


# MotionBERT
# RUN git clone https://github.com/Walter0807/MotionBERT.git



# command
CMD ["bash"]