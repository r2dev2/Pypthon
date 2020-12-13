# Pypthon

Pipes for python3 to be used in shell

# Setup

```
pip install pypthon -U 
```

# Usage

```
pyp 'Pypthon command'
```

If pypthon is not in your path, you must invoke via

```
python3 -m pypthon 'Pypthon command
```

To see the python code being generated, use the ``--show-python`` flag:

```
pyp --show-python 'Python command'
```

A Pypthon command consists of the following

```
source | piped function | piped function | piped function
```

The source must be any python expression. To have the source be an external command being piped into Pypthon, use ``stdin``.

## Piped functions

Piped functions are any python functions which take the previous value as their last argument. In the example pypthon code,

```python
[2, 1, 3] | sorted | print "Sorted" "list:"
```

``sorted`` takes in the iterable ``[2, 1, 3]`` as its last parameter and ``print`` takes the sorted list as its last parameter. When passing other arguments to functions in Pypthon, one must use the space separated syntax. In our example, the strings ``"Sorted"`` and ``"list:"`` are passed as arguments to ``print`` via the syntax of separating each argument with a space.

```
Sorted list: [1, 2, 3]
```

will be outputted by the above command.

## Lambda expressions

In python, lambdas are of the following structure

```python
lambda arg1, arg2: arg1 + arg2
```

In pypthon, lambda expressions do not need the ``lambda`` keyword before the arguments. In the example,

```python
['1.', '6.', '2.', '4.'] | map x: int(float(x)) | reduce x, y: x if x > y else y | print
```

``map`` converts the strings in the list into integers, and ``reduce`` finds the maximum of the integers.

## Environment

The environment is fully customizable with a ``.pypthonrc.py``. On startup, the pypthonrc will be imported, giving the pypthon command access to custom functions. If you feel like you have general functions that can be used by other pypthon users, do not hesitate to send a pull request to add your customizations to the standard environment as it is still growing. It is advisable to not include heavy imports such as ``numpy`` to the pypthonrc as the startup time will be negatively impacted for each invocation of pypthon.

To import modules specifically for the Pypthon invocation, use the ``-i`` flag.

```
pyp -i 'requests' -i 'numpy as np' "[1, 2, 3] | map x: requests.get('https://google.com').status_code | list | np.mean | print"
```

In the above example, numpy and requests were imported. The syntax of ``module`` ``as`` ``alias`` is valid in Pypthon. The methods in the modules are available for use in Pypthon.

The documentation for the standard environment is at [docs/example.md](https://github.com/r2dev2bb8/Pypthon/blob/master/docs/environment.md).

# Other

There are currently some bugs in parsing the source to the pipe chain. If it incorrectly raises an error in the first pipe segment, surround it with parenthesis and see if it works.

This project idea was heavily inspired by the pied piper package which only works with Python 2 and has virtually disappeared.
