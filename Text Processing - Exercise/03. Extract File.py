# import os.path
# line = input()
#
# x = os.path.basename(line)
# x = x.split('.')
# print(f"File name: {x[0]}")
# print(f'File extension: {x[1]}')
line = input().split('\\')
x = line[-1]
x = x.split('.')
print(f"File name: {x[0]}")
print(f'File extension: {x[1]}')

