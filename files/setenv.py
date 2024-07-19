import os

print('setenv....', end=' ')

os.environ['USER'] = 'Balazs'
os.system('python echoenv.py')

os.environ['USER'] = 'Mark'
os.system('python echoenv.py')

os.environ['USER'] = input('?')
print(os.popen('python echoenv.py').read())

