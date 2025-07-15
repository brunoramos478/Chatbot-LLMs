# Desenvolvido por Bruno Ramos 👨‍💻
# Bibliotecas usadas

import os

from dotenv import load_dotenv
from docling.document_converter import DocumentConverter
from langchain_groq import ChatGroq

# Recebe uma env contendo a chave api  

load_dotenv()
groq_api = os.getenv('groq_api_key')

# Configura o Chatbot

llma = ChatGroq(

    model = "llama-3.3-70b-versatile",
    temperature = 0.3,
    max_retries = 2,
    api_key = groq_api

)

#Função converter em documentos.md 

def convert_doc():
    
 entrada = input('Cole aqui o endereço: ')
    
 convert = DocumentConverter()
 res = convert.convert(entrada)
 print(res.document.export_to_markdown())
    
 with open("Documento.md", "w", encoding="UTF-8") as s:
  s.write(res.document.export_to_markdown())
  print(res.document.export_to_markdown)
       
# Memória do chatbot

memoria = [{"role": "system", "content": "Chatbot Aqui"}]
def robo():
    
  while True:

   pergunta = input('Caso deseja voltar ao menu digite (voltar)\n'  'Olá! Como posso ajudar? ').strip().lower()
   
   
# Armazena a pergunta
   memoria.append({"role": "user", "content": pergunta})

# Mostra a resposta da pergunta

   saida = llma.invoke(memoria) 
   print("🤖 Chatbot: ", saida.content)
   memoria.append({"role": "assistant", "content": saida.content})

# Voltar para o menu
   if pergunta in ['encerrar', 'fechar', 'sair', 'exit', 'parar', 'voltar']:
       print('Qualquer dúvida estou aqui. 😀 Encerrado')
       break   


# Menu terminal

def main():
    while True:
        
        print( '\n', ' ' * 16 ,'Bem-vindo ao menu interativo')
        
        print('''  \n
                   |------------------------|            
                   | 1--Converter Links MD  |
                   |------------------------|
                   | 2--Falar Com Chatbot   |
                   |------------------------|
                   | 3-------Encerra        |
                   |------------------------|
             ''')
        select = input('Selecione Uma Opção ').strip().lower()

        if select in ['1', 'converter','abrir arquivo', 'converter arquivo', 'md','converter links','link', 'links']:
            convert_doc()

        elif select in ['2', 'falar', 'falr com assistente', 'assistente', 'buscar','pesquisar','chatbot', 'falar com chatbot']:
            robo()    
            
        elif select in ['3', 'encerrar', 'fechar', 'sair', 'exit', 'parar']:
            print('Programa finalizado')
            break   

main()
