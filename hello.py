from flask import Flask, url_for, redirect, render_template
app = Flask(__name__,'')
app.debug = True

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
