# MyPhonebook
my very first fullstack app with a miserable frontend without using any css or js


to download the docker container I created a golang script for windows I have a executable just execute it in the shell and it should build the container 
else if you use linux you need to download golang with "sudo apt install golang" than you can run it with: 
`go run main.go`

the project is made in 2 diffrent containers

the first one is the Frontend and backend Container just to represent the website. this one you will have to forward it to port 80 from port 5000 the command to run this container is:
`docker run -d -p 80:5000 website`

---

the second container is the communication to the Database this one is just port 4000 the commant for this one is. But this one won't work because I cancelled all the connection the only one which works is the official Server
`docker run -d -p 4000:4000 api`
