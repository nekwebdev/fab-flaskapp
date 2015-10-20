Sample empty Flask project for a Debian 8.1 server provisioned by this Fabric script: https://github.com/nekwebdev/fab-debian81

How to deploy and run locally:

```
git clone git@github.com:nekwebdev/fab-flaskapp.git myapp
cd myapp
virtualenv venv
source venv/bin/activate
pip install -r requirements
gunicorn wsgi_gunicorn:app -b localhost:8000
```

Once you want to push to the server:

`fab deploy`