"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
small_talking = {
        "Привет":"Ку",
        "Как дела?":"Очень хорошо",
        "Чем занимаешься?":"Отвечаю на вопросы",
        "Можно?":"Нельзя!",
        "Que tal la vida?":"Muy bien!",
        "Hi":"Hello Kitty"
    }

def ask_user():
    """
    Замените pass на ваш код
    """
    print('Я птица говорун! Умею поддерживать разговор на следующие темы: ','\n')
    
    for k in small_talking:
        print(k)
    
    print('\n')
    # user_response = input('Ну скажи что-нибудь: ')
    
    # if small_talking.get(user_response) is None:
    #     print('Краткость сестра таланта!')
    # else:
    #     print(small_talking.get(user_response))
    
    condition = True

    while condition is not None:
      # bool(None) == False , приравнивание - избыточный код, его обычно изьегают
        try:
            user_response = input('Ну скажи что-нибудь: ')
            condition = small_talking.get(user_response)
            bot_response = small_talking.get(user_response) if small_talking.get(user_response) is not None else "Чао какао!"
            # в пердыдущих 2х строчках ты 3 раза вытаскиваешь ответ из словаря
            # есть 2 варианта - вытаскивать 1 раз. писать в переменную и двльше только с ней работать (ты и так записываешь 
            # в кондишн) или двлеть разные действия
            # в рамках обучения предлагаю второй вариант. давай сделаем так:
            # 1. проверяем, есть ли в словаре такой ключ, если нет - пишем "пока" и вываливаемся
            # 2. если ключ есть, отвесаем ответ =)
            print(bot_response)
        except KeyboardInterrupt:
            print('пока :(')
            break
    
if __name__ == "__main__":
    ask_user()
