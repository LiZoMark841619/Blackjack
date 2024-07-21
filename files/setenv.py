import os

print('setenv...', end=' ')
print(os.environ['USERNAME'])

os.environ['USERNAME'] = 'Balazs'
os.system('python echoenv.py')

os.environ['USERNAME'] = 'Mark'
os.system('python echoenv.py')

os.environ['USERNAME'] = input('? ')
print(os.popen('python echoenv.py').read())

