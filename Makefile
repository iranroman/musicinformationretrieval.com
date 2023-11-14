
.PHONY: run

run: venv/bin/jupyter-lab
	venv/bin/jupyter-lab index.ipynb

venv/:
	python3 -m venv venv
	venv/bin/pip install --upgrade pip

venv/bin/jupyter-lab: venv/
	venv/bin/pip install -r requirements.txt


