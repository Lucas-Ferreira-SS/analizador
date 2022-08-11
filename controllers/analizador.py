class Analizador:
    def __init__(self) -> None:
        with open('text.txt', encoding='utf-8') as file:
            self.arq = file.read()
        self.expressoes = (self.arq.replace(' ', '').replace('\n', ''))
        self.ind = 0
        self.prox_caractere = self.expressoes[0]

    
    def le_proximo_caractere(self) -> None:
        try:
            self.ind += 1
            self.prox_caractere = self.expressoes[self.ind]

        except:
            self.prox_caractere = 'EOF'


    def verifica_indice(self, tipo):
        if self.prox_caractere != None and self.prox_caractere in tipo:
            return True
        return False
    

if __name__ == '__main__':
    analise = Analizador()
    analise.le_proximo_caractere(analise.expressoes[0])