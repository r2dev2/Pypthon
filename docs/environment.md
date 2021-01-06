## Usage

To run the pypthon code in the following documentation, run ``pyp 'Pypthon command'``.

## Imports

The default imports are

```python
import functools
import itertools as it
import os
import random
import re
import shlex
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from functools import reduce
from pathlib import Path
from pprint import pprint
from sys import stdin
```

## Functions

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

``uprint`` unpacks the previous value into the ``print`` function. It takes one optional parameter which is a dictionary containing the keyword arguments to pass to ``print``.

### ufunc

```python
[[1, 2, 3], [4, 5, 6]] | ufunc it.chain | uprint
```
will output
```
1 2 3 4 5 6
```

``ufunc`` unpacks the previous value into the function provided as the first argument. It takes a second optional argument specifying keyword arguments.

### sh

```python
[1, 2, 3, 4, 5, 6] | map str | sh "shuf" | map str.strip | uprint
```

``sh`` inputs the previous values into a shell function. It takes one argument which is the shell command.

### cmap

The following Pypthon invocation

```
pyp -i 'requests' "range(3) | cmap x: requests.get('https://google.com').status_code | uprint"
```

will concurrently send get requests to google using ``cmap``. ``cmap`` (concurrent map) concurrently maps a function to the previous value. It has a second optional parameter which is the amount of threads to limit ``cmap`` to. This defaults to ``100``.

### cfilter

The following Pypthon invocation

```
pyp -i 'requests' "['https://google.com', 'https://google.com/pypthon'] | cfilter url: requests.get(url).status_code == 200 | uprint"
```

will concurrently filter urls for successful get requests using ``cfilter``. ``cfilter`` (concurrent filter) concurrently filters a function to the previous value. It has a second optional parameter which is the amount of threads to limit ``cfilter`` to. This defaults to ``100``.


### result_fn

The following pypthon invocation

```
pyp -i 'requests' "['https://google.com', 'invalidurl'] | cmap url: result_fn(requests.get)(url) | list | print"
```
will output
```
[<Response [200]>, MissingSchema("Invalid URL 'invalidurl': No schema supplied. Perhaps you meant http://invalidurl?")]
```

``result_fn`` wraps a function to make it return the function return value or the exception raised by the function. This is used as of now as there is no ``try``/``catch`` syntax in Pypthon yet.
