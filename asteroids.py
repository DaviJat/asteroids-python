# Author: Davi Jatobá Galdino
# Date of conclusion: April 26th 2022

# Autor: Davi Jatobá Galdino
# Componente Curricular: Algoritmos I
# Concluido em: 26/04/2021
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.


from random import randint
from time import sleep
import keyboard
import os

# Global Variables
# Variáveis Globais
initial_menu = 1
ship_row = 29
ship_column = 15
asteroid_row = 0
asteroid_column = randint(0, 21)
projectile_row = 27
projectile_column = 26
score = 0
asteroid_counter = 0
space_key = False
first_score = 0
second_score = 0
third_score = 0
fourth_score = 0
fifth_score = 0
first_place = 'None'
second_place = 'None'
third_place = 'None'
fourth_place = 'None'
fifth_place = 'None'


# Function to erase inputs that were registered during the game
# Função para apagar inputs que eram registrados durante o jogo
def erase_inputs():
    while True:
        for i in range(0,1):
            keyboard.press('enter')
        input('')
        break

# Function responsible for showing the content of 'options', and also controlling the commands inside it
# Função reponsável por mostrar o conteúdo do 'sobre', e também controlar os comandos dentro dele
def show_options():
    options_menu = 1
    global initial_menu
    while options_menu == 1:
        os.system('cls')
        print('==== Options ====\n\n    1 - Story\n    2 - Tutorial\n    3 - Go back')
        options_menu = input('\nYour choice: ').strip()
        os.system('cls')
        if options_menu == '1':
            print ('Story:')
            print('''\nYear 3021 - A.D. - The collision of Planet Upsilon - 431 with comet Faye, generated a devastating explosion, scattering
debris across the Milky Way, Earth scientists on duty have observed this unrest in the universe, and
identified that a asteroid rain would approach the Earth's atmosphere in a few years. Seen that,
all the nations of the world have come together to develop a ship, with projectiles capable of extinguishing asteroids. With
tight time, they estimated that they would be able to build just one ship for this mission, and to decide which one will
define the fate of the earth, called the best pilots in the world to simulate this confrontation with the
asteroids, and you have been selected to participate in these tests. Do your best, and be the one to save everyone
in the Earth's ecosystem.''')
            print('\Press "ESC" to go back')
            keyboard.wait('esc')
            options_menu = 1
        elif options_menu == '2':
            print('How to Play:')
            print('''\n- To control the ship use the keys "< . >" (left key, and right key).
- Press space to launch projectile.
- Only one projectile can be fired at a time, so DON'T MISS (Hitting an asteroid resets the shots). 
- The game ends when 10 asteroids reach the end without being destroyed, or when they reach the ship.
- Pressing the "Esc" key immediately ends the game.
- Each destroyed asteroid will give you 10 points that will be counted in the end to define the records.''' )
            print('\nPress "ESC" to go back')
            keyboard.wait('esc')
            options_menu = 1
        elif options_menu == '3':
            initial_menu = 1
            options_menu = 0
        else:
            print('Invalid option')

# Function that prints the name of the recordist player, and their respective score
# Função que printa o nome do jogador dado, e a sua respectiva pontuação
def show_record():
    global first_score
    global second_score
    global third_score
    global fourth_score
    global fifth_score
    global first_place
    global second_place
    global third_place
    global fourth_place
    global fifth_place
    global initial_menu
    os.system('cls')
    print('========= Records ==========')
    print('Player ============ Score')
    print(f'{first_place}   ============   {first_score}')
    print(f'{second_place}   ============   {second_score}')
    print(f'{third_place}   ============   {third_score}')
    print(f'{fourth_place}   ============   {fourth_score}')
    print(f'{fifth_place}   ============   {fifth_score}')
    print('=============================')
    print('Press "ESC" to go back to main menu')
    keyboard.wait('esc')
    initial_menu = 1

