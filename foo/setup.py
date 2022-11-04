from setuptools import setup

setup(name='falcon-raml',
    version='0.1.0',
    description='Parameter checker middleware using RAML for Falcon',
    author='johnlinp',
    author_email='johnlinp@gmail.com',
    url='https://github.com/johnlinp/falcon-raml',
    license='New BSD License',
    install_requires=[
        'falcon==1.1.0',
        'ramlfications==0.1.9',
        'jsonschema==4.16.0',
    ],
    packages=[
        'falconraml',
    ],
)
