import os
import shutil

def rename_and_move_pdfs(root_dir):
    # 현재 디렉토리의 모든 하위 디렉토리를 순회합니다
    for dir_name in os.listdir(root_dir):
        dir_path = os.path.join(root_dir, dir_name)
        
        # 디렉토리인지 확인
        if os.path.isdir(dir_path):
            # 디렉토리 내의 PDF 파일 찾기
            pdf_files = [f for f in os.listdir(dir_path) if f.lower().endswith('.pdf')]
            
            if pdf_files:
                # 첫 번째 PDF 파일 선택
                pdf_file = pdf_files[0]
                old_file_path = os.path.join(dir_path, pdf_file)
                
                # 새 파일 이름 생성
                new_file_name = f"{dir_name}.pdf"
                new_file_path = os.path.join(root_dir, new_file_name)
                
                # 파일 이동 및 이름 변경
                shutil.move(old_file_path, new_file_path)
                print(f"Moved and renamed: {old_file_path} -> {new_file_path}")
            else:
                print(f"No PDF file found in {dir_name}")

    print("Process completed.")

# 현재 디렉토리 경로
current_dir = os.getcwd()

# PDF 파일 이름 변경 및 이동
rename_and_move_pdfs(current_dir)