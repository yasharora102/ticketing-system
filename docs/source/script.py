import os
from m2r import parse_from_file

filename = '../../README.md'
with open(filename, 'r') as f:
    rst_content = parse_from_file(f)

with open('README.rst', 'w') as f:
    f.write(rst_content)