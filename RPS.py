# Rock Paper Scissors
import random

box = ['Rock', 'Paper', 'Scissors']
match = 1
ch = True
pl_score = 0
cscore = 0

while ch:
    print('Match #', match, sep='')
    player = input('Rock/Paper/Scissors! [Rr/Pp/Ss]: ')
    if player not in ['P', 'p', 'R', 'r', 'S', 's']:
        player = input("Re-enter [R/r,P/p,S/s]: ")
    if player in ['R', 'r']:
        player = 'Rock'
    elif player in ['p', 'P']:
        player = 'Paper'
    elif player in ['S', 's']:
        player = 'Scissors'
    computer = random.choice(box)
    print('Player :', player)
    print('Computer :', computer)

    if player == 'Rock' and computer == 'Scissors':
        print('Player wins')
        pl_score += 1
    if player == 'Scissors' and computer == 'Paper':
        print('Player wins')
        pl_score += 1
    if player == 'Paper' and computer == 'Rock':
        print('Player wins')
        pl_score += 1
    if player == 'Scissors' and computer == 'Rock':
        print('Computer wins')
        cscore += 1
    if player == 'Paper' and computer == 'Scissors':
        print('Computer wins')
        cscore += 1
    if player == 'Rock' and computer == 'Paper':
        print('Computer wins')
        cscore += 1
    elif player == computer:
        if pl_score > cscore:
            print(pl_score, cscore, 'Player Wins!')
        else:
            print('Computer wins.')
    print('[Score:', 'Player -', pl_score, ', Comp. -', cscore ,']')

    match += 1

    ch = input('Enter-exit, any_key-continue: ')

    print('___________________________________________________________________________')