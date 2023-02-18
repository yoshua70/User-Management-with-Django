# User Management with Django

## Setup guide

Create a new directory to contain the virtual environment:
```shell
$ mkdir ~/.virtualenvs
```

Create a new virtual environment:
```shell
$ python 3 -m venv ~/.virtualenvs/djangodev
```

If you get an error on Ubuntu/Debian, then you need to install the `python3-venv` package:
```shell
$ sudo apt install python3-venv
```

Activate the newly created environment:
```shell
$ source ~/.virtualenvs/djangodev/bin/activate
```

Install a version of Django via `pip`:
```shell
$ python3 -m pip install Django
```

Verify the version of Django you've just installed:
```shell
$ python3 -m django --version
```

