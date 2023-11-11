import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, na minha visão, vale muito a pena aprender Python. Python é uma das linguagens que mais cresce no mundo e possui salários mensais que variam de R$2100,00 a mais de R$10000,00 no Brasil. Além disso, a média anual nos EUA é de $85.000 dólares.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, o tempo para conseguir um emprego com Python varia muito com o nível de esforço, dedicação e busca diária por vagas de cada indivíduo. Alguns conseguem em menos de 3 meses, outros demoram mais. Tudo depende do quanto você já sabe ou está disposto a aprender.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, primeiro entenda que ninguém vai dizer magicamente que você está BOM o suficiente para conseguir um emprego. Você precisa começar a aplicar para oportunidades ou até mesmo criar as suas. Quando dominar os fundamentos de uma linguagem (no caso de Python, recomendo aprender pelo menos os 5 pilares de programação), estará pronto.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, você pode estudar através de vídeos gratuitos no YouTube, livros e sites de programação. Se busca um lugar com suporte 1 a 1, estrutura sequencial, projetos novos todos os meses e um curso que ensine toda a base e habilidades lucrativas para criar aplicações em Python, recomendo o cursodepython.net.{os.linesep}')
    elif resposta == '0':
        print('Até mais! Volte sempre.')
        exit()
    else:
        print('Digite apenas 1, 2, 3, 4 ou 0 para sair.')

def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo a DevMrBarros')
    # Pedir o nome
    nome = input('Digite seu nome: ')
    # Pedir o e-mail
    email = input('Digite seu e-mail: ')

    while True:
        # Oferecer o menu de opções
        resposta = input(
            f'O que gostaria de saber hoje?{os.linesep}[1] - Vale a pena aprender Python?{os.linesep}[2] - Quanto tempo leva para conseguir um emprego com Python?{os.linesep}[3] - Quando vou saber que estou BOM o suficiente para conseguir um emprego?{os.linesep}[4] - Onde me recomenda estudar Python para conseguir um emprego hoje?{os.linesep}[0] - Sair{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()
