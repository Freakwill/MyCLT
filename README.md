# MyScripts
My useful and powerful scripts (in Python).

## scripts

### jpg2eps
transform .jpg to .eps

-f FromWhat.j(e)pg -t ToWhat.eps


### send_mail
send a file or send a folder (compressed before sending)

send_mail.py -p File/Folder -t toWhom -s Subject

### delext

delete files with some special extension names (under a certain directory)

### search
search file in general case.

python Scripts/search.py -p "Folders/Math Note" -x "Game*"

### findfile
find a file in a more direct way

python Scripts/findfile.py -e md tex -p /Users/william/Folders

### baike
just try python baike.py -i Python (or any item in baiduepdia)


## common programs

base.py

- searchFiles # parent parser for searching files
- search # wrapper of os.walk
- some common paths:pathlib.Path

## Notice
recommended to use pathlib instead of os.path
