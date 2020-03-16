FROM jupyter/datascience-notebook

LABEL maintainer="Joshua L. Phillips <https://www.cs.mtsu.edu/~jphillips/>"

USER root

# Additional tools
RUN apt-get update && \
    apt-get install -y \
    autoconf \
    libtool \
    vim \
    less \
    texlive-science \
    ssh \
    rsync \
    zip \
    tmux \
    graphviz \
    xvfb \
    python-opengl \
    gdb

# CSCI 4350 & 4850
USER $NB_UID

RUN pip install --quiet \
    keras \
    tensorflow \
    torch \
    torchvision \
    bash_kernel \
    pydot \
    xvfbwrapper \
    gym \
    gensim \
    nltk \
    stanfordcorenlp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

RUN python -m nltk.downloader all

