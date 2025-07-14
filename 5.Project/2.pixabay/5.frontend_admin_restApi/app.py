from flask import Flask, jsonify, redirect, url_for, send_from_directory, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_FILE_EXT = {'png', 'jpg', 'jpeg', 'gif', 'png'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 글로벌 변수
images = [
    {"filename":"dog1.jpg", "keywords": ["dog", "animal", "cute"]},
    {"filename":"dog2.jpg", "keywords": ["dog", "pet", "cute"]},
    {"filename":"dog3.jpg", "keywords": ["dog", "kitty", "cute"]},
]

def allowed_file_pythonic(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_EXT

@app.route('/api/search')
def search():
    query = request.args.get("q", "").lower()
    results = []
    
    for item in images:
        # pythonic하게 한줄로...
        if any(query in keyword for keyword in item["keywords"]):
            image_url = url_for('static', filename=f'img/{item["filename"]}')
            results.append(image_url)
    return jsonify({"url": results})

@app.route('/')
def index():
    return send_from_directory("index.html")

@app.route('/admin')
def admin():
    return send_from_directory("admin.html")

@app.route('/api/upload', methods=['POST'])
def upload():
    file = request.files.get('image')
    keywords = request.form.get('keywords')
    print(keywords)
    
    if file:
        filename = file.filename
        filepath = os.path.join('static', 'img', filename)
        file.save(filepath)
        images.append({'filename': filename, "keywords": keywords.lower().split(',')})
    
    return redirect(url_for('admin'))

@app.route('/api/modify/<filename>', methods=['POST'])
def update_keywords(filename):
    new_keywords = request.form.get('keywords')
    for i in images:
        if i["filename"] == filename:
            i["keywords"] = [word.strip() for word in new_keywords.lower().split(',') if len(word.strip())]
            break
        
    return redirect(url_for('admin'))

@app.route('/api/delete/<filename>')
def delete_image(filename):

    # 실제로 이미지를 지울거면??
    filepath = os.path.join('static', 'img', filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    
    return redirect(url_for('admin'))

if __name__ == "__main__":
    app.run(debug=True)
    