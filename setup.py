from setuptools import setup, find_packages

setup(
    name='pymolly',
    version='0.1.0',
    packages=find_packages(),
    py_modules=['pymolly'],
    install_requires=[
        'astropy',
        'matplotlib',
        'numpy',
        'trm-molly @ git+https://github.com/WarwickAstro/trm-molly.git'
    ],
    author='Felipe Jimenez-Ibarra',
    description='A pytonian version of  MOLLY',
    url='https://github.com/fji/pymolly',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
