from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Nattphon!'

@app.route('/Id')
def Id():
    return '654272103'

@app.route('/name')
def name():
    return 'Nattphon Taotong'

@app.route('/university')
def university():
    return 'Phetchaburi Rajabhat University'

if __name__ == '__main__':
    app.run(debug=True)