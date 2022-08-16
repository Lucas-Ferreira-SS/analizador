class Analizador:
    def __init__(self) -> None:
        with open('text.txt', encoding='utf-8') as file:
            self.arq = file.read()
        self.expressoes = (self.arq.split('\n'))

    def verifica_indice(self,caractere, tipo):
        if caractere in tipo:
            return True
        return False
    
