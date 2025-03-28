#Variável que define o funcionamento do aplicativo.
usr_jogando = True

#FPS do programa
FPS = 60

#Sobre a tela do jogo em geral.
tam_tela = tam_tela_x, tam_tela_y = 1000, 800

#Variável armazenando a tela atual do jogo. Começa com menu.
tela_atual = 'menu'

#Sobre a tela principal (Menu).

#Nome da janela.
str_janela_menu = 'Chess CIn'

#Sobre o título do Menu.
str_fonte_menu = 'Ubuntu' #Uma string com o nome da fonte do título.
tam_fonte_menu = 48
str_menu = 'Bem-vindo ao Chess CIn!' #Nome do título que aparecerá como principal.
cor_menu = (0, 0, 0) #Define a cor do título do menu como azul.

#Sobre o botão de Jogar. Definindo tamanho, cor e posição do botão Jogar.
tam_jogar = tam_jogar_x, tam_jogar_y = 300, 100 #Define o tamanho do botão. Ordem: largura e comprimento.
jogar_x = (tam_tela_x) / 2 - (tam_jogar_x / 2) #Define posição x (horizontal) do botão Jogar referente ao menu.
jogar_y = (tam_tela_y) / 2 - (tam_jogar_y / 2) #Define posição y (vertical) do botão Jogar referente ao menu.
cor_jogar = (255, 0, 0) #Define que a cor do botão 'Jogar' será vermelha.

#Sobre o texto do botão jogar. Definindo string, cor e 
str_jogar = 'Jogar'
cor_txt_jogar = (0, 0, 0) #Define que a cor do texto 'Jogar' no botão será preta.
str_fonte_jogar = 'Ubuntu'
tam_fonte_jogar = 30

#Sobre a tela do xadrez.

#Matriz que vai armazenar um grupo de objetos da classe Casa, que serão as 64 casas do jogo. Começa vazia, pois o tabuleiro ainda não foi desenhado.
matriz_casas = []

#Casa de origem e de destino selecionadas. Ambas começam vazias. Ex.: Se o usuário clica na casa a7, e além disso ele havia clicado anteriormente na casa a1, onde há uma torre, a torre deve ser movida de a1 para a7.
casa_origem = ()
casa_destino = ()

#Um dicionário de mapeia os índices das colunas às colunas do xadrez.
dict_colunas = {
    0:'a',
    1:'b',
    2:'c',
    3:'d',
    4:'e',
    5:'f',
    6:'g',
    7:'h',
}
