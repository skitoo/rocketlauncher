
init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock


test:
	detox


ci:
	pipenv run py.test --junitxml=report.xml
