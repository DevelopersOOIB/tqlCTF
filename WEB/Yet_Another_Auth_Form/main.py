from flask import Flask, render_template, request
import sqlite3
import hashlib

app = Flask(__name__)
app.db_name = "authbypass.db"
app.password = "SuperStrongSecretAdminPa$$w0rd"  # hash in DB from this one


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', code="404", reason="Not Found"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html', code="500", reason="Internal Server Error"), 500


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/authbypass", methods=['GET', 'POST'])
def authbypass():
    if request.method == "GET":
        return render_template("login.html")
    else:
        con = sqlite3.connect(app.db_name)  # connect to db
        cur = con.cursor()
        username = request.form.get('username')  # get username from POST body
        password = request.form.get('password')  # get password from POST body
        form_pass_hash = hashlib.md5(password.encode())  # encode pass and get MD5
        printable_hash = form_pass_hash.hexdigest()  # get HEX hash of password
        result = cur.execute(f"SELECT * FROM users WHERE username='{username}' and  hash='{printable_hash}'")
        # select all data from DB with username from POST request
        creds = result.fetchall()  # type result to creds variable
        print(f"Result from DB: {creds}")
        if creds:
            print(f"Username from DB: {creds[0][1]}")  # username
            print(f"Password hash in MD5 from DB: {creds[0][2]}")  # pass hash
            print(form_pass_hash.hexdigest())
            if creds[0][2] == printable_hash:
                return render_template("flag.html", message="Well done!", flag="tqlCTF{C7F_l1k3_SQL1_4u7h_byp455}")
            else:
                return render_template("profile.html", name=creds[0][1])
        else:
            return render_template("login.html", error_message="Invalid credentials")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
