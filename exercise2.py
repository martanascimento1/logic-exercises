from sympy import symbols, Equivalent, parse_expr

def espressoes(sentenca1, sentenca2):
    
    value1 = parse_expr(sentenca1)
    value2 = parse_expr(sentenca2)

    resultado = Equivalent(value1, value2)

    return resultado

sentenca1 = "(P | Q) & (Q | R)"
sentenca2 = "(P | R)"

if espressoes(sentenca1, sentenca2):
    print("As sentenças são logicamente equivalentes.")
else:
    print("As sentenças não são logicamente equivalentes.")
