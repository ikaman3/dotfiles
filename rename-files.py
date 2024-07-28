import os

def rename_files_in_folders(root_dir, old_filename, new_filename):
    print(f"Starting file renaming process in: {root_dir}")
    renamed_count = 0
    error_count = 0

    # 루트 디렉토리의 모든 하위 디렉토리를 순회합니다
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # 각 디렉토리에서 old_filename 파일을 찾습니다
        if old_filename in filenames:
            old_file = os.path.join(dirpath, old_filename)
            new_file = os.path.join(dirpath, new_filename)
            
            try:
                os.rename(old_file, new_file)
                print(f"Renamed in {os.path.relpath(dirpath, root_dir)}: {old_filename} -> {new_filename}")
                renamed_count += 1
            except OSError as e:
                print(f"Error renaming file in {os.path.relpath(dirpath, root_dir)}: {e}")
                error_count += 1

    print(f"\nProcess completed.")
    print(f"Total files renamed: {renamed_count}")
    print(f"Total errors encountered: {error_count}")

# 스크립트가 실행되는 현재 디렉토리를 얻습니다
current_dir = os.getcwd()

# 바꾸려는 파일 이름과 바꾸고 싶은 파일 이름을 변수로 정의합니다
old_filename = '0_.jpg'
new_filename = '0.jpg'

# 현재 디렉토리에서 파일 이름 변경 프로세스를 시작합니다
rename_files_in_folders(current_dir, old_filename, new_filename)