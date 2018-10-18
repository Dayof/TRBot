from app.mac import mac, signals

'''
Signals this module listents to:
1. When a message is received (signals.command_received)
==========================================================
'''
@signals.command_received.connect
def handle(message):
    if message.command == 'noticia':
        get_news(message)
    elif message.command == 'ajuda':
        help(message)
    else:
        menu(message)

'''
Actual module code
==========================================================
'''
def get_news(message):
    who_name = message.who_name
    greeting = f'Olá {who_name},\n'
    new = '*TSE lança site para esclarecer os eleitores sobre fake news*\n' \
    'O Tribunal Superior Eleitoral (TSE) lançou uma página na internet ' \
    'para ajudar a esclarecer o eleitorado brasileiro sobre as notícias ' \
    'falsas.\nFonte : https://congressoemfoco.uol.com.br/eleicoes/tse-' \
    'lanca-pagina-para-esclarecer-eleitores-sobre-noticias-falsas/'
    answer = f'{greeting}{new}'
    mac.send_message(answer, message.conversation)

def help(message):
    answer = '*Tah Repreendido ! Bot* \nMaiores informações no site' \
    'https://tahrepreendido.com .'
    mac.send_message(answer, message.conversation)

def menu(message):
    who_name = message.who_name
    greeting = f'Olá {who_name},\n'
    content = 'Precisa de ajuda?\nUse alguns dos comandos abaixo:\n' \
    '!noticia\n!ajuda.'
    mac.send_message(answer, message.conversation)
