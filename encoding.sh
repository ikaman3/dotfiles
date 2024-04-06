#!/bin/zsh

targetPath=~/Movies/encoded
desktopPath=~/Desktop

# 중간에 강제로 종료할 경우 "0" 파일이 남는데 그거 지우는 함수
rm0File() {
	if [ $(find ~ -maxdepth 1 -name "0") ]
	then
		rm ~/0
	fi
}

# 파일이 존재하는지 확인 후 작업 여부 결정
find $desktopPath -maxdepth 1 -name "*.mp4" -o -name "*.mov"
if [ -e "${desktopPath}/*.mp4" -o "${desktopPath}/*.mov" ]
then
	fileCount=$(find $desktopPath -maxdepth 1 -name "*.mp4" -o -name "*.mov" | wc -l | tr -d \ )
	echo "총 파일 개수: ${fileCount}"
	# -n: Built-in echo와 /bin/echo 명령어가 달라서 생기는 문제 같다.
	printf "작업을 진행합니까? (y/n)> "
	read YorN 
	# 변수값이 비어버릴 경우 문법에 의해 조건식이 성립될 수 없어 "[: too many arguments" 에러가 발생, 변수를 ""로 묶을 것
	if [ "$YorN" = "n" -o "$YorN" = "N" ]
	then
		echo "작업을 종료했습니다."
		exit 0
	fi

	# 파일 개수만큼 인코딩 반복
	videoArray=$(find $desktopPath -maxdepth 1 -name "*.mp4" -o -name "*.mov")
	count=0 # 작업 횟수 확인용 변수
	for filename in $videoArray
	do
		title=$(echo $filename | cut -d "/" -f 5 | cut -d "." -f 1)
		
		let count++
		ffmpeg -i "${filename}" -s 1920x1080 -c:v libx265 -tag:v hvc1 "${targetPath}/${title}.mp4" \
		&& mv "${filename}" ~/.Trash/
	done
	echo "총 작업 횟수: $count"
	echo "작업 종료."
	rm0File
	exit 0
else
	echo "작업할 파일 없음!!!"
	rm0File
	exit 0
fi
