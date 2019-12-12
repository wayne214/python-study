from flask import Flask

app = Flask(__name__)  # 创建一个应用


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run()