# Function responsible for restarting the asteroid and the projectile when they collide
# Função responsável por reiniciar o asteroid e o projétil quando entram em colisão
def to_score():
    global asteroid_column
    global asteroid_row
    global projectile_row
    global projectile_column
    global space_key
    global score
    asteroid_column = randint(0, 21)
    asteroid_row = 0
    projectile_row = 27
    projectile_column = 26
    space_key = False
    score += 1

# Function that launches the projectile when the 'space' key is pressed
# Função que adiciona o projétil a quando a tecla 'espaço' é pressionada
def projectile_generator():
    global space_key
    global projectile_column
    global ship_collision
    global projectile_row
    if space_key == False:
        if keyboard.is_pressed('space'):
            space_key = True
            projectile_column = ship_column
    if space_key == True:
        if projectile_row != 5:
            matrix[projectile_row][projectile_column] = 'o'
            projectile_row -= 1
        else:
            projectile_row = 27
            space_key = False


# Print the score inside the game matrix
# Print da pontuação dentro da matriz do jogo
def matrix_score():
    global score
    global asteroid_counter
    matrix[30][1] = 'Score:'
    matrix[30][2] = str(score)
    matrix[31][1] = 'Not destroyed asteroids:'
    matrix[31][3] = str(asteroid_counter)


# End game menu, asks if the user wants to try again, and resets the game data (Score, Asteroid Counter, ...)
# Menu final de jogo, pergunta se o usuário quer tentar novamente, e reinicia os dados de jogo (Score, Contador de Asteroids, ...)
def second_try():
    global try_again
    global asteroid_counter
    global projectile_column
    global projectile_row
    global space_key
    global ship_collision
    global score
    global asteroid_row
    global initial_menu
    while try_again != '1' and try_again != '2':
        print('\n====== Try Again? ======')
        print('== 1 - Yes ======= No - 2 ==')
        try_again = (input('Your choice: ')).strip()
        if try_again == '1':
            asteroid_counter = 0
            projectile_column = 26
            projectile_row = 27
            space_key = False
            ship_collision = 1
            score = 0
            asteroid_row = 0
            print('3...')
            sleep(0.8)
            print('2...')
            sleep(0.8)
            print('1...')
            sleep(0.8)
            initial_menu = '1'
        elif try_again == '2':
            asteroid_counter = 0
            projectile_column = 26
            projectile_row = 27
            space_key = False
            ship_collision = 1
            score = 0
            asteroid_row = 0
            initial_menu = 1
        else:
            print('\n===== Invalid option =====')
            sleep(1.5)
            os.system('cls')


# Print Game Over and the reason
# Printa GAME OVER e o motivo disso ter acontecido
def gameover_message():
    global ship_collision
    if ship_collision == 0:
        print('======= GAME OVER =======')
        print('An asteroid hit your ship')
        sleep(2)
        os.system('cls')
    elif ship_collision == 1:
        print('============== GAME OVER ===============')
        print(f'You missed {asteroid_counter} asteroids')
        sleep(2)
        os.system('cls')
    else:
        print('========= GAME OVER ==========')
        print('Game terminated by ESC command')
        sleep(2)
        os.system('cls')


# Reset values ​​when 'esc' is pressed to end the game
# Reinicia os valores quando 'esc' é apertado para finalizar o jogo
def press_esc():
    global asteroid_counter
    asteroid_counter = 0
    global projectile_row
    projectile_row = 27
    global projectile_column 
    projectile_column = 26
    global space_key
    space_key = False
    global ship_collision
    ship_collision = 3
    global asteroid_row
    asteroid_row = 0


