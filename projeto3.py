# Escrevendo as classes de um Jogo

#Classe
class Heroi:

    def __init__(self, nome, idade, tipo):
    
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    def atacar (self):
#Fim da classe

#estrutura de controle 
        if self.tipo == "mago":
            ataque = "usou magia" 

        elif self.tipo == "guerreiro":
            ataque = "usou espada"

        elif self.tipo == "monge":
            ataque = "usou artes marciais"

        elif self.tipo == "ninja":
            ataque = "usou shuriken"

        print(f" {self.tipo} atacou usando {ataque}")

# Cria uma instância (objeto) da classe Heroi
heroi_Kratos = Heroi ("Kratos", 49, "guerreiro")

# Chama o método 'atacar' do objeto
heroi_Kratos.atacar()