# Falcon RAML ![Python package](https://github.com/johnlinp/falcon-raml/actions/workflows/python-package.yml/badge.svg)

This is a [Falcon](https://falconframework.org/) middleware for parameter checking using [RAML](http://raml.org/).


## Requirement

- Python: >= 3.4.
- Falcon: >= 1.1.0.
- RAML: Only 0.8 is supported since I use [ramlfications](https://github.com/spotify/ramlfications/) as the RAML parser.


## Install

```bash
pip3 install falcon-raml
```


## Usage

```python
import falcon
import falconraml

api = falcon.API(middleware=[
    falconraml.ParameterChecker('spec.raml')
])
```


## Test

1. `pip3 install tox`
1. `tox`
