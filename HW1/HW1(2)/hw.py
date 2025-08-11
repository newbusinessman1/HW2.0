#1 ДЗ

#Найти ошибку в коде

from flask import Flask

app = Flask(__name__)

@app.route('/')  #ошибка была здесь вместо (") нужно сделать правельную машрутизацию через ('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()


