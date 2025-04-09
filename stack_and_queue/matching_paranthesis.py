data = input()

parentheses = []

for ch in range(len(data)):
    if data[ch] == '(':
        parentheses.append(ch)

    elif data[ch] == ')':
        start_index = parentheses.pop()
        result = data[start_index:ch + 1]
        print(result)
        