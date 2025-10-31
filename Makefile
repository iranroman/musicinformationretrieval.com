.PHONY: run install build fix


run: venv/bin/jupyter-lab
	venv/bin/jupyter-lab README.md

install: venv/bin/jupyter-lab
	venv/bin/pip install -e .

test: venv/bin/jupyter-lab
	echo "Running .py tests..."
	venv/bin/pytest -n=auto --ignore-glob='*.ipynb' --reruns 3 --reruns-delay 5 tests
	echo "Running .ipynb tests..."
	venv/bin/pytest --nbmake -n=auto --ignore-glob='*.py' --ignore-glob='*exercise*.ipynb' --ignore-glob='*adtlib*.ipynb' --reruns 3 --reruns-delay 5 mirdotcom

venv/:
	python3 -m venv venv
	venv/bin/pip install --upgrade pip

venv/bin/jupyter-lab: venv/
	venv/bin/pip install -r requirements.txt
	touch venv/bin/jupyter-lab

build:
	jupyter-book build mirdotcom

fix:
	black mirdotcom/content --target-version=py310