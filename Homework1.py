#Задача 2: Найдите сумму цифр трехзначного числа.


#print('Введите трехзначное  число:')
#a = int(input())
#b1 = a % 10
#a = a //10
#b2 = a % 10
#a = a // 10
#print("Сумма цифр числа составляет:", a + b1 + b2)


#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?


#print('Введите количество журавликов:')
#a = int(input())
#if a % 2 == 0:
    #e = (a//3)*2
    #d = (e//2)//2
    #c = d
    #print("Петя сделал журавликов:", c)
    #print("Сережа сделал журавликов:", d)
    #print("Катя сделала журавликов:" , e)
#else:
    #print("Значение введено некорректно!")
    

#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

#print("Введите число билетика:")
#n = (input())
#a = int(n[0])
#b = int(n[1])
#c = int(n[2])
#d = int(n[3])
#e = int(n[4])
#f = int(n[5])

#g = a + b + c
#h = d + e + f

#if g == h:
    #print("Yes, it's a lucky ticket!")
#else:
    #print("No, it's an unlucky ticket.")

#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).


#print('Введите ширину шоколадки:')
#n = int(input())
#print('Введите длину шоколадки:')
#m = int(input())
#print('Введите количество долек:')
#k = int(input())
#if n *m > k:
    #if k % n == 0 or k % m == 0:
        #print ("Можно отломить долек:", k)
    #else:
        #print("Разделить шоколадку невозможно!")
    