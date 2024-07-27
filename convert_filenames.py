import os
import jaconv

# 현재 스크립트의 절대 경로를 얻습니다
SCRIPT_PATH = os.path.abspath(__file__)

# 현재 작업 디렉토리를 얻습니다
CURRENT_DIR = os.getcwd()

print(f"Processing files in: {CURRENT_DIR}")

# 현재 작업 디렉토리의 모든 파일을 가져옵니다
files = os.listdir(CURRENT_DIR)

for file in files:
    # 파일의 전체 경로를 얻습니다
    file_path = os.path.join(CURRENT_DIR, file)
    
    # 현재 스크립트 파일은 건너뜁니다
    if file_path == SCRIPT_PATH:
        print(f'Skipped: {file} (script file)')
        continue
    
    # 디렉토리는 건너뜁니다
    if os.path.isdir(file_path):
        print(f'Skipped: {file} (directory)')
        continue
    
    # 전각 문자를 반각 문자로 변환
    new_name = jaconv.z2h(file, kana=False, ascii=True, digit=True)
    
    # 파일 이름이 변경되었을 경우에만 이름 변경
    if file != new_name:
        new_path = os.path.join(CURRENT_DIR, new_name)
        try:
            os.rename(file_path, new_path)
            print(f'Renamed: {file} -> {new_name}')
        except OSError as e:
            print(f'Error renaming {file}: {e}')
    else:
        print(f'Skipped: {file} (no change needed)')

print("File processing complete.")