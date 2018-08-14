# Flask

Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.

##Example
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```