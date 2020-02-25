#!/usr/bin/env python
# 도커 이미지에 secrets.json이 포함
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('cmd', type=str, nargs=argparse.REMAINDER, default='')
args = parser.parse_args()

DOCKER_OPTIONS = [
    ('--rm', ''),
    ('-it', ''),
    ('-d', ''),
    ('-p', '8001:80'),
    ('--name', 'deploy-test'),
]
DOCKER_IMAGE_TAG = 'moonpeter/deploy-test'

subprocess.run(f'poetry export -f requirements.txt > requirements.txt', shell=True)
subprocess.run(f'docker build -t {DOCKER_IMAGE_TAG} -f Dockerfile .', shell=True)
subprocess.run(f'docker stop deploy-test', shell=True)
subprocess.run('docker run -d {options} {tag} /bin/bash'.format(
    options=' '.join([
        f'{key} {value}' for key, value in DOCKER_OPTIONS
    ]),
    tag=DOCKER_IMAGE_TAG,
), shell=True)
subprocess.run(f'docker cp secrets.json deploy-test:/srv/deploy-test', shell=True)

# 실행중인 name=instagram인 container에서 argparse로 입력받은 cmd또는 bash를 실행(foreground 모드)
subprocess.run('docker exec -it deploy-test {cmd}'.format(
    cmd=' '.join(args.cmd) if args.cmd else 'supervisord -c ../.config/local_dev/supervisord.conf -n'
), shell=True)