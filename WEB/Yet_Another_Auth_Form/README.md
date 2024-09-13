# SQLi Auth Bypass
Application to test you SQLi auth bypass skills
---
This is a simple lab that demonstrates a slightly non-standard way of authorization in a web application.

I was inspired to create this app by the hint in the task "Bypass from the back" from the WAPT CODEBY course, and I was really interested in implementing a similar authorization mechanism.

The application is written in Python using the Flask web framework.
To run the application on your own, follow these steps:
```bash
git clone https://github.com/cherepawwka/SQLi_Auth_Bypass.git
cd SQLi_Auth_Bypass
pip install flask
python3 main.py
```
or if you prefer to run app in docker:
```bash
git clone https://github.com/cherepawwka/SQLi_Auth_Bypass.git
cd SQLi_Auth_Bypass
docker build . -t sqliauthbypass
docker run -d -p 5000:5000 sqliauthbypass:latest
```
Now your app is running at http://127.0.0.1:5000/

To stop container
```bash
docker ps -a  # get ID
docker stop ID
```

Enjoy!
---
The way to bypass authorization will be clear after analyzing the source code.

To facilitate the task, I have already placed the prepared database in the repository and added a password into source code, relative to which the hash from the database was calculated.

Maybe [this repo](https://github.com/carlospolop/hacktricks/blob/master/pentesting-web/login-bypass/sql-login-bypass.md) will help you to find payload.


The finished payload can be posted later😊
