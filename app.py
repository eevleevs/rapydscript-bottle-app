from bottle import get, run, static_file
from glob import glob
import os
from pathlib import Path


@get('/')
def main():
    return static_file('index.html', root='static/html')


@get('/rapydscript/<path:path>.js')
def rapydscript(path):
    return static_file(f'{path}.js', root='rapydscript')


@get('/static/<path:path>')
def static(path):
    return static_file(path, root='static')


if __name__ == '__main__':
    # transpile rapydscript
    try:
        transpiled = os.stat('rapydscript/.transpiled').st_mtime
    except FileNotFoundError:
        transpiled = 0
    for name in glob('rapydscript/*.py'):
        if os.stat(name).st_mtime > transpiled:
            os.system(f"rapydscript {name} -b -o {name.replace('.py', '.js')}")
    Path('rapydscript/.transpiled').touch()
    
    # run bottle
    run(port=8081, debug=True, reloader=True)
