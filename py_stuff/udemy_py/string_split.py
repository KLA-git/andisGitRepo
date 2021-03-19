#!
x = 'Hi im a string'
# --> ['Hi', 'im', 'a', 'string']
x.split()

# -->['H', ' ', 'm a str', 'ng']
print(x.split('i'))

print('the {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

name="andi"
print(f'Hi ich bin {name}')
num = 23.45678
print(f"My 10 character, four decimal number is:{num:{10}.{6}f}")