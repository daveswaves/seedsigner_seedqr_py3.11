# Starting Poetry Virtual Environment and running project

```
cd ~/python_venv/test_seedqr_py3.11

poetry shell

python src/test_seedqr.py
```

## Tips

The project root (~/python_venv/test_seedqr) contains a '.venv' folder, so VS Code should pick this up automatically.

It will display something like `3.11.6 ('.venv': Poetry)` in the bottom right corner.

The `pyproject.toml` file lists all the required packages for the project:
```
[tool.poetry.dependencies]
python = "^3.8"
pip = "^23.3.1"
embit = "^0.7.0"
numpy = "^1.22.4"
opencv-python = "^4.6.0.66"
Pillow = "^9.4.0"
qrcode = "^7.3.1"
six = "^1.16.0"
```

To see the installed Python packages in the virtual environment run 'pip list':
```
$ pip list
Package           Version      Editable project location
----------------- ------------ -----------------------------------------------------
embit             0.7.0
numpy             1.24.4
opencv-python     4.8.1.78
Pillow            9.5.0
pip               23.3.1
pypng             0.20220715.0
pyzbar            0.1.9        /home/david/python_venv/test_seedqr/.venv/src/pyzbar
qrcode            7.4.2
setuptools        67.0.0
six               1.16.0
test-seedqr       0.1.0        /home/david/python_venv/test_seedqr
typing_extensions 4.8.0
urtypes           0.1.0        /home/david/python_venv/test_seedqr/.venv/src/urtypes
wheel             0.38.4
```

Alternatively, run `pip list | grep [PACKAGE]` to view a specific package:
```
$ pip list | grep embit
embit             0.7.0
```

View multiple packages:
```
$ pip list | grep -E 'embit|qrcode'
embit             0.7.0
qrcode            7.4.2
```

Display package details `pip show [PACKAGE]`:
```
$ pip show qrcode
Name: qrcode
Version: 7.4.2
Summary: QR Code image generator
Home-page: https://github.com/lincolnloop/python-qrcode
Author: Lincoln Loop
Author-email: info@lincolnloop.com
License: BSD
Location: /home/david/python_venv/test_seedqr/.venv/lib/python3.8/site-packages
Requires: pypng, typing-extensions
Required-by: test-seedqr
```

View latest package version: [https://pypi.org/project/embit](https://pypi.org/project/embit)


Search for available packages, in the browser: [https://pypi.org/search/?q=embit](https://pypi.org/search/?q=embit)

or command line:
```
$ poetry search embit

embit (0.7.0)
 yet another bitcoin library

seed-shuffler (0.0.0)
 BIP39 Seed Shuffler
```
