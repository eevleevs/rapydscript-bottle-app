- `npm install rapydscript`
- for reloading on change of any `rapydscript/*.py`, modify local copy of `bottle.py` (or use the one provided here)
    - at the top add
        ```python
        from glob import glob
        ```
    - at FileCheckerThread.run() add
        ```python
        for path in glob('rapydscript/*.py'):
            files[path] = mtime(path)
        ```