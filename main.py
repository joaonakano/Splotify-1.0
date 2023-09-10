import random, pygame, os, time


os.chdir('./music')
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)


# Pilha - Funções
def is_empty(pilha):
    return len(pilha) == 0


def pop(pilha):
    if not is_empty(pilha):                                               # Pilha - Is_empty
        return pilha.pop()
    else:
        return "A pilha está Vazia."


def push(pilha, elemento):
    return pilha.append(elemento)


def peek(lista, tipo):
    if is_empty(lista):
        return "A lista está Vazia."
    elif tipo == "pilha":
        return lista[-1]
    elif tipo == "lista":
        return lista[0]   


# Fila - Funções
def enqueue(fila, elemento):
    return fila.append(elemento)


def dequeue(fila):                              
    if len(fila) == 0:
        return "A fila está vazia."
    else:
        return fila.pop(0)


musicas = []                                                             # Fila Vazia
enqueue(musicas,'kill_again.mp3')                                        # Fila - Inserção
enqueue(musicas,'eazy_duz_it.mp3')
enqueue(musicas,'check_yo_self.mp3')
enqueue(musicas,'chamber_of_reflection.mp3')
enqueue(musicas,'2_much.mp3')
enqueue(musicas,'hey_ya.mp3')


playlist1, playlist2 = [],[]                                             # Pilhas Vazias. 
for i in range(3):
    musica = dequeue(musicas)                                            # Fila - Remoção
    push(playlist1, musica)                                              # Pilha - Inserção - 3 primeiras músicas.

for i in range(3):
    musica = dequeue(musicas)                                            # Fila - Remoção
    push(playlist2, musica)                                              # Pilha - Inserção - Músicas restantes.


def limparTela():
    _ = os.system('clear' if os.name == 'posix' else 'cls')


def timer(x):
    time.sleep(x)


def ListaMusicas(playlist):
    limparTela()
    print("┌──────────────────────────────┐\n", " "*7, "- ̗̀  MÚSICAS ̖́  -", "\n└──────────────────────────────┘")
    print("\n▶ PLAYLIST1:", end=" ")
    
    for i in range(len(playlist)): # [0, 1, 2]
        print(playlist[i].replace(".mp3"," / "), end="")                 # Substitui o mp3 por " / "
    print()                                                              # Fecha o print (end=" ") para nao misturar com futuros prints

    print("\n▶ PLAYLIST2:", end=" ")
    for i in range(len(playlist2)):
        print(playlist2[i].replace(".mp3"," / "), end="")
    print()
    input("\n\nPressione ENTER para sair da tela...")                    # Frear o codigo
    StartMenu()


def StartMenu():
    opcoes_menu = []                                                     # Pilha Vazia
    push(opcoes_menu, "╚════════════════════════╝\n")                    # Pilha - Inserção
    push(opcoes_menu, " * [3] - Fechar")
    push(opcoes_menu, " * [2] - Lista de Músicas")
    push(opcoes_menu, " * [1] - Music")
    push(opcoes_menu, "           MENU ")
    push(opcoes_menu, "\n╔════════════════════════╗")
    limparTela()
    print("""
/$$$$$$            /$$             /$$     /$$  /$$$$$$          
/$$__  $$          | $$            | $$    |__/ /$$__  $$         
| $$  \__/  /$$$$$$ | $$  /$$$$$$  /$$$$$$   /$$| $$  \__//$$   /$$
|  $$$$$$  /$$__  $$| $$ /$$__  $$|_  $$_/  | $$| $$$$   | $$  | $$
\____  $$| $$  \ $$| $$| $$  \ $$  | $$    | $$| $$_/   | $$  | $$
/$$  \ $$| $$  | $$| $$| $$  | $$  | $$ /$$| $$| $$     | $$  | $$
|  $$$$$$/| $$$$$$$/| $$|  $$$$$$/  |  $$$$/| $$| $$     |  $$$$$$$
\______/ | $$____/ |__/ \______/    \___/  |__/|__/      \____  $$
        | $$                                            /$$  | $$
        | $$                                           |  $$$$$$/ 
        |__/                                            \______/ 
                    * JEB Productions *""")
    timer(1)
    for i in range(len(opcoes_menu)):
        print(pop(opcoes_menu))                                          # Pilha - Remoção + Is_Empty
    menuOpcoes()


