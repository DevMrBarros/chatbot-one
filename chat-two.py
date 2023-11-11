import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Vale muito a pena aprender Python, pois é uma das linguagens que mais cresce atualmente{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} A média salarial de um programador Python é em torno de R$ 150.000,00 por ano.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} pra se tornar um cientista de dados você precisa estudar alguns temas que são muito relevantes para a profissão.\nÉ preciso se dedicar e estar sempre em busca de novos conhecimentos.\nUma boa forma de aprimorar seus conhecimentos e aprender muita coisa legal é se inscrever no Canal NERD DOS DADOS,\nporque é um canal que traz conteúdos atualizados toda semana.\nEntão se inscreve aqui no canal e ative as notificações pra sempre ficar por dentro das novidades.{os.linesep}')    
    else:
        print('Digite apenas as opções 1, 2 ou 3')    


def start():
    #Apresentar o chatbot
    print('Olá, Bem vindo ao Bot DevMrBarros')

    #Pedir o nome
    nome = input('Digite seu nome: ')
    
    while True:

        #Oferecer um menu de opções
        resposta = input(
            f'O que gostaria de saber hoje? {os.linesep}[1] - Vale a pena aprender Python? {os.linesep}[2] - Qual a média salarial de um profissional que trabalha com Python? {os.linesep}[3] - E como eu faço pra me tornar um cientista de dados?{os.linesep}')
        
        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ =='__main__':
    start()