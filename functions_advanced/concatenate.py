def concatenate(*words, **parts):
    text = ''.join(words)

    for key in parts:
        text = text.replace(key, parts[key])

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
