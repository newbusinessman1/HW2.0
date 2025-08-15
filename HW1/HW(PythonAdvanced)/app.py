from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello Flask!'

@app.route('/user/<name>')
def user(name):
    return f'Hello, {name}!'


if __name__ == '__main__':
    app.run(port=3000, debug=True, host='localhost')


print(f"" split=".")