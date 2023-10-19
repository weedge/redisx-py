## dev
```shell
pip3 uninstall redisx 
python3 setup.py install
# run python example like this
python3 examples/ann_usearch.py
```

## deploy
1. need register pypi user [https://pypi.org/](https://pypi.org/)
2. install `twine`, `pip3 install twine`, add token conf to `~/.pypirc`
```shell
[pypi]
  username = __token__
  password = {your token}
```
3. change `setup.py` version, then deploy
```shell
rm -rf dist && python3 setup.py sdist bdist_wheel
twine upload --verbose --skip-existing dist/*
```