from flask import Flask, request, render_template, render_template_string
import os
import base64
import re

app = Flask(__name__)


def filter_input(user_input):
    blacklist = ['config', 'os', 'import', 'eval', 'exec', 'getattr', 'setattr', 'delattr']
    for char in blacklist:
        user_input = user_input.replace(char, '')
    allowed_chars = re.compile(r'[^a-zA-Z0-9\s]')
    user_input = allowed_chars.sub('', user_input)

    return user_input


def decode_base32(encoded_str):
    try:
        decoded_bytes = base64.b32decode(encoded_str, casefold=True)
        return decoded_bytes.decode('utf-8')
    except Exception:
        return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    decoded_name = decode_base32(name)

    if decoded_name is None:
        safe_name = filter_input(name)
        response_header = safe_name
        response_body = safe_name
    else:
        safe_name = filter_input(decoded_name)
        if "{{" in decoded_name and "}}" in decoded_name:
            try:
                rendered_result = render_template_string(decoded_name)
                if rendered_result.strip() == os.environ['FLAG']:
                    response_header = "GOOD JOB :)"
                    response_body = os.environ['FLAG']
                else:
                    response_header = "TRY HARDER"
                    response_body = "TRY HARDER"
            except Exception:
                response_header = "TRY HARDER"
                response_body = "TRY HARDER"
        else:
            response_header = safe_name
            response_body = safe_name
    template = '''
    <h2>Report for {{ response_header }}</h2>
    <p>Dear {{ response_body }}, thank you for using our service.</p>
    '''

    return render_template_string(template, response_header=response_header, response_body=response_body)


if __name__ == '__main__':
    os.environ['FLAG'] = 'tqlCTF{ssti_explo1t3d_succ3ssfully}'
    app.run(host='0.0.0.0', port=5000)
