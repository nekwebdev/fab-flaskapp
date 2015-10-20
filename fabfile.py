from fabric.api import env, prompt, local, run

env.hosts = ['45.79.75.219']
env.user = 'flaskuser'

def deploy():
    local('git push production master')
    run('supervisorctl restart flaskapp')