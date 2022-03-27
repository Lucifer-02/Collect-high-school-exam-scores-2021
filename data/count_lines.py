import subprocess

def line_count(filename):
    return int(subprocess.check_output(['wc', '-l', filename]).split()[0])

s = 0
for i in range(1,65):
    if i == 50:
        continue
    s += line_count(str(i) + '.csv')

print(s)
