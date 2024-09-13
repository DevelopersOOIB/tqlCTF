from flask import Flask, request, render_template, send_file
from pyhtml2pdf import converter
import uuid
from io import BytesIO
import os



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        url = request.form['url']
        if not url:
            error = "URL is required!"
            return render_template('index.html', error=error)

        try:
            filename = './parsed/' + str(uuid.uuid4()) + ".pdf"
            converter.convert(url, filename)
            
            with open(filename, 'rb') as f:
                data = f.read()

            os.remove(filename)

            return send_file(BytesIO(data), download_name=filename)
        except Exception as e:
            print(e)
            error = "Unknown error!"
            return render_template('index.html', error=error)
    
'''    
    if request.method == 'POST':
        url = request.form['url']
        if not url:
            error = "URL is required!"
            return render_template('index.html', error=error)

        
        filename = '/app/SSRF/parsed/' + str(uuid.uuid4()) + ".pdf"
        converter.convert(url, filename)
            
        with open(filename, 'rb') as f:
            data = f.read()

        os.remove(filename)

        return send_file(BytesIO(data), download_name=filename)
        
'''





if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
