line = input()
line = [x for x in line if x not in 'аеёиоуыэюяАЕЁИОУЫЭЮЯ']
print(''.join(line))