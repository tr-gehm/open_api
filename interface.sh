#!/bin/bash -ilex
if docker ps -a | grep clink2_autotest$1 ;then
	docker ps -a | grep clink2_autotest$1 | awk '{print $1}' | xargs docker stop
	docker ps -a | grep clink2_autotest$1 | awk '{print $1}' | xargs docker rm
	echo "rm container success!!!!!!!!!!"
else
	echo "no container!!!!!!!!!!!!"
fi
if docker images | grep clink2_autotest$1; then
	docker images | grep clink2_autotest$1 | awk '{print $3}' | xargs docker rmi
	echo "rm inages seccess!!!!!!!!!!!"
else
	echo "no images!!!!!!!!!!!!!!!!!"
fi
echo "start build!!!!!!!!!!!!!!!!"
if docker build -t clink2_autotest$1 . -f $1;then

	echo "build success!!!!!!!!!!!!1"
else
	echo "build fail!!!!!!!!!!!!"
fi
echo "make container!!!!!!!!!!!1"
#docker run --name="clink2_autotest"  clink2_autotest
docker run  -v /var/lib/jenkins/workspace/api_demo:/usr/src/clink2_autotest$1/ --name clink2_autotest$1  clink2_autotest$1
echo "complete!!!!!!!!!!!"
