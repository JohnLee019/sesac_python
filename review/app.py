from flask import Flask, render_template, request
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    items_per_page = 10

    return render_template('index.html', stores=stores)


if __name__ == '__main__':
    app.run(debug=True)