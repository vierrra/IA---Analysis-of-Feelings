from analise_sentimentos import AnaliseSentimentos
from googletrans import Translator

message = AnaliseSentimentos()

translatedText = Translator().translate(text=input('Digite um texto: '), dest='pt')
result = message.avalia(translatedText.text)

if (result['polaridade'] > 0):
    print('Frase positiva')
elif (result['polaridade'] < 0):
     print('Frase negativa')
else:
    print('Frase Neutra')


