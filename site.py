from flask import Flask, url_for, redirect, render_template
app = Flask(__name__,'')
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/mics')
def mics():
    return render_template('mics.html')

@app.route('/post')
def post():
    return render_template('post.html')

if __name__ == '__main__':
    app.run()
