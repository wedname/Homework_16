from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/generic')
def generic_page():
    return render_template('generic.html')


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
