# Pypthon

Pipes for python3 to be used in shell

# Setup

```
pip install -U pypthon
```

# Usage

```
pyp 'Pypthon command'
```

A Pypthon command consists of the following

```
source | piped function | piped function | piped function
```

The source must be any python expression. To have the source be another command being piped into Pypthon, use ``stdin``.

## Piped functions

Piped functions are any python functions which take the previous value as their last argument. In the example,

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

```python
# TODO documentation, for now just look in pypthon/environment.py
```

# Other

This project idea was heavily inspired by the pied piper package which only works with Python 2 and has virtually disappeared.
