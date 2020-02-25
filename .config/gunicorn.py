daemon = False
chdir = '/srv/deploy-test/app'
bind = 'unix:/run/deploy-test.sock'
accesslog = '/var/log/gunicorn/deploy-test-access.log'
errorlog = '/var/log/gunicorn/deploy-test-error.log'
capture_output = True
