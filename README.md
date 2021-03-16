# socketio-maxsize-patch
Patch the maximum size of packets accepted over the async websocket connection establised using the `python-socketio` library.
[https://pypi.org/project/python-socketio/](https://pypi.org/project/python-socketio/)

Applying this patch sets `maxsize=0` i.e. the maximum size limit is removed.
### Usage
Do this at the top of the module before any `import` statements
```python
from patch import apply_patch
apply_patch()
```
### What you should see on `client.connect()`
On successful application of the patch, wise words will be spoken by `cowsay`
```
[patching max response size]

            ^__^            
            (oo)\_______    
            (__)\       )\/\ 
                ||----w |   
  w w w w w     ||     ||
  ```
