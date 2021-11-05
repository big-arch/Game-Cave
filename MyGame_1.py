import random
import time

friendlyDoor = random.randint(1,2)


def intro():
    print("Приветствую тебя путник, как твое имя?")
    print()
    myName = input()
    print(f"Здравствуй {myName} \n давно у моих дверей не было ни кого")
    print()
    time.sleep(1)
    print("Тут две двери, за одной богатство \n а за другой кто то поопаснее тебя")
    time.sleep(1)


def doorChoose():
    door = ""
    while door != "1" and door != "2":
        print("В какую дверь ты войдешь? 1-ю или 2-ю")
        door = input()

    return door


def way(doorChoose):
    print("Дверь открывается очень медлено и со скрипом \n")
    time.sleep(1)
    print("Проходи, дверь открыта")
    time.sleep(1)
    print()
    print("Дым заполняет комнату, в далеке вы видите силует, но его не разобрать")
    time.sleep(1)
    print()
    print(f"Подойдете? (да \ нет)")


    go = ""
    while go != 'да':
        go = input()
        if go != "да" and go != 'нет':
            print("Отвечай да или нет")
        elif go == "нет":
            print("Ты слишком слаб для этого испытания, уходи и больше не приходи НИКОГДА")
            break
        else:
            time.sleep(1)
            print("Вы медленно подходите к силуету и ....")

    time.sleep(1)

    if go == 'да':
        if doorChoose != str(friendlyDoor):
            print()
            print("Дым исчезает, и ты видешь сундук с золотом")
            print("Ты можешь его открыть и забрать все золото, быстро уходи а то дракон найдет тебя")
            return go
        elif doorChoose == str(friendlyDoor):
            print()
            print("Дым исчезает и появляется огромный волшебный дракон")

        if friendlyDoor == True:
            print("Здравствуй путник, я загадал число от 1 до 20 попробуй его отгадать \n а то будешь съеден, ням-ням")
        number = random.randint(1, 30)
        guessNumber = 0
        for guessNumber in range(6, 0, -1):  # добавляет обратный отсчет при попытки угадать число

            print("Скажи число")
            guess = input()
            guess = int(guess)
            if guess < number:
                 print(f"Мое число больше, пробуй еще, у тебя осталось {guessNumber - 1} попытки")  # начинает отсчет от 5
            elif guess > number:
                 print(f"Мое число меньше, пробуй еще, у тебя осталось {guessNumber - 1} попытки")
            elif guess == number:
                break

        if guess == number:
             guessNumber = str(guessNumber + 1)
             print(f"Отлично ты угадал!!! с {guessNumber} попытки !!!")
        if guess != number:
             number = str(number)
             print(f"Прости ты не угадал!! я загадал число {number}")




playAgain = 'да'
while playAgain != 'да' or playAgain != 'д' or playAgain != 'нет' or playAgain != 'н':
    #print("Ответь да или нет")
    if playAgain == "да" or playAgain == "д":
        intro()
        doorNumber = doorChoose()
        way(doorNumber)
    elif playAgain == "нет" or playAgain == "н":
        print()
        print("Спасибо за игру, приходи еще у нас тут много опасных пещер")
    else:
        print()
        print("Отвечай да или нет")


    print('Попытайте удачу снова!!! (да или нет)')
    playAgain = input()