# Function to record the score in descending order and receive the player's nickname
# Função para registrar o score em ordem decrescente e recever o nick do jogador
def recordes():
    global first_score
    global second_score
    global third_score
    global fourth_score
    global fifth_score
    global first_place
    global second_place
    global third_place
    global fourth_place
    global fifth_place
    if score >= first_score:
        fifth_place = fourth_place
        fourth_place = third_place
        third_place = second_place
        second_place = first_place
        first_place = input('NEW RECORD - Write your nick (5 characters): ')
        fifth_score = fourth_score
        fourth_score = third_score
        third_score = second_score
        second_score = first_score
        first_score = score
    elif score >= second_score:
        fifth_place = fourth_place
        fourth_place = third_place
        third_place = second_place
        second_place = input('NEW RECORD - Write your nick (5 characters): ')
        fifth_score = fourth_score
        fourth_score = third_score
        third_score = second_score
        second_score = score
    elif score >= third_score:
        fifth_place = fourth_place
        fourth_place = third_place
        third_place = input('NEW RECORD - Write your nick (5 characters): ')
        fifth_score = fourth_score
        fourth_score = third_score
        third_score = score
    elif score >= fourth_score:
        fifth_place = fourth_place
        fourth_place = input('NEW RECORD - Write your nick (5 characters): ')
        fifth_score = fourth_score
        fourth_score = score
    elif score >= fifth_score:
        fifth_place = input('NEW RECORD - Write your nick (5 characters): ')
        fifth_score = score

# Control the ship by the <,> keyboard keys, and reposition it in the matrix
# Controle da nave pelas teclas <,> do teclado, e a reposiciona na matriz
def ship_position(column, movement):
    if movement == 'right':
        if column != 23:
            column += 1
            return column
        else:
            return 23
    if movement == 'left':
        if column != 2:
            column -= 1
            return column
        else:
            return 2
 
# Reset the asteroid when it reaches the last row of the matrix
# Reset do asteroid quando ele chega na ultima linha da matriz
def posicao_asteroid(row):
    if row != 29:
        row += 1
        return row
    else:
        return 0


# Print of the ship in the matrix
# Print da nave na matriz
def ship_format():
    matrix[ship_row][ship_column - 1] = '/'
    matrix[ship_row][ship_column] = '_'
    matrix[ship_row][ship_column + 1] = '\\'
    matrix[ship_row - 1][ship_column] = '^'
    return


# Print of the asteroid in the matrix
# Print do asteroid na matriz
def asteroid_format():
    matrix[asteroid_row][asteroid_column + 1] = '/'      
    matrix[asteroid_row][asteroid_column + 2] = '*'     
    matrix[asteroid_row][asteroid_column + 3] = '\\'
    matrix[asteroid_row + 1][asteroid_column] = '/'
    matrix[asteroid_row + 1][asteroid_column + 1] = '*'
    matrix[asteroid_row + 1][asteroid_column + 2] = '*'
    matrix[asteroid_row + 1][asteroid_column + 3] = '*'
    matrix[asteroid_row + 1][asteroid_column + 4] = '\\'
    matrix[asteroid_row + 2][asteroid_column] = '*'
    matrix[asteroid_row + 2][asteroid_column + 1] = '*'
    matrix[asteroid_row + 2][asteroid_column + 2] = '*'
    matrix[asteroid_row + 2][asteroid_column + 3] = '*'
    matrix[asteroid_row + 2][asteroid_column + 4] = '*'
    matrix[asteroid_row + 3][asteroid_column ] = '\\'
    matrix[asteroid_row + 3][asteroid_column + 1] = '*'
    matrix[asteroid_row + 3][asteroid_column + 2] = '*'
    matrix[asteroid_row + 3][asteroid_column + 3] = '*'
    matrix[asteroid_row + 3][asteroid_column + 4] = '/'
    matrix[asteroid_row + 4][asteroid_column + 1] = '\\'
    matrix[asteroid_row + 4][asteroid_column + 2] = '*'
    matrix[asteroid_row + 4][asteroid_column + 3] = '/'
    return


