class Person:
    pass


person = Person()

p_key = "name"
p_value = "Ritvik"


setattr(person, p_key, p_value)
name = getattr(person, p_key)
