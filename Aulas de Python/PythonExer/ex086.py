 #* Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
 #*                         [ 1 ] [ 2 ] [ 3 ]
 #*                         [ 4 ] [ 5 ] [ 6 ]
 #*                         [ 7 ] [ 8 ] [ 9 ]
 #* No final, mostre a matriz na tela, com formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')      #* É possível formatar uma lista dessa forma, dentro de um for.
    print()