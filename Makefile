.PHONY: run install


run: venv/bin/jupyter-lab
	venv/bin/jupyter-lab README.md

install: venv/bin/jupyter-lab

test: venv/bin/jupyter-lab
	echo "Running .py tests..."
	venv/bin/pytest -n=1 --ignore-glob='*.ipynb' .
	echo "Running .ipynb tests..."
	venv/bin/pytest --nbmake -n=1 --ignore-glob='*.py' .

venv/:
	python3 -m venv venv
	venv/bin/pip install --upgrade pip

venv/bin/jupyter-lab: venv/
	venv/bin/pip install -r requirements.txt
	touch venv/bin/jupyter-lab