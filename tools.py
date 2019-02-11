#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Tools for Scripts
"""

import pathlib

import sh

# head = "#!/usr/bin/env python3"

scriptsFolder = pathlib.Path('/Users/william/Scripts/')

def d2u():
    for f in scriptsFolder.iterdir():
        sh.dos2unix(f)

# def script_list():
#     for f in scriptsFolder.iterdir():
#         print(f)


def script_list(n=1):
    for f in scriptsFolder.iterdir():
        if f.suffix == '.py':
            print(f)
            lines = f.read_text(encoding='utf-8').strip().split('\n')
            print('\n'.join(lines[:n]))


def set_env():
    # set environment
    for f in scriptsFolder.iterdir():
        if f.suffix == '.py':
            lines = f.read_text(encoding='utf-8').strip().split('\n')
            first_line = lines[0]
            if first_line in {'#!/usr/local/bin/python, #!/usr/bin/env python'}:
                lines[0] = '#!/usr/bin/env python3'
            else:
                lines.insert(0, '#!/usr/bin/env python3')
            
            f.write_text('\n'.join(lines), encoding='utf-8')

script_list()