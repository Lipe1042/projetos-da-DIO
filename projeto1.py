# Classificador de nivel de heroi


# variaveis

nomedoheroi = "Felipão"
quantidadedexp = 5001
nivel = ""


# estrutura de decisão

if quantidadedexp < 1000:
    nivel = "Ferro"


elif quantidadedexp >= 1000 and quantidadedexp <= 2000:
    nivel = "Bronze"


elif quantidadedexp >= 2001 and quantidadedexp <= 5000:
    nivel = "Prata"


elif quantidadedexp >= 5001 and quantidadedexp <= 7000:
    nivel = "Ouro"


elif quantidadedexp >= 7001 and quantidadedexp <= 8000:
    nivel = "Platina"


elif quantidadedexp >= 8001 and quantidadedexp <= 9000:
    nivel = "Ascendente"


elif quantidadedexp >= 9001 and quantidadedexp <= 10000:
    nivel = "Imortal"


elif quantidadedexp >= 10001:
    nivel = "Radiante"


# resultado
print(f"O Herói de nome {nomedoheroi} está no nível de {nivel}")



