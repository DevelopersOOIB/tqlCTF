from os import unlink
import subprocess
import tempfile
from flask import Flask, request, send_file, abort, render_template, redirect, url_for

YARA_BIN = "/usr/bin/yara" # your path to yara scanner

FLAG = ("tqlCTF{y4r4_c00l_1n57rum3n7}", "tqlCTF{y4r4_15_1mm0r74l_4nd_1ncr3d1bl3}", "tqlCTF{y4r4_15_c00l_pr0f35510n4l_1n57rum3n7_f0r_4ny_745k5}")
GOODMAX = (4,7,200)

app = Flask(__name__)

@app.get('/BlenderPro-Medium.woff2')
def font_get():
    return send_file('BlenderPro-Medium.woff2')

@app.get('/task/<int:task_id>/sample')
def sample_get(task_id):
    return send_file(f'task{task_id}.zip')

@app.route('/')
def hello():
    return redirect('/task/1')

@app.get('/task/<int:task_id>')
def task1_get(task_id):
    if task_id in [1,2,3]:
        return send_file(f'./tasks/task{task_id}.html')
    else:
        abort(404)

@app.post('/task/<int:task_id>')
def task_handler(task_id):
    if len(request.form['yara_rule']) > 10000:
        abort(413)
    raw_user_rule = request.form['yara_rule']#.replace('\r','')
    if raw_user_rule.count('rule ') > 1:
        return render_template('error.html', task_id=task_id, yara_rule=raw_user_rule, error_text="Разрешается только одно Yara правило!")
    if 'import ' in raw_user_rule:
        return render_template('error.html', task_id=task_id, yara_rule=raw_user_rule, error_text="Используйте правила без модулей!")
    tmp = tempfile.NamedTemporaryFile(delete=False)
    with open(tmp.name, 'w') as f:
        f.write(raw_user_rule)
    #valid rule has good syntax, one defined rule only and generates no warnings
    good_yara_process = subprocess.Popen(f"{YARA_BIN} --fail-on-warnings -a 30 {tmp.name} ./collection/task{task_id}/good", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    good_yara_result, _ = good_yara_process.communicate()
    #print(good_yara_result.decode("utf-8"))
    good_yara_process.kill()
    bad_yara_process = subprocess.Popen(f"{YARA_BIN} --fail-on-warnings -a 30 {tmp.name} ./collection/task{task_id}/bad", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    bad_yara_result, yara_error = bad_yara_process.communicate()
    #print(bad_yara_result.decode("utf-8"))
    bad_yara_process.kill()
    tmp.close()
    unlink(tmp.name)
    if not yara_error == b'':
        return render_template('error.html', task_id=task_id, yara_rule=raw_user_rule, error_text=yara_error.decode("utf-8"))
    good_hits = good_yara_result.decode("utf-8").count('\n')
    bad_hits = bad_yara_result.decode("utf-8").count('\n')
    if bad_hits == 200 and good_hits == 0:
        flag=FLAG[task_id-1]
    else:
        flag=""
    return render_template('result.html', task_id=task_id, yara_rule=raw_user_rule, good_hits=good_hits, good_max=GOODMAX[task_id-1], bad_hits=bad_hits, flag=flag)