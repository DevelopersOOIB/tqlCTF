from flask import Flask, render_template, session, request, redirect
import database
import os
import uuid


app = Flask(__name__)
app.secret_key = "93a0aac1-e458-4f2d-aa42-e947c17b0c82"
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024


#def check_user_is_auth(session):
#    if "user_id" not in session:
#        return redirect('/logout')
#    if not database.
# tqlCTF{1ns3cur3_p@ssw0rd_ch4ng3_funct10n}

@app.route('/', methods=['GET'])
def main():
    if "user_id" in session:
        return redirect('/home')
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if "user_id" in session:
        return redirect('/home')
    
    if request.method == 'GET':
        return render_template('login.html')
    
    login = request.form['login']
    password = request.form['password']

    if not (login and password):
        error = "Login and password are required!"
        return render_template('login.html', error=error)
    user = database.login(login, password)

    if user:
        session["user_id"] = user[0]
        return redirect('/home')

    error = "Incorrect login or password" 
    return render_template('login.html', error=error)


@app.route('/logout', methods=['GET'])
def logout():
    if 'user_id' in session:
        session.pop('user_id')
    return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if "user_id" in session:
        return redirect('/')
    
    if request.method == 'GET':
        return render_template('/register.html')
    
    if request.method == 'POST':    
        login = request.form['login']
        password = request.form['password']
        
        if not (login and password):
            error = "Login and password are required!"
            return render_template('register.html', error=error)
        
        if database.register(login, password):
            user = database.login(login, password)
            session["user_id"] = user[0]
            return redirect('/home')
        
        error = "Login already taken"
        return render_template('register.html', error=error)


@app.route('/change_pass', methods=['GET', 'POST'])
def change_pass():
    if 'user_id' not in session:
        return redirect('/')
    
    username = database.get_username_by_id(session["user_id"])
    if not username:
        return redirect('/')

    username = username[1]

    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        if not (login and password):
            error = "All fields are required!"
            return render_template('change_password.html', error=error, username=username)

        if not database.check_login(login):
            error = "All fields are required!"
            return render_template('change_password.html', error=error, username=username)
        
        database.change_pass(login, password)
        success = "Password has been changed"

        return render_template('change_password.html', success=success, username=username)

    return render_template('change_password.html', username=username)


@app.route('/home', methods=['GET'])
def home():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('home.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'user_id' not in session:
        return redirect('/')
    
    if request.method == 'POST':
        uploaded_file = request.files["file"]

        if uploaded_file.filename == "":
            error="File not selected"
            return render_template('upload.html', error=error)

        file_ext = os.path.splitext(uploaded_file.filename)[1]
        
        if file_ext not in ['.jpg', '.png', '.jpeg']:
            error = "Restricted extention"
            return render_template('upload.html', error=error)
        
        new_filename = str(uuid.uuid4()) + file_ext
        uploaded_file.save('./static/uploads/' + new_filename)

        success = "File has been uploaded"
        file_url = '/static/uploads/' + new_filename

        database.add_uploaded_file(session["user_id"], file_url)

        return render_template('upload.html', success=success, file_url=file_url)

    return render_template('upload.html')
    

@app.route('/galery', methods=['GET'])
def galery():
    if 'user_id' not in session:
        return redirect('/')
    
    uploads = database.get_uploads_by_user_id(session['user_id'])

    return render_template('galery.html', uploads=uploads)


if __name__ == '__main__':
    database.create_database()
    app.run(debug=False, host="0.0.0.0")