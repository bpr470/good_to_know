mkdir .vim
echo "
set shell=/bin/bash

packloadall

syntax on

let g:airline#extensions#tabline#enabled = 1
let g:airline_theme = 'solarized'
set laststatus=2
set noshowmode
set ruler
set number

devicons
set encoding=utf8
set guifont=Meslo\ LG\ M\ DZ\ Regular\ for\ Powerline\ Nerd\ Font\ Complete\:h18
" > /.vimrc
cd .vim
mkdir pack
cd pack
mkdir bundle
cd bundle
mkdir start
cd start
git clone git@github.com:preservim/nerdtree.git
git clone git@github.com:altercation/vim-colors-solarized.git
git clone git@github.com:vim-airline/vim-airline.git
git clone git@github.com:vim-airline/vim-airline-themes.git

