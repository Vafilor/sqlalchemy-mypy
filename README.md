# About

This is a repo showing a possible bug with SQLAlchemy and mypy when working with mixins.

The bug happens on line 48 of main.py when running mypy and is:
```error: Unexpected keyword argument "user" for "Task"  [call-arg]```

## System Info

* Python: 3.12.2
* OS: macOS 14.5 
* SQLAlchemy: 2.0.31 
* mypy: 1.11.1
* mypy-extensions: 1.0.0

## To Reproduce

1. Install  ```pip install -r requirements.txt```
2. Run ```mypy main.py```