# Check if the projectile coordinate is the same as the asteroid coordinate, declaring collision
# Verifica se a coordenada do projétil é a mesma coordenada do asteroid, declarando colisão
def check_projectile_collision():
    coordenada_projetil = matrix[projectile_row][projectile_column]
    if coordenada_projetil == matrix[asteroid_row + 4][asteroid_column + 1] or \
    coordenada_projetil == matrix[asteroid_row + 4][asteroid_column + 2] or \
    coordenada_projetil == matrix[asteroid_row + 4][asteroid_column + 3] or \
    coordenada_projetil == matrix[asteroid_row + 3][asteroid_column] or \
    coordenada_projetil == matrix[asteroid_row + 3][asteroid_column + 1] or \
    coordenada_projetil == matrix[asteroid_row + 3][asteroid_column + 2] or \
    coordenada_projetil == matrix[asteroid_row + 3][asteroid_column + 3] or \
    coordenada_projetil == matrix[asteroid_row + 3][asteroid_column + 4] or \
    coordenada_projetil == matrix[asteroid_row + 2][asteroid_column] or \
    coordenada_projetil == matrix[asteroid_row + 2][asteroid_column + 4]:
        return True
    else:
        return False
    

# Check if the ship coordinate is the same as the asteroid coordinate, declaring collision
# Verifica se a coordenada da nave é a mesma coordenada do asteroid, declarando colisão
def check_ship_collision():
    if matrix[ship_row][ship_column - 1] == '*' or \
    matrix[ship_row][ship_column] == '*' or \
    matrix[ship_row][ship_column + 1] == '*' or \
    matrix[ship_row - 1][ship_column] == '*':
        return True
    else:
        return False

    
# Start of the program's initial menu, through a while loop
# Início do menu inicial do programa, através de um loop While
while initial_menu == 1:
    os.system('cls')
    print('==== ASTEROIDS ====\n\n    1 - Play\n    2 - Record\n    3 - About\n    4 - Exit')
    initial_menu = input('\nYour option: ').strip()
    # Ship collision = variable to identify if the ship was hit
    # Colisão nave = variável para identificar se a nave foi atingida
    ship_collision = 1
    asteroid_counter = 0
    if initial_menu == '1':
        while initial_menu == '1':
            try_again = 0
            while asteroid_counter < 10 and ship_collision == 1:
                os.system('cls')
                matrix = []
                for i in range(0, 32):
                    linha = []
                    for j in range(0, 27):
                        linha.append(' ')
                    matrix.append(linha)
                # Ship generator
                # Gerador Nave
                ship_format()
                # Ateroid generator
                # Gerador Asteroid
                asteroid_format()
                # Projectile generator
                # Gerador Projetil
                projectile_generator()
                matrix_score()
                # Matrix print
                # Print da matriz
                for l in matrix:
                    print(''.join(l))
                # Receives commands and performs the respective functions
                # Recebe os comando e realiza as funções respectivas
                if keyboard.is_pressed('esc'):
                    press_esc()
                    break
                if check_ship_collision() == True:
                    ship_collision = 0
                if keyboard.is_pressed('right'):
                    direcao = 'right'
                    ship_column = ship_position(ship_column, direcao)
                if keyboard.is_pressed('left'):
                    direcao = 'left'
                    ship_column = ship_position(ship_column, direcao)
                if check_projectile_collision() == True:
                    to_score()
                if asteroid_row + 4 == 29:
                    # Asteroid reset
                    asteroid_counter += 1
                    asteroid_row = 0
                    asteroid_column = randint(0, 21)
                if check_ship_collision == True:
                    ship_collision = 0
                asteroid_row = posicao_asteroid(asteroid_row)
                sleep(0.03)
            erase_inputs()
            gameover_message()
            recordes()
            second_try()
    # Other main menu options
    # Outras opções do menu principal
    elif initial_menu == '2':
        show_record()
    elif initial_menu == '3':
        show_options()
    elif initial_menu == '4':
        os.system('cls')
        print('============================')
        print('==== Thanks for playing ====')
        print('============================')
    else:
        print('\n== Invalid option ==')
        sleep(1.5)
        initial_menu = 1
        os.system('cls')