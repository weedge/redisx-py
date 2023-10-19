

init:
	pip3 install twine pytest

pypi_deploy:
	@rm -rf dist && python3 setup.py sdist bdist_wheel
	@twine upload --verbose --skip-existing dist/*

local_setup:
	@pip3 uninstall redisx -y
	@rm -rf dist && python3 setup.py install