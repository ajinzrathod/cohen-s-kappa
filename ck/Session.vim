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
edit api/serializers.py
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
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
let s:l = 9 - ((8 * winheight(0) + 9) / 18)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
9
normal! 09|
wincmd w
argglobal
if bufexists("api/views.py") | buffer api/views.py | else | edit api/views.py | endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 64 - ((16 * winheight(0) + 8) / 17)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
64
normal! 051|
wincmd w
2wincmd w
wincmd =
tabnext 1
badd +0 templates/terms-and-policy
badd +155 templates/terms-and-policy/terms-of-service.html
badd +127 templates/terms-and-policy/privacy-policy.html
badd +1 main/urls.py
badd +12 main/views.py
badd +53 ck/settings.py
badd +31 templates/account/login.html
badd +51 templates/account/login-form.html
badd +35 ck/urls.py
badd +16 templates/account/half-screen-bg-image.html
badd +120 templates/base/header.html
badd +17 main/context_processors.py
badd +6 tweet/urls.py
badd +13 tweet/views.py
badd +18 templates/tweets/index.html
badd +43 templates/widgets/searchBar-and-uploadFile.html
badd +4 tweet/models.py
badd +17 tweet/admin.py
badd +0 tweet/apps.py
badd +40 templates/widgets/searchBar-and-downloadButton.html
badd +8 api/urls.py
badd +62 api/views.py
badd +8 api/serializers.py
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
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
