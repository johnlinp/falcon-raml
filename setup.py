from distutils.core import setup

setup(name='falcon-raml',
    version='0.1',
    description='Parameter checker middleware using RAML for Falcon',
    author='johnlinp',
    author_email='johnlinp@gmail.com',
    install_requires=[
        'falcon',
        'ramlfications',
        'jsonschema',
    ],
    packages=[
        'falconraml',
    ],
)
