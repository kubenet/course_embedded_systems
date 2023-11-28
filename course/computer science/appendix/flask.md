# Введение


## Установка `flask`

`pip install flask`

## Использование `flask`

```python
"""test Flask with this"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'
```