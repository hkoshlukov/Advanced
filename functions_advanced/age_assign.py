def age_assignment(*names, **info):
    result = []
    for letter, age in info.items():
        person = ''
        for name in names:
            if name.startswith(letter):
                person = name
                break
        result.append(f'{person} is {age} years old.')

    return '\n'.join(sorted(result, key=lambda x: x[0]))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
