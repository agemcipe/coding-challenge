# coding_challenge

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Description

This is my Implementation to solve the [Taktile Coding Challenge](https://github.com/taktile-org/coding-challenge)
For reference the coding challenge is stated as:


> Your challenge is to implement `fold` in the language of your choice.
> `fold` is a higher order function that takes
> * a sequence of type A
> * a "starting" value of type B
> * a function (A, B) -> B
> 
> and returns a B. E.g., the `sum` of an array is a special case of fold, where
> * the sequence is an array of numbers
> * the starting value is 0
> * the function is `+`
> 
> 
> You can find more information on [Wikipedia](https://en.wikipedia.org/wiki/Fold_(higher-order_function)).

## Requirements
Create a conda environment to run this project in isolation (not needed but recommended).

```[bash]
conda env create -f environment.yml
conda activate coding_challenge 
```

## Installation
```[bash]
pre-commit install
pip install --editable .
```

## Usage
```[python]
from coding_challenge.main import fold

fold(iterable=[1,2,3], start=0, fn=lambda x,y: x+y)
```

Or check the `tests/` for more examples of how to run the code 