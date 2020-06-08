from analise_sentimentos import AnaliseSentimentos
from googletrans import Translator

message = AnaliseSentimentos()

translatedText = Translator().translate(text=input('Digite um texto: '), dest='pt')
result         = message.avalia(translatedText.text)


