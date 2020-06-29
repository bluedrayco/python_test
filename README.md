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

- Execute the script specifying the number to convert

```python
python quantity.py [number]
```

example:

```python
python quantity.py 3243243242343
```

# Issues

I found a little issue that I would like to explain:

If you refer an amount in bytes the measure divided by 1024 because it's multiple by 2, in the case of the excercise 
you refer by 1000, i.e the result of my script could not be correct, if you like to adjust the script it's very simple, you only need to change the line:

    divided_by = 1000

by:

    divided_by = 1024