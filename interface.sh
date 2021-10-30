#!/bin/bash -ilex
if docker ps -a | grep clink2_autotest_$1 ;then
        docker ps -a | grep clink2_autotest_$1 | awk '{print $1}' | xargs docker stop
        docker ps -a | grep clink2_autotest_$1 | awk '{print $1}' | xargs docker rm
        echo "#######################rm container success#######################"
else
        echo "#######################no container#######################"
fi
if docker images | grep clink2_autotest_$1; then
        docker images | grep clink2_autotest_$1 | awk '{print $3}' | xargs docker rmi
        echo "#######################rm inages seccess#######################"
else
        echo "#######################no images#######################"
fi
sed -i "s/\${cases}/$1/g" Dockerfile
echo "start build!!!!!!!!!!!!!!!!"
if docker build -t clink2_autotest_$1 .;then

        echo "#######################build success#######################"
else
        echo "#######################build fail#######################"
        sed -i "s/$1/\${cases}/g" Dockerfile
        exit 1
fi
echo "##########################make container###########################"
#docker run --name="clink2_autotest"  clink2_autotest
if docker run  -v /var/lib/jenkins/workspace/api_demo:/usr/src/clink2_autotest_$1/ --name clink2_autotest_$1  clink2_autotest_$1; then
    echo "#######################complete##########################"
    sed -i "s/$1/\${cases}/g" Dockerfile

else
    echo "#######################container fail#######################"
fi
sed -i "s/$1/\${cases}/g" Dockerfile
