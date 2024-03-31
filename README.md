[![CircleCI](https://circleci.com/gh/PetterS/quickjs.svg?style=svg)](https://circleci.com/gh/PetterS/quickjs) [![PyPI version fury.io](https://d25lcipzij17d.cloudfront.net/badge.svg?id=py&r=r&ts=1683906897&type=6e&v=1.19.4&x2=0)](https://pypi.python.org/pypi/pyquickjs/)

Just install with

    pip install pyquickjs -i https://pypi.org/simple
OR

    python setup.py build -c mingw32 install
    

Binaries are provided for:
 - 1.24.3 and later: Python 3.7-3.12, 64-bit for Windows, macOS and GNU/Linux.

# How to Build 

### To build for Windows:
```text
1. Install MingW-W64-builds from https://www.mingw-w64.org/downloads/|https://sourceforge.net/projects/mingw-w64/files/
It is important to change the default to 64-bit when installing if a 64-bit Python is installed in windows.
2. Put the bin/ folder inside x86_64-8.1.0-posix-seh-rt_v6-rev0 in your system PATH when compiling.
3. The code below will moneky-patch distutils to work.
python setup.py build -c mingw32 bdist_wheel
```

### Build wheel
```shell
python3 setup.py bdist_wheel
```

### Build egg
```shell
python3 setup.py bdist_egg # discarded
```

### Build zip
```shell
python3 setup.py sdist
```

# Usage

```python
from pyquickjs import Function

f = Function("f", """
    function adder(a, b) {
        return a + b;
    }
    
    function f(a, b) {
        return adder(a, b);
    }
    """)

assert f(1, 2) == 3
```

Simple types like int, floats and strings are converted directly. Other types (dicts, lists) are converted via JSON by the `Function` class.
The library is thread-safe if `Function` is used. If the `Context` class is used directly, it can only ever be accessed by the same thread.
This is true even if the accesses are not concurrent.

Both `Function` and `Context` expose `set_memory_limit` and `set_time_limit` functions that allow limits for code running in production.

## API
The `Function` class has, apart from being a callable, additional methods:
- `set_memory_limit`
- `set_time_limit`
- `set_max_stack_size`
- `memory` – returns a dict with information about memory usage.
- `add_callable` – adds a Python function and makes it callable from JS.
- `execute_pending_job` – executes a pending job (such as a async function or Promise).

## Documentation
For full functionality, please see `test_pyquickjs.py`

# Developing
This project uses a git submodule for the upstream code, so clone it with the `--recurse-submodules` option or run `git submodule update --init --recursive` afterwards.

Use a `poetry shell` and `make test` should work from inside its virtual environment.

### Publish
.pypirc 放用户主目录,里面内容如下
```text
[distutils]
 index-servers=pypi 
[pypi]
repository = https://upload.pypi.org/legacy/
username = __yourname__
password = pypi-XXX
```
pypi生成token https://pypi.org/manage/account/token/
```shell
# 安装或更新twine
pip install --upgrade twine

python -m twine upload dist/*

```