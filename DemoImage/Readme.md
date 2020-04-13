# How to setup for the demo.
Note I am running Windows 10 and using powershell, but the commands are similar for other platforms.

#### Pre-reqs
Have docker installed and setup on your machine correctly. 

Have Git installed and setup on your machine correctly.

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
docker build --rm -f ./DemoImage/Dockerfile -t democontainer .
```
Where democontainer is the name of your built image (you can change this to whatever).

Before you run the command below, make sure you modify the path "C:\Users\YOURUSERNAMEHERE\Desktop\S20-team7-project\WorkSpace" to reflect your path to the cloned repo. Make sure to include \WorkSpace.

```
docker run -v C:\Users\YOURUSERNAMEHERE\Desktop\S20-team7-project\WorkSpace:/WorkSpace -it --rm --privileged democontainer bash 
```

What we are doing here is building a local docker container, which installs the dependencies internally. The /WorkSpace directory in the Docker Container will be mapped to the /WorkSpace folder in your local copy of the repository. When you execute docker run, it will drop you into a session in the container. Any changes you make in /WorkSpace will be persisted to the host (your local machine).

