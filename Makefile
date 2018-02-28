
init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock


test:
	detox


ci:
	pipenv run py.test --junitxml=report.xml

coverage:
	pipenv run py.test --verbose --cov-report term --cov-report xml --cov=rocketlauncher tests

flake8:
	pipenv run flake8
