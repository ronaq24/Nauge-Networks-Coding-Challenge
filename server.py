from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')
@app.route('/prob1')
def setup():
    return render_template('prob1.html')
@app.route('/prob2')
def setup2():
    return render_template('prob2.html')

if __name__ == '__main__':
    app.run()
