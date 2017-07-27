import os 
import tensorflow as tf
import sys
import urllib

#versioning, urllib named differently for dif python versions
if sys.version_info[0] >= 3:
  from urllib.request import urlretrieve
else:
  from urllib import urlretrieve
