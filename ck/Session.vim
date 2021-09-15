let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Documents/git/personal/cohen-s-kappa/ck
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
edit assets/js/tweet-response.js
set splitbelow splitright
wincmd _ | wincmd |
split
wincmd _ | wincmd |
split
wincmd _ | wincmd |
split
3wincmd k
wincmd w
wincmd w
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
wincmd =
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 237 - ((4 * winheight(0) + 4) / 8)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
237
normal! 035|
wincmd w
argglobal
if bufexists("assets/js/compare-users.js") | buffer assets/js/compare-users.js | else | edit assets/js/compare-users.js | endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 9 - ((4 * winheight(0) + 4) / 8)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
9
normal! 013|
wincmd w
argglobal
if bufexists("assets/css/ck.css") | buffer assets/css/ck.css | else | edit assets/css/ck.css | endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 346 - ((5 * winheight(0) + 4) / 9)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
346
normal! 018|
wincmd w
argglobal
if bufexists("templates/compare/index.html") | buffer templates/compare/index.html | else | edit templates/compare/index.html | endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 35 - ((3 * winheight(0) + 4) / 8)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
35
normal! 037|
wincmd w
2wincmd w
wincmd =
tabnext 1
badd +8 compare/views.py
badd +24 templates/compare/index.html
badd +1 templates/widgets/pagination.html
badd +69 tweet/views.py
badd +8 templates/tweets/index.html
badd +47 templates/base/header.html
badd +7 tweet/templatetags/tweet_extras.py
badd +1 templates/base.html
badd +51 ck/urls.py
badd +335 assets/css/ck.css
badd +2 compare/decorators.py
badd +9 main/context_processors.py
badd +26 main/views.py
badd +11 main/urls.py
badd +5 compare/urls.py
badd +23 templates/error-pages/error-403.html
badd +21 templates/error-pages/error-404.html
badd +21 templates/error-pages/error-500.html
badd +92 templates/home.html
badd +36 assets/js/compare-users.js
badd +167 assets/js/tweet-response.js
badd +23 api/serializers.py
badd +3 tweet/models.py
badd +298 api/views.py
badd +20 api/urls.py
badd +331 ~/Documents/git/personal/cohen-s-kappa/venv/lib/python3.8/site-packages/django/contrib/auth/models.py
badd +0 ~/Documents/git/personal/cohen-s-kappa/venv/lib/python3.8/site-packages/django/contrib/auth/signals.py
badd +117 ~/Documents/git/personal/cohen-s-kappa/venv/lib/python3.8/site-packages/django/contrib/auth/tokens.py
badd +0 ~/Documents/git/personal/cohen-s-kappa/venv/lib/python3.8/site-packages/django/contrib/auth/validators.py
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOS
set winminheight=1 winminwidth=1
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
