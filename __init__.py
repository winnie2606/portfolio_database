from flask import Flask
from flask import Flask, render_template


SoftDev = Flask(__name__)

@SoftDev.route('/')


def main():
    return render_template('index.html')
if __name__ == "__main__":
    SoftDev.run()
