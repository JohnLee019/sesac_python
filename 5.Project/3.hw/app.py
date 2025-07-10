from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_FILE_EXT = {'png', 'jpg', 'jpeg', 'gif'}

# 파일명과 키워드를 저장하는 딕셔너리
file_keywords = {}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_EXT

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files, file_keywords=file_keywords)

@app.route('/index', methods=['POST'])
def upload_file():
    file = request.files['file']
    keyword = request.form.get('keyword')

    if file.filename == '':
        return '파일이 올바르게 전송되지 않았습니다'

    if allowed_file(file.filename):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        file_keywords[file.filename] = keyword  # 업로드 시 키워드 저장
        return redirect(url_for('index'))
    else:
        return '허용되지 않는 파일입니다.'

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/update/<filename>', methods=['POST'])
def update_keyword(filename):
    keyword = request.form.get('keyword')
    file_keywords[filename] = keyword
    return redirect(url_for('index'))

@app.route('/delete/<filename>')
def delete_file(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        file_keywords.pop(filename, None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
