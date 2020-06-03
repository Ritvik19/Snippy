class Connection:
    def __init__(self):
        pass

    def __enter__(self):
        # Initialize connection...
        pass

    def __exit__(self, type, value, traceback):
        # Close connection...
        pass

with Connection() as c:
    # __enter__() executes
    pass
    # conn.__exit__() executes
    
##################################################
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

with tag("h1"):
    print("This is Title.")