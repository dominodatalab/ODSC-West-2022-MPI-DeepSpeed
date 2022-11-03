### ODSC-West 2022 Tutorial on MPI and DeepSpeed

This tutorial covers absolute beginner (MPI), intermediate (summarization and translation tasks) and advanced (a computer vision example).  We also provide supplementary materials.  We do not recommend working on any supplementary materials during the workshop as you will not have access to appropriate GPU clusters.  However you can take this code and run it on any MPI + DeepSpeed Cluster of your choice.  Below are the dockerfile instructions for running the MPI+DeepSpeed code on your own.

#### Dockerfile Instructions for the Workspace

```
# System-level dependency injection runs as root
USER root:root

# Validate base image pre-requisites
# Complete requirements can be found at
# https://docs.dominodatalab.com/en/latest/reference/environments/Automatic_Custom_Image_Compatibility.html#custom-image-requirements-for-domino-compatibility
RUN /opt/domino/bin/pre-check.sh

# Configure /opt/domino to prepare for Domino executions
RUN /opt/domino/bin/init.sh

# Validate the environment
RUN /opt/domino/bin/validate.sh

RUN apt-get update
RUN apt-get -y install pdsh

RUN pip install deepspeed mpi4py pytorch-lightning rouge_score sentencepiece sacrebleu datasets pypdsh ipywidgets IProgress jupyter evaluate torchvision pillow>=7.1.0 matplotlib
RUN pip install git+https://github.com/huggingface/transformers accelerate

```

#### Dockerfile Instructions for the Cluster

```
USER root

RUN apt-get update
RUN apt-get -y install pdsh
RUN pip install deepspeed pypdsh mpi4py pytorch-lightning rouge_score sentencepiece sacrebleu datasets evaluate torchvision pillow>=7.1.0 matplotlib
RUN pip install git+https://github.com/huggingface/transformers accelerate
```

Please feel free to reach out to the Field Data Science Team with any questions.  We appreciate your attendance at our workshop. Materials will be uploaded to a public github repository after the workshop.
