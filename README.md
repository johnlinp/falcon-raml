# Falcon RAML

This is a [Falcon](https://falconframework.org/) middleware for parameter checking using [RAML](http://raml.org/).


## Requirement

- Python: >= 3.4.
- Falcon: >= 1.1.0.
- RAML: Only 0.8 is supported since I use [ramlfications](https://github.com/spotify/ramlfications/) as the RAML parser.


## Install

1. `git clone https://github.com/johnlinp/falcon-raml`
1. `cd falcon-raml`
1. `pip install .`


## Usage

```python
import falcon
import falconraml

api = falcon.API(middleware=[
    falconraml.ParameterChecker('spec.raml')
])
```


## Test

1. `pip install tox`
1. `tox`
