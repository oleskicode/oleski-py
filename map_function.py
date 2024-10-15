def convert_to_american(x):
    usd_cad = 0.75  # USD to CAD. x is a tuple, where x[1] is price to convert
    return (x[0], x[1] * usd_cad)


timber_prices_in_canada = [("pinetree", 40), ("oak", 80), ("mapple", 50)]
print(timber_prices_in_canada)

mapped = map(convert_to_american, timber_prices_in_canada)

mapped_list = [*mapped]
print(mapped_list)
