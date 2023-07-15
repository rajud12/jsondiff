SHELL := /bin/bash

install_req:
	pip3 install -r requirements.txt

build_file:
	python3 setup.py clean sdist bdist_wheel