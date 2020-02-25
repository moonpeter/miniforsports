#!/usr/bin/env sh
IDENTITY_FILE="$HOME/.ssh/wps12th.pem"
USER="ubuntu"
HOST="54.180.89.136"
TARGET=${USER}@${HOST}
ORIGIN_SOURCE="$HOME/projects/wps12/selfstudy/django/deploy-test/"
DEST_SOURCE="/home/ubuntu/projects/"
SSH_CMD="ssh -i ${IDENTITY_FILE} ${TARGET}"

echo "===== runserver 배포 ====="

# 서버 초기설정
echo " ### apt update & upgrade & autoremove"
${SSH_CMD} -C 'sudo apt udpate && sodo DEBIAN_FRONTEND=noninteractiv apt dist-upgrade -y && apt -y autoremove'
echo " ### apt install python3-pip"
${SSH_CMD} -C 'sudo apt -y install python3-pip'

# pip freeze
echo " ### pip freeze"
"$HOME"/.pyenv/versions/3.7.4/envs/deploy-test/bin/pip freeze > "$HOME"/projects/wps12/selfstudy/django/deploy-test/requirements.txt

# 기존 폴더 삭제
echo " ### remove server source"
${SSH_CMD} sudo rm -rf ${DEST_SOURCE}

# 로컬에 있는 파일 업로드
echo " ### upload local source"
${SSH_CMD} mkdir -p ${DEST_SOURCE}
scp -q -i "${IDENTITY_FILE}" -r "${ORIGIN_SOURCE}" ${TARGET}:${DEST_SOURCE}

# pip install
echo " ### pip install"
${SSH_CMD} pip3 install -q -r /home/ubuntu/projects/deploy-test/requirements.txt

# screen sttings
echo " ### screen settings"
# 실행중이던 screen 세션 종료
${SSH_CMD} -C 'screen -X -S runserver quit'
# screen 실행
${SSH_CMD} -C 'screen -S runserver -d -m'
#실행중인 세션에 명령어 전달
${SSH_CMD} -C "screen -R runserver -X stuff 'sudo python3 /home/ubuntu/projects/deploy-test/app/manage.py runserver 0:80\n'"

echo "===== finish 배포 ====="