#!/usr/bin/env python
# poetry export
# docker build
# docker stop
# docker run (bash, background mode)
# docker cp secrets.json

import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('cmd', type=str, nargs=argparse.REMAINDER, default='')
args = parser.parse_args()

DOCKER_OPTIONS = [
    ('--rm', ''),
    ('-it', ''),
    # background로 실행하는 옵션 추가
    ('-d', ''),
    ('-p', '8000:80'),
    ('--name', 'deploy-test'),
]
DOCKER_IMAGE_TAG = 'moonpeter/deploy-test'

# poetry export로 docker build시 사용할 requirements.txt작성
subprocess.run(f'poetry export -f requirements.txt > requirements.txt', shell=True)

# secrets.json이 없는 이미지를 build
subprocess.run(f'docker build -t {DOCKER_IMAGE_TAG} -f Dockerfile .', shell=True)

# 이미 실행되고 있는 name=instagram인 container를 종료
subprocess.run(f'docker stop deploy-test', shell=True)

# secrets.json이 없는 이미지를 docker run으로 bash를 daemon(background)모드로 실행
subprocess.run('docker run {options} {tag} /bin/bash'.format(
    options=' '.join([
        f'{key} {value}' for key, value in DOCKER_OPTIONS
    ]),
    tag=DOCKER_IMAGE_TAG,
), shell=True)

# secrets.json을 name=instagram인 container에 전송
subprocess.run('docker cp secrets.json deploy-test:/srv/deploy-test', shell=True)

# collectstatic을 subprocess.run()을 사용해서 실행
subprocess.run('docker exec deploy-test python manage.py collectstatic --noinput', shell=True)

# 실행중인 name=instagram인 container에서 argparse로 입력받은 cmd또는 bash를 실행(foreground 모드)
subprocess.run('docker exec -it deploy-test {cmd}'.format(
    cmd=' '.join(args.cmd) if args.cmd else 'supervisord -c ../.config/supervisord.conf -n'
), shell=True)