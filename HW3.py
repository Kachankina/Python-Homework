# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве из случайных чисел. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. Последняя строка содержит число X


# N = abs(int(input('Number of  elements:' )))
# L = input('Enter elements using spacebar:').split()
# L_numb = list(map(int,L))
# if len(L_numb) !=  N:
#     print("Not Correct!")
# else:
#     X = int(input("Insert number X:"))
#     count = 0
#     for i in range(N):
#         if L_numb[i] == X:
#             count += 1
#     print(f'{X} meets {count} times')

# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n)
# самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N
# – количество элементов в массиве. Последняя строка содержит число X

# from random import randint

# N = abs(int(input("Insert number of elements:")))
# L = []
# for i in range (N):
#     L.append(randint(1,N))
# print(L)
# if len(L) != N or N == 0:
#     print("Not correct!")
# else:
#     X = int(input("Insert number for comparison: "))
#     min = abs(X - L[X-1])
#     number = 0
#     for i in range (1, N):
#         count = abs(X - L[i])
#         if count < min:
#             min = count
#             number = i
#     print(f'Number {L[number]} close to number {X} ')
        

#  Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет
# определенную ценность. В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо
# только английские, либо только русские буквы.

# eng = {1:'AEIOULNSTR',
#       	2:'DG',
#       	3:'BCMP',
#       	4:'FHVWY',
#       	5:'K',
#       	8:'JZ',
#       	10:'QZ'}
# rus = {1:'АВЕИНОРСТ',
#       	2:'ДКЛМПУ',
#       	3:'БГЁЬЯ',
#       	4:'ЙЫ',
#       	5:'ЖЗХЦЧ',
#       	8:'ШЭЮ',
#       	10:'ФЩЪ'}
# N = abs(int(input('Введите 1, если в английской раскладке, либо 0, если в русской: ')))
# word = input('Введите слово: ').upper()
# if N == 1:
# 	print('За это слово вы получаете', sum([k for i in word for k, v in eng.items() if i in v]), 'очков')
# elif N == 0:
# 	print('За это слово вы получаете', sum([k for i in word for k, v in rus.items() if i in v]), 'очков')
# else:
#     print('Вы играете не по правилам!')