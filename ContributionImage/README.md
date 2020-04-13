# How to setup for contribution workflow.
This is also a good way to explore and run the code in general.

Note I am running Windows 10 and using powershell, but the commands/instructions are pretty much the same for other platforms. On a unix-based platform, you will use / instead of \ when specifying the path.

#### Pre-reqs
Have docker installed and setup on your machine. (This can be tricky depending on the platform and build your machine is on)

Have Git installed and setup on your machine.

#### Instructions
Navigate to where you want your local copy of our repository to be. (for example, I am just putting it on the Desktop)

Type:
```
git clone https://github.com/CSCI4850/S20-team7-project.git
```
Then Type:
```
cd S20-team7-project
```
Then Type:
```
docker build -t dockercontainer DockerContainer
```
Before you run the command below, make sure you modify the path "C:\Users\YOURUSERNAMEHERE\Desktop\S20-team7-project\WorkSpace" to reflect your path to the cloned repo. Make sure to include \WorkSpace.

***What we are doing here is building a local docker container where we run the Jupyter Lab stack. The /WorkSpace directory in the (Docker Container) Jupyter Lab will be mapped to the /WorkSpace folder in your local copy of the repository. This means you can type the docker run command below, open up the file you want to work on in Jupyter Lab (via a browser on your local machine), save it, and then submit a pull request. Since all changes get persisted to the /WorkSpace folder within the repo, this is more of an automated workflow, especially if you are trying to contribute.***

```
docker run -it --rm -p 8888:8888 --user root -e JUPYTER_ENABLE_LAB=yes -e GRANT_SUDO=yes -v C:\Users\YOURUSERNAMEHERE\Desktop\S20-team7-project\WorkSpace:/home/jovyan/WorkSpace dockercontainer
```

**The above saves a lot of hassle... but you can always go the more manual route for contributuion**

Now, to access Jupyter Lab, look for something like this in your command line output:
```
[I 00:11:03.609 LabApp] The Jupyter Notebook is running at:
[I 00:11:03.609 LabApp] http://a3f363a92b41:8888/?token=f35d7cb340c6074d46f9b4c3280b0816c02de3148fa9c2ec
[I 00:11:03.610 LabApp]  or http://127.0.0.1:8888/?token=f35d7cb340c6074d46f9b4c3280b0816c02de3148fa9c2ec
[I 00:11:03.610 LabApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```

Copy the url (preferably 2nd one) and paste into your browser. Jupyter Lab should now load. How? Because forwarded the port from the docker container to localhost when we ran the container. 

Note that with this image, there are a lot of extra dependencies that are not critical for our project to run. Navigate to the /WorkSpace Directory and start hacking.

Note that the CSCI4850 Docker Container does not satisfy all requirements for our project to run.

# Old readme from CSCI4850 for quick additional reference
### CSCI4850
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
