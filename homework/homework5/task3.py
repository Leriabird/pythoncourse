__author__ = 'Leria'

import re

data = "def generate():\nnum_tests = 10\ntests = []\nfor test in range(num_tests):\na = random.randrange(10)\nb = random.randrange(10)\ntest_case = ""{} {}"".format(a, b)\ntests.append(test_case)\nreturn tests"

def check_code(code):
    listed = code.strip().split('\n')
    for index, line in enumerate(listed):
        treasures = re.findall('((\w+|_) = (\S+))', line)
        if len(treasures) > 0:
            print(index + 1, treasures[0][1])

#data = sys.stdin.read()
check_code(data)