#!/bin/zsh

# 업그레이드 가능한 패키지 리스트 가져오기
outdated_packages=$(brew outdated -g)

# 리스트에서 microsoft로 시작하는 패키지 제외
filtered_packages=$(printf "%s" "${outdated_packages}" | grep -v "^microsoft")

# 패키지 업그레이드 실행
if [ -n "${filtered_packages}" ]; then
    brew upgrade ${filtered_packages}
else
    printf "%s" "업그레이드할 패키지가 없음."
fi
