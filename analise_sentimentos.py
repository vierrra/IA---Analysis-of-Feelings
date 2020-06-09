import spacy

class AnaliseSentimentos: 

    def __init__(self):
        self.__nlp = spacy.load('pt_core_news_sm')
        self.__dicionario = {}
        self.__criaDicionario()

    def __criaDicionario(self):
        #Busca o Lexico
        arquivo = open('./texto.txt', 'r')
        linhas = arquivo.readlines()

        #Salva as palavras no dicionario
        for linha in linhas:
            dado = linha.split(',')
            self.__dicionario[dado[0]] = int(dado[2])
        #Encerra o arquivo
        arquivo.close()

    def avalia(self, texto): 
        retorno = {'polaridade': 0, 'entidades': []}

        tokens = self.__nlp(texto)
        #Identifica as entidades
        retorno['entidades'] = tokens.ents
        
        #Avalia as polaridades das palavras
        for token in tokens:
            #Normaliza o texto
            palavra = str(token.lemma_).lower()

            #Checa se existe no dicionário
            if (palavra in self.__dicionario):
                retorno['polaridade'] += self.__dicionario[palavra]
            
        return retorno