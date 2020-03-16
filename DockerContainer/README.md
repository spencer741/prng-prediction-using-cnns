# CSCI4850
Docker container for CSCI 4850/5850 - Neural Networks

This container is built on top of jupyter/datascience-notebook provided by jupyter/docker-stacks. It provides a JupyterLab environment with several essential (and non-essential) tools used in CSCI4850/5850 - Neural Networks.

To prep:
```
git clone https://github.com/jlphillipsphd/CSCI4850.git
```
 
To build:
```
docker build -t csci4850 CSCI4850
```

To run:
```
docker run -it --rm -p 8888:8888 --user root -e JUPYTER_ENABLE_LAB=yes -e GRANT_SUDO=yes -v /home/jphillips:/home/jovyan/work csci4850
```

You will need to modify `/home/jphillips` to where your files are in order to make this work...

If you want to pull from Docker Hub instead:
```
docker pull jlphillips/csci4850
docker run -it --rm -p 8888:8888 --user root -e JUPYTER_ENABLE_LAB=yes -e GRANT_SUDO=yes -v /home/jphillips:/home/jovyan/work jlphillips/csci4850
```
