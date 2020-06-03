def power(a: int, b:int) ->int:
    return a**b

print(power.__annotations__)

# Output:
# {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}