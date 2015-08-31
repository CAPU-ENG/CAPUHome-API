run:
	python run.py
req:
	pip install -r requirements.txt
deploy:
	service capuhome-api reload
clean:
	find . -name '*.pyc' -print0 | xargs -0 rm -f
	find . -name '*.swp' -print0 | xargs -0 rm -f
	-@sudo rm -rf whoosh_index
permission:
	chown -R www-data.www-data .
	chown www-data.www-data /tmp/jieba.cache
pyflakes:
	pyflakes app config.sample.py run.py
pep8:
	pep8 app config.sample.py run.py
pylint:
	pylint app config.sample.py run.py
lint: pyflakes pep8 pylint
