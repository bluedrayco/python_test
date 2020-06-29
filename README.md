# Excercise

Write a function in Python called ‘humanSize’ that takes a non-negative number of bytes and returns a string 
with the equivalent number of ‘kB’, ‘MB’, ‘GB’, ‘TB’, ‘PB’, ‘EB’, ‘ZB’, or ‘YB’, between [0, 1000), 
with at most 1 digit of precision after the decimal. If the number of bytes is >= 1000 YB, 
return this number of YB, for example 5120 YB. For example, your function might return ‘107.3MB’.
Write this function without writing a separate case for each byte prefix, and without using Math.log or Math.pow.

# Requirements
- Virtualenv
- Python 3

# How to execute 

- Create virtual environment

Put the following command for create a virtualenv based on python3

```bash
virtualenv venv --python=python3
```

- Accessing to virtualenv

```bash
source venv/bin/activate
```