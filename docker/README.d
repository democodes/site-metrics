			Docker instllation and wordpress container
		========================================================

Created by Rejul James on 1/14/2015 

Contact details : rejuljames@gmail.com

DOCKER INSTALLTION
==================

Prerequisites
----------------
Ubuntu 14.04 64 bit or greater
Kernal version 3.10 or higher( To check the kernel version uname -r )
Make sure firewall has to disabled. If you are using firewall make sure you write appropriate rules

Installation Steps
--------------------
1. Configure docker apt repository

Step:
     Create a file /etc/apt/sources.list.d/docker.list and add deb https://apt.dockerproject.org/repo debian-wheezy main
     apt-get update //  update apt repository

2. Install docker service
Step:
    apt-get install docker-engine // Install docker service
    service docker start // start the service
    update-rc.d docker defaults // start the service automatically after the reboot

3. Testing
Step:
   docker push ubuntu  // Pull hello world image
   docker images   // List all the images in docker
   docker run -i -t ubuntu /bin/bash  //Use ubuntu  image to create the container. If images is not present locallay it will pull the image from docker web repository
   docker ps -a // List all the contrainers in docker
   docker inspect $CID// CID: container ID. Command is used to container properties


Wordpress Installation
======================

Prerequisties
-------------
Working docker instance
working MySQL docker container

Installation Steps
-------------------

MySQL Container installation
----------------------------

Steps:
      docker run --name wordpressdb -e MYSQL_ROOT_PASSWORD=Password123 -d mysql:5.7// Command automatically donwload MYSQL image and container will be configured with parameters given. DB name will be wordpress and MySQL root password will be Password123
      docker exec -it wordpress  bash // MySQL command line interface

Wordpress installation
----------------------

1. Installation
Steps:
     docker pull wordpress // Download wordpress image 
     docker run --name wordpress --link wordpressdb:mysql -p 8080:80 -d wordpress // creating wordpress container  

2. Testing     
Steps:
     docker inspect $CID // Get the ip address of the containter to access wordpress
     elinks http://ip_addr:80 //Ellnks browser is command line browser  or use firefox from GUI to access the wordpress 

Completed
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Copyright 2016  Name of Rejul James


