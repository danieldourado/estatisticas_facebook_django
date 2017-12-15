from subprocess import call

call("sudo service postgresql start", shell=True)
call("python manage.py runserver $IP:$PORT", shell=True)
