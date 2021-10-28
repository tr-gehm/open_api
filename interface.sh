#!/bin/bash
if docker ps -a | grep clink2_autotest ;then
	docker ps -a | grep clink2_autotest | awk '{print $1}' | xargs docker stop
	docker ps -a | grep clink2_autotest | awk '{print $1}' | xargs docker rm
	echo "rm container success!!!!!!!!!!"
else
	echo "no container!!!!!!!!!!!!"
fi
if docker images | grep clink2_autotest; then	
	docker images | grep clink2_autotest | awk '{print $3}' | xargs docker rmi
	echo "rm inages seccess!!!!!!!!!!!"
else
	echo "no images!!!!!!!!!!!!!!!!!"
fi
echo "start build!!!!!!!!!!!!!!!!"
if docker build -t clink2_autotest .;then

	echo "build success!!!!!!!!!!!!1"
else
	echo "build fail!!!!!!!!!!!!"
fi
echo "make container!!!!!!!!!!!1"
docker run --name="clink2_autotest"  clink2_autotest
echo "complete!!!!!!!!!!!"
