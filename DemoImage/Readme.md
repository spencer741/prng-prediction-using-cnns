docker build --rm -f ./DockerContainer/Dockerfile -t tester .

docker run -v C:\Users\YOURUSERNAMEHERE\Desktop\S20-team7-project\WorkSpace:/Demo -it --rm --privileged tester bash  
