spam = {'name':'pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'

print(spam)

spam = {'name':'pooka', 'age' : 6}
spam.setdefault('color','white')

print(spam)