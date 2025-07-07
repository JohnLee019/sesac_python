#pip install flask
#ctrl + 클릭해서 밑줄 만들고 들어가고 그리고 나서 Alt + 왼쪽화살표에서 나오기
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, Flask!<h1>"

if __name__ == '__main__':
    print("여기가 메인 함수")
    app.run()