import os

print('setenv....', end=' ')
print(os.environ['USER'])

os.environ['USER'] = 'Balazs'
os.system('python echoenv.py')

os.environ['USER'] = 'Mark'
os.system('python echoenv.py')

os.environ['USER'] = input('?')
print(os.popen('python echoenv.py').read())

