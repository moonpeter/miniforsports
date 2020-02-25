#!/usr/bin/env sh
IDENTITY_FILE="$HOME/.ssh/wps12th.pem"
USER="ubuntu"
HOST="54.180.89.136"
TARGET=${USER}@${HOST}
ORIGIN_SOURCE="$HOME/projects/wps12/selfstudy/django/deploy-test/"
DOCKER_REPO="moonpeter/deploy-test"
SSH_CMD="ssh -i ${IDENTITY_FILE} ${TARGET}"

echo "===== Docker 배포 ====="

# 서버 초기설정
echo " ### apt update & upgrade & autoremove"
${SSH_CMD} -C 'sudo apt udpate && sodo DEBIAN_FRONTEND=noninteractiv apt dist-upgrade -y && sudo apt -y autoremove'
echo " ### apt install docker.io"
${SSH_CMD} -C 'sudo apt -y install docker.io'

echo " ### poetry export"
poetry export -f requirements.txt > requirements.txt

# docker build
echo " ### docker build"
docker build -q -t ${DOCKER_REPO} -f Dockerfile "${ORIGIN_SOURCE}"

# docker push
echo " ### docker push"
docker push ${DOCKER_REPO}

echo " ### docker stop"
${SSH_CMD} -C "sudo docker stop deploy-test"

echo " ### docker pull"
${SSH_CMD} -C "sudo docker pull ${DOCKER_REPO}"

# 로컬의 aws profile을 전달

# screen에서 docker run
echo "screen settings"
# 실행중이던 screen 세션 종료
${SSH_CMD} -C 'screen -X -S docker quit'
# screen 실행
${SSH_CMD} -C 'screen -S docker -d -m'
# 실행중인 screen에서 docker container 를 사용해서 bash 실행
${SSH_CMD} -C "screen -R docker -X stuff 'sudo docker run --rm -it -p 80:8000 --name=deploy-test moonpeter/deploy-test /bin/bash\n'"

# bash를 실행중인 container에 HOST의 ~/.aws폴더를 폭사

# container에서 bash를 실행중인 screen에 runserver 명령어를 전달
${SSH_CMD} -C "screen -r docker -X stuff 'python manage.py runserver 0:8000\n'"


echo "===== finish 배포 ====="