
.PHONY: run install


run: venv/bin/jupyter-lab
	venv/bin/jupyter-lab index.ipynb

install: venv/bin/jupyter-lab

test: venv/bin/jupyter-lab
	venv/bin/pytest --nbmake  -n=auto *.ipynb

venv/:
	python3 -m venv venv
	venv/bin/pip install --upgrade pip

venv/bin/jupyter-lab: venv/
	venv/bin/pip install -r requirements.txt
	touch venv/bin/jupyter-lab


