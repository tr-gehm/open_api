#!/bin/bash -ilex
sed -i 's/${cases}/$1/g' call_success
if docker ps -a | grep clink2_autotest_$1 ;then
        docker ps -a | grep clink2_autotest_$1 | awk '{print $1}' | xargs docker stop
        docker ps -a | grep clink2_autotest_$1 | awk '{print $1}' | xargs docker rm
        echo "#######################rm container success#######################"
else
        echo "#######################no container#######################"：
fi
if docker images | grep clink2_autotest_$1; then
        docker images | grep clink2_autotest_$1 | awk '{print $3}' | xargs docker rmi
        echo "#######################rm inages seccess#######################"
else
        echo "#######################no images#######################"
fi
echo "start build!!!!!!!!!!!!!!!!"
if docker build -t clink2_autotest_$1 . -f $1;then

        echo "#######################build success#######################"
else
        echo "#######################build fail#######################"
        sed -i 's/$1/${cases}/g' call_success
        exit 1
fi
echo "make container!!!!!!!!!!!1"
#docker run --name="clink2_autotest"  clink2_autotest
if docker run  -v /var/lib/jenkins/workspace/api_demo:/usr/src/clink2_autotest_$1/ --name clink2_autotest_$1  clink2_autotest_$1; then
    echo "#######################complete##########################"
    sed -i 's/$1/${cases}/g' call_success

else
    echo "#######################container fail#######################"
sed -i 's/$1/${cases}/g' call_success
