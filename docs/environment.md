### uprint

```python
[1, 2, 3] | uprint {"sep": "\n"}
```
will output
```
1
2
3
```

``uprint`` unpacks the previous value into the ``print`` function. It takes one parameter which is a dictionary containing the keyword arguments to pass to ``print``.

