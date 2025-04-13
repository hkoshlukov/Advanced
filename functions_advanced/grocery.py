def grocery_store(**products):
    new_dict = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = []
    for product, price in new_dict:
        result.append(f"{product}: {price}")
    return '\n'.join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
