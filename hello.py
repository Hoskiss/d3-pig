#from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('pig.html')

@app.route("/example/")
def example():
    return render_template('example.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)