# build image
docker build -t yara-platform .
# run container
docker run -v /home/sibctf/yara-platform/test/server:/usr/src/app --net=host -d --name=yara-platform-box yara-platform
# stop container
docker stop yara-platform-box
# remove container
docker rm yara-platform-box
# remove image
docker image rm --force yara-platform