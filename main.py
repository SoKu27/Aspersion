from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder="static")

@app.route('/')
def hello_world():
    return render_template('front.html')

@app.route('/Sonny')
def Sonny():
    return render_template('Sonny.html')

@app.route('/Peter')
def Peter():
    return render_template('Peter.html')

@app.route('/Jimmy')
def Jimmy():
    return render_template('Jimmy.html')

@app.route('/Chase')
def Chase():
    return render_template('Chase.html')

@app.route('/merch')
def merch():
    return render_template('merch.html')


if __name__ == '__main__':
    app.run(port=8000)