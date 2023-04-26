import os
from time import sleep
#os.system('cls')
class Jogao:

    def __init__(self, nick):
        #info player
        self._jogador_nick = nick
        self.jogador_level = 0
        self.jogador_xp = 0
        self.jogador_hp = 100
        #skills player
        
        self.Menu()

    def checar_xp(self, xp_obtido):
        self.jogador_xp += xp_obtido
        if self.jogador_xp >= 100:
            self.jogador_xp -= 100
            self.jogador_level +=1
        
    #skills jogador
    def bola_de_fogo(self):
        return 250
    
    def ataque_rapido(self):
        return 100
    
    #navegacao
    def Menu(self):
        while True:
            os.system('cls')
            print("""1
================
JOGO DE RPG FDS
===============\n
            """)
            user = int(input("[MENU DE OPCOES]\n[1] info jogador\n[2] arenas\n[3] sair do jogo\n.. "))
            match user:
                case 1:
                    os.system('cls')
                    self.info_jogador()
                case 2:
                    os.system('cls')
                    self.arenas_menu()
                case 3:
                    os.system('cls')
                    print("fechando...")
                    sleep(2)
                    exit()
                case _:
                    os.system('cls')
                    print("comando invalido, tente novamente\n")
                    continue

    def info_jogador(self):
        while True:
            print("="*20)
            print(f"NICK: {self._jogador_nick}\nLEVEL: {self.jogador_level}\nXP: {self.jogador_xp}\nHP: {self.jogador_hp}")
            print("="*20)
            print("\n")
            user = int(input("[1] voltar\n.. "))
            if user == 1:
                self.Menu()
            else:
                os.system('cls')
                print("comando invalido")
                continue

    def arenas_menu(self):
        while True:
            print("="*20)
            print("ARENAS PVE")
            print("="*20)
            print("\nMONSTROS DISPONIVEIS")
            print("-"*len("MONSTROS DISPONIVEIS"))
            print("\n")
            user = int(input("[1] CEIFADOR DE ALMAS\ninfos: ao matar +xp[100]\n\n[2] FANTASMA DE GUERREIRO NORDICO\ninfos: ao matar +xp[500]\n.. "))
            if user == 1:
                self.batalhar_ceifadorAlmas()
            elif user == 2:
                self.batalhar_guerreiroNordico()
            else:
                print("comando invalido.")
                continue

    
    #arenas
    def batalhar_ceifadorAlmas(self):
        cont = 0  #contador hits
        hp_ceifador = 1000
        while True:
            os.system('cls')
            print("💥💥💥💥💥💥💥💥💥")
            print("O mais temido coveiro do cemiterio das 7 noites chegou\n💀Ceifador de Almas: Boa noite companheiro, esta eh uma otima noite pra derramar um pouco de sangue nao acha?!\n")
            
            print("="*22)
            print(f"💀CEIFADOR DE ALMAS:\nHP: {hp_ceifador}\n")
            print(f"🥷{self._jogador_nick}:\nHP: {self.jogador_hp}\n\n")
            print(f"SKILLS DISPONIVEIS:\n[1] ATAQUE RAPIDO 🗡100\n[2] BOLA DE FOGO 🗡250")
            print("="*22)

            #dano no monstro
            escolha_ataque = int(input("\nATACAR: "))
            if escolha_ataque == 1:
                hp_ceifador -= self.ataque_rapido()
            elif escolha_ataque == 2:
                hp_ceifador -= self.bola_de_fogo()
            else:
                print("skills nao aprendida.")
                continue

            if hp_ceifador <= 0:
                break
            
            cont+=1

        print("\n💀Ceifador de Almas: Vo...vo..voce ira pagar da proxima vez...\n")
        print("🟢VOCE ACABA DE MATAR 💀CEIFADOR DE ALMAS\n🟢xp+[100]")
        if cont <= 4:
            print("como voce matou o monstro com 4 ou menos hits, ganhara um bonus de xp+[50]\n")
            self.checar_xp(50)
        self.checar_xp(100)
        
        voltar_menu = int(input("\n[1] voltar ao menu\n[2] batalhar novamente\n.. "))
        if voltar_menu == 1:
            self.Menu()
        elif voltar_menu == 2:
            self.batalhar_ceifadorAlmas()
        else:
            print("comando invalido, voltando para o menu...")
            print(sleep(3))
            self.Menu()

if __name__ == "__main__":
    Jogao('Lorenzo')