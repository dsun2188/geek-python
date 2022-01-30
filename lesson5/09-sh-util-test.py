import shutil
import sys

shutil.copyfile('person.json', 'lesson5/person.json')

shutil.rmtree('lesson5')

sys.stdin  # standard input
sys.stdout  # standard output
sys.stderr  # standard error output

sys.exit(5)
