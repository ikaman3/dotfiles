" Configuration file for vim
set modelines=0		" CVE-2007-2438

" Normally we use vim-extensions. If you want true vi-compatibility
" remove change the following statements
set nocompatible	" Use Vim defaults instead of 100% vi compatibility
set backspace=2		" more powerful backspacing

" Don't write backup file if vim is being called by "crontab -e"
au BufWrite /private/tmp/crontab.* set nowritebackup nobackup
" Don't write backup file if vim is being called by "chpass"
au BufWrite /private/etc/pw.* set nowritebackup nobackup

" 문법이 존재한다면 문법 Highlight 켜기
if has("syntax")
    syntax on
endif

let skip_defaults_vim=1
set title
" Line number 보기
set nu 
" 자동 들여쓰기 시 #include 같은 전처리 구문을 판단하여 들여쓰기 하지 않음
set smartindent
" 괄호의 짝에 하이라이트하기
set showmatch
" 현재 커서 위치의 줄번호, 행번호 출력 
set ruler
set ts=4
set expandtab
set shiftwidth=4
" set hlsearch
set encoding=utf8
" syntax on
" let &titleold="Terminal"
