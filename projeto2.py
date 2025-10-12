
# Calculadora de partidas Rankeadas


# função
def calculo (vitoria, derrota):

    calculo = vitoria - derrota 
    return calculo

# variaveis 
nomeDoHeroi = "Felipão"
vitorias = 71
derrotas = 50
SaldoDeVitorias = calculo (vitorias, derrotas)
nivel = ""

# estrutura de controle
if SaldoDeVitorias <= 10:
    nivel = "Ferro"

elif SaldoDeVitorias >= 11 and SaldoDeVitorias <= 20:
    nivel = "bronze"

elif SaldoDeVitorias >= 21 and SaldoDeVitorias <= 50:
    nivel = "prata"

elif SaldoDeVitorias >= 51 and SaldoDeVitorias <= 80:
    nivel = "ouro"

elif SaldoDeVitorias >= 81 and SaldoDeVitorias <= 90:
    nivel = "diamante"

elif SaldoDeVitorias >= 91 and SaldoDeVitorias <= 100:
    nivel = "lendario"

elif SaldoDeVitorias >= 101:
    nivel = "imortal"

# resultado 
print(f"O Heroi de nome {nomeDoHeroi} tem saldo de {SaldoDeVitorias} vitorias e está no nivel {nivel}")