# Two types of modules in python
# build in modules
# external modules
# https://docs.python.org/3/py-modindex.html
import math
import os
import mymodule
import requests

print(math.sqrt(16))
mymodule.helloworld()
r=requests.get("https://www.google.com")
print(r.text)