import os

#현재 디렉토리를 가져온다 cwd = current working directory
print("현재 작업 디렉토리는", os.getcwd())

new_directory = 'sesac1234'
os.mkdir(new_directory)
print("생성 완료")

os.chdir(new_directory)
print("이동 완료")

os.chdir("..") #.은 현재 디렉토리, ..은 부모 디렉토리
print("부모디렉토리로 이동완료")

os.rmdir(new_directory)
print("삭제 완료")