def menuOpcoes():
    escolha = (input("Escolha uma opção: "))
    if escolha == "1":
        menuSelecaoPlaylist()
    elif escolha == "2":
        ListaMusicas(playlist1)
    elif escolha == "3":
        print("""
              
 ▄▄▄▄ ▓██   ██▓▓█████ 
▓█████▄▒██  ██▒▓█   ▀ 
▒██▒ ▄██▒██ ██░▒███   
▒██░█▀  ░ ▐██▓░▒▓█  ▄ 
░▓█  ▀█▓░ ██▒▓░░▒████▒
░▒▓███▀▒ ██▒▒▒ ░░ ▒░ ░
▒░▒   ░▓██ ░▒░  ░ ░  ░
 ░    ░▒ ▒ ░░     ░   
 ░     ░ ░        ░  ░
      ░░ ░            
""")
        return 0
    else:
        print("Opção inválida. Escolha novamente.")
        timer(1.5)
        limparTela()
        StartMenu()


playlist_selecionada = []
def menuSelecaoPlaylist():
    global playlist_selecionada
    limparTela()
    print(" Playlists Encontradas no Sistema: \n* [1] Playlist1\n* [2] Playlist2")
    user_selection = int(input("Digite o número da playlist: "))
    if user_selection == 1:
        playlist_selecionada = playlist1
    elif user_selection == 2:
        playlist_selecionada = playlist2
    else:
        limparTela()
        print("""              
┳┓┳┳┳┳┓┏┓┳┓┏┓  ┏┓┳┓┳┓┏┓┳┓┏┓
┃┃┃┃┃┃┃┣ ┣┫┃┃  ┣ ┣┫┣┫┣┫┃┃┃┃
┛┗┗┛┛ ┗┗┛┛┗┗┛  ┗┛┛┗┛┗┛┗┻┛┗┛                      
""")
        timer(1.5)
        menuSelecaoPlaylist()                # Recursividade - O Menu de seleção retorna se o input for incorreto
    for i in range (10):
        limparTela()
        print(f"A proxima música será: {peek(playlist_selecionada, 'lista')}")                   # Fila - Peek - Primeira Música [0]
        timer(0.2)
    selecaoDeMusica(playlist_selecionada)


indice = 0
musica_atual = ""
def selecaoDeMusica(tipo):
    global indice, musica_atual, playlist_selecionada
    if tipo == "proxima":
        if indice is not playlist_selecionada.index(playlist_selecionada[-1]):
            indice = indice + 1
        else:
            indice = 0
    elif tipo == "anterior":
        if indice is not playlist_selecionada.index(playlist_selecionada[0]):
            indice = indice - 1
        else:
            indice = playlist_selecionada.index(playlist_selecionada[-1])
    elif tipo == "random":
        for i in range(1):
            indice = random.randint(0, len(playlist_selecionada) - 1)
    musica_atual = playlist_selecionada[indice]
    return tocarMusica(musica_atual)


def tocarMusica(musica):
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()
    playerMusicaMenu()


def playerMusicaMenu():
    global indice
    verificador = 0
    while verificador != 1:
        limparTela()
        print(f"""\nFunções disponiveis:\n* [1]  ▶ Play{" "*13}* [2] ⏸  Pause\n* [3] 🔁 Replay {" "*10}* [4] 🔄 Loop\n* [5] ⏭️  Próxima{" "*10}* [6] ⏮️  Retornar\n* [7] 🔀 Aleatório{" "*8}* [8] ⚙️  Escolher Outra Playlist\n* [9] 📄 Ver a última música\n\n* [0] 🚪 Sair""")
        term = int(input("Digite o número da opção: "))
        match term:
            case 0:
                pygame.mixer.music.stop()
                limparTela()
                verificador = 1
                break
            case 1:
                pygame.mixer.music.unpause()
            case 2:
                pygame.mixer.music.pause()
            case 3:
                pygame.mixer.music.play()
            case 4:
                pygame.mixer.music.play(-1)
            case 5:
                selecaoDeMusica("proxima")
            case 6:
                selecaoDeMusica("anterior")
            case 7:
                selecaoDeMusica("random")
            case 8:
                pygame.mixer.music.stop()
                indice = 0
                menuSelecaoPlaylist()
            case 9:
                limparTela()
                print("\nÚltima música da playlist →",peek(playlist_selecionada, "pilha"))                          # Pilha - Peek
                input("\nPressione Enter para sair.")
            case _:
                limparTela()
                print("Opção inválida!")
                timer(1)
                playerMusicaMenu()
    StartMenu()


StartMenu()  # Inicialização