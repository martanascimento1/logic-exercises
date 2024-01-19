from sympy.logic.boolalg import truth_values
from sympy.logic.boolalg import And, Or, Implies, Not
from sympy.abc import symbols

def avaliar_sentenca(sentenca):
    # Obter todas as combinações de valores verdadeiro/falso para as variáveis na sentença
    variaveis = list(sentenca.atoms(symbols))
    combinacoes = list(truth_values(variaveis))

    # Avaliar a sentença para cada combinação de valores
    resultados = [(comb, sentenca.subs(dict(zip(variaveis, comb)))) for comb in combinacoes]

    return resultados

def classificar_sentenca(resultados):
    valores_verdade = [resultado[1] for resultado in resultados]

    # Classificar a sentença
    if all(valores_verdade):
        return "Tautologia"
    elif not any(valores_verdade):
        return "Contradição"
    else:
        return "Satisfatível"

def imprimir_passo_a_passo(resultados):
    for resultado in resultados:
        combinacao, valor = resultado
        print(f"{' ^ '.join([f'{var}={int(val)}' for var, val in zip(combinacao, valor)])} => {int(valor)}")

# Exemplo de uso:
sentenca = Or(And(symbols('A'), symbols('B')), Not(symbols('C')))

resultados = avaliar_sentenca(sentenca)

print("Avaliação passo a passo:")
imprimir_passo_a_passo(resultados)

classificacao = classificar_sentenca(resultados)
print(f"\nClassificação da Sentença: {classificacao}")
