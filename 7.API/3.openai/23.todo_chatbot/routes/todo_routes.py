from flask import Blueprint, request, jsonify
todo_bp = Blueprint('todo', __name__)


# 내 메모 리스트 담을곳
todos = []
next_id = 1

# READ = todo 리스트 가져오기
@todo_bp.route('/api/todo', methods=['GET'])
def get_todos():
    return jsonify(todos)

# CREATE = todo 리스트 생성하기
@todo_bp.route('/api/todo', methods=['POST'])
def add_todo():
    global next_id
    
    # 1. 입력값 가져온다
    data = request.get_json()
    task = data.get('text')
    print('할일: ', task)
    # 2. 입력값 프로세싱 및 저장
    new_todo = {'id': next_id, 'task': task, 'done': False}
    todos.append(new_todo)
    next_id += 1
    # 3. 결과 반납
    return jsonify({'success': '성공적으로 추가됨'})

# UPDATE = todo 리스트 done/undone (toggle) 처리
@todo_bp.route('/api/todo/<int:todo_id>', methods=['PUT'])
def toggle_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['done'] = not todo['done']
            return jsonify({'success': f"ID: {todo_id} 를 {todo['done']} 처리 완료"})
            
    return jsonify({'error': '아직 구현안됨'})

# DELETE = todo 아이템 삭제하기
@todo_bp.route('/api/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
            return jsonify({'success': '성공적으로 삭제 완료'})
        
    return jsonify({'error': f'해당 항목이 없음 (ID: {todo_id}) '}), 404