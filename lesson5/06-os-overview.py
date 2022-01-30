import os

if os.path.exists('data.txt'):
    os.remove('data.txt')

current_dir = '.'
files = os.listdir(current_dir)

for x in files:
    print(os.path.split(x))
    # print(os.path.isdir(f"./{x}"))

print(os.path.split('/etc/hosts'))

print(os.path.join('/etc/hosts', 'file', 'hop/test', '1.txt'))
