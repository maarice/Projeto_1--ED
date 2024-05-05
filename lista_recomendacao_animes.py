class Noh:
    def __init__(self, anime):
        self.anime = anime
        self.proximo_anime = None

class Lista_animes:
    def __init__(self):
        self.cabeca = None

    def inserir_anime(self, anime):
        if not self.cabeca:
            self.cabeca = Noh(anime)
        else:
            proximo_noh = self.cabeca
            while proximo_noh.proximo_anime:
                proximo_noh = proximo_noh.proximo_anime
            proximo_noh.proximo_anime = Noh(anime)

    def remover_anime(self, anime):
        if not self.cabeca:
            return

        if self.cabeca.anime == anime:
            self.cabeca = self.cabeca.proximo_anime
            return

        proximo_noh = self.cabeca

        while proximo_noh.proximo_anime:
            if proximo_noh.proximo_anime.anime == anime:
                proximo_noh.proximo_anime = proximo_noh.proximo_anime.proximo_anime
                return
            proximo_noh = proximo_noh.proximo_anime

    def mostra_anime(self):
        print('\nEsta é sua lista de animes:')
        proximo_noh = self.cabeca

        while proximo_noh:
            print(proximo_noh.anime)
            proximo_noh = proximo_noh.proximo_anime

def menu_anime():
    print('\n============ Sistema de recomendação de animes ============')
    print('1. Adicionar anime')
    print('2. Remover anime')
    print('3. Mostrar lista de animes') 
    print('4. Sair')

anime_lista = Lista_animes()

while True:
    menu_anime()
    escolha_menu = input('Escolha uma das opções acima: ')

    if escolha_menu == '1':
        anime = input('Digite o nome do anime a ser adicionado: ')
        anime_lista.inserir_anime(anime)

    elif escolha_menu == '2':
        anime = input('Digite o nome do anime a ser removido: ')
        anime_lista.remover_anime(anime)

    elif escolha_menu == '3':
        print('\nLista de animes:')
        anime_lista.mostra_anime()
        continuar = input('Deseja acessar o menu? [S]im ou [N]ão: ')
        if continuar == 'S':
            continue
        elif continuar == 'N':
            break
        else:
            print('Escolha uma opção válida!')

    elif escolha_menu == '4':
        print('Volte sempre!')
        break

    else:
        print('Opção inválida.')
        print('Tente novamente!')
