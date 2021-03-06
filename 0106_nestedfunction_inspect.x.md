#Nested function

1.Inner functions can access variables from the enclosing scope (in this case, the local variable x). If you're not accessing any variables from the enclosing scope, they're really just ordinary functions with a different scope.  
2.Readability   
source: http://stackoverflow.com/questions/1589058/nested-function-in-python


```python
def make_adder(x):
    def add(y):
        return x + y
    return add

plus5 = make_adder(5)
print(plus5(12))  
```
[out] 17


#inspect module   
inspect module cannot be used for peeking the source codes of built-in functions  
it provides methods to inspect where the methods, functions, or classes came from 
  
inspect.getdoc(object) : get one line desription of the object  
inspect.getfile(object) : get the file name where the object is on  
inspect.getmodule(object) : get the module name where the object is contained  
inspect.getsourcefile(object) : ---???? (dunno what's different from .getfile)  
inspect.getsourcelines(object) ---????   


```python

>>> import inspect as i
>>> import numpy as np
>>> i.getdoc(sorted)

'Return a new list containing all items from the iterable in ascending order.\n\nA custom key function can be supplied to customise the sort order, and the\nreverse flag can be set to request the result in descending order.'

>>> i.getsource(sorted)

TypeError: <built-in function sorted> is not a module, class, method, function, traceback, frame, or code object

>>> i.getsourcefile(np.ndarray)                 or               i.getfile(np.ndarray)
'C:\\Users\\xozmf\\Anaconda3\\lib\\site-packages\\numpy\\__init__.py'

>>> i.getsource(np)
'raise ImportError(msg)\n\n    from .version import git_revision as __git_revision__\n    from .version import version as __version__\n\n    from ._import_tools import PackageLoader\n\n    def pkgload(*packages, **options):\n        loader = PackageLoader(infunc=True)\n        return loader(*packages, **options)\n\n    from . import add_newdocs\n    __all__ = [\'add_newdocs\',\n               \'ModuleDeprecationWarning\',\n               \'VisibleDeprecationWarning\']\n\n    pkgload.__doc__ = PackageLoader.__call__.__doc__\n\n    # We don\'t actually use this ourselves anymore, but I\'m not 100% sure that\n    # no-one else in the world is using it (though I hope not)\n    from .testing import Tester\n    test = testing.nosetester._numpy_tester().test\n    bench = testing.nosetester._numpy_tester().bench\n\n    from . import core\n    from .core import *\n    from . import compat\n    from . import lib\n    from .lib import *\n    from . import linalg\n    from . import fft\n    from . import polynomial\n    from . import random\n    from . import ctypeslib\n    from . import ma\n    from . import matrixlib as _mat\n    from .matrixlib import *\n    from .compat import long\n\n    # Make these accessible from numpy name-space\n    # but not imported in from numpy import *\n    if sys.version_info[0] >= 3:\n        from builtins import bool, int, float, complex, object, str\n        unicode = str\n    else:\n        from __builtin__ import bool, int, float, complex, object, unicode, str\n\n    from .core import round, abs, max, min\n\n    __all__.extend([\'__version__\', \'pkgload\', \'PackageLoader\',\n               \'show_config\'])\n    __all__.extend(core.__all__)\n    __all__.extend(_mat.__all__)\n    __all__.extend(lib.__all__)\n    __all__.extend([\'linalg\', \'fft\', \'random\', \'ctypeslib\', \'ma\'])\n\n\n    # Filter annoying Cython warnings that serve no good purpose.\n    warnings.filterwarnings("ignore", message="numpy.dtype size changed")\n    warnings.filterwarnings("ignore", message="numpy.ufunc size changed")\n    warnings.filterwarnings("ignore", message="numpy.ndarray size changed")\n\n    # oldnumeric and numarray were removed in 1.9. In case some packages import\n    # but do not use them, we define them here for backward compatibility.\n    oldnumeric = \'removed\'\n    numarray = \'removed\'\n# \n__mkl_version__ = \'11.3.3\' \n'
#returns the sourcecode as a line of string
```

