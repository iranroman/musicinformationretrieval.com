
.PHONY: run install

install: venv/bin/jupyter-lab

run: venv/bin/jupyter-lab
	venv/bin/jupyter-lab index.ipynb

test: venv/bin/jupyter-lab
	venv/bin/pytest --nbmake *.ipynb

venv/:
	python3 -m venv venv
	venv/bin/pip install --upgrade pip

venv/bin/jupyter-lab: venv/
	venv/bin/pip install -r requirements.txt
	touch venv/bin/jupyter-lab


