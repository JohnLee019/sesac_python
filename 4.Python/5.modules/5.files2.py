import os
import zipfile
#빌트인 모듈중에 zip으로 압축해주는 기능이 있음

my_dir = 'sesac1234'

#디렉토리 안에 파일'만' 읽어오기
for filename in os.listdir(my_dir):
    file_path = os.path.join(my_dir, filename)
    if (os.path.isfile(file_path)):
        #print(filename)
        # 해당 파일을 압축하기
        zip_filename = f"{file_path}.zip"

        #zip으로 압축하기 
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            zipf.write(file_path, arcname=filename)
            print(f"{filename} 을 {zip_filename}으로 압축 완료함")

        #원본 파일 삭제
        os.remove(file_path)
        print(f"원본 파일 삭제")