import os
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

# Продолжаем писать код нашей программы...
config = configparser.ConfigParser()

def create_config():
    """
    Create a base config file
    """
    config = configparser.ConfigParser()
    config.add_section("general")
    config.set("general", "title", "Привет тебе инвестор🖖.\nЕсли ты решил вложиться и поиметь что-то с этого, то ты пришел по адресу!😁\nВсе выплаты выкладываются в виде скриншота у нас в канале  @CashBack_Channel🔥🔥\nВыводы от инвестиции поступают на ваш кошелек с которого поступили инвестиции ровно через трое суток после вложения🤑")
    config.add_section("button1")
    config.set("button1", "title", "⬇️ТАРИФЫ⬇️")
    config.set("button1", "message", "Выберите подходящий для вас тариф.👇👇👇")
    config.add_section("button2") 
    config.set("button2", "title", "Start💶")
    config.set("button2", "message", "Информация о тарифе ''Start💶'': \nХорошо подходит для начинающих в этом деле людей.\n🤓Сумма вложения от 50рублей до 249рублей.\nКоличество процентов в день: 10 процентов\nВывод будет произведен через 3 дня после вложения.(Автоматический вывод на номер с которого был пополнен счет 📲 💳 )")
    config.add_section("button3")
    config.set("button3", "title", "V.I.P.💰")
    config.set("button3", "message", "Информация о тарифе ''V.I.P.💰'':\nДанный тариф хорошо подходит для тех кто освоился в этом деле.😎\nСумма вложения от 250рублей до 999рублей. 💵\nКоличество процентов в день: 15процентов. 💸\nВывод будет произведен через 3 дня после вложения.(Автоматический вывод на номер с которого был пополнен счет 📲 💳 )")
    config.add_section("button4")
    config.set("button4", "title", "Premium💎")
    config.set("button4", "message", "Информация о тарифе ''Premium.💎'':\nДанный тариф хорошо подходит для ''взрослых дяденек'' которые хотят заработать на пустом месте. 🤑\nСумма вложения от 1000рублей до 15000рублей. 💵\nКоличество процентов в день: 20 процентов. 💸\nВывод будет произведен через 3 дня после вложения.(Автоматический вывод на номер с которого был пополнен счет 📲 💳 )")
    config.add_section("button5")
    config.set("button5", "title", "Info📋")
    config.set("button5", "message", "Наш канал где выкладываем скрины с выплатами @CashBack_Channel\nНаш чат с инвесторами @CashBack_Chat\nСвязь с нами и Техническая поддержка @S_CashBackRobot- Работает каждый день с 9:00 до 20:00(МСК)\nНе забывайте нажимать /start что бы не пропустить обновления в боте")
    config.add_section("button6")
    config.set("button6", "title", "Пополнение счета💵📲")
    config.set("button6", "message", "Для начала вы должны пополнить баланс на номер📲 +77778229160.\n Далее вам остается только ждать. \nПо окончанию трех дней, на счет💳,  с которого вы пополняли баланс бота, придет ваша сумма с процентами💰 в зависимости от тарифа, который вы выбрали ранее💷.")
    config.add_section("button7")
    config.set("button7", "title", "Статистика Бота📊")
    config.set("button7", "message", "👨‍👩‍👧‍👦Статистика пользователей ...\n 💸Статистика выплат...\n\n P.s. статистика обновляется 1 раз 24 часа. Для обновления статистики нажмите>> /start")

    with open("data.ini", "w", encoding = 'utf-8') as config_file:
        config.write(config_file)

def get_config():
    """
    Returns the config object
    """
    if not os.path.exists("data.ini"):
        create_config()
    config = configparser.ConfigParser()
    config.read("data.ini", encoding='utf-8')
    #with open("data.ini", "r", encoding = 'utf-8') as config_file:
    #    config.read(config_file)
    return config

def get_setting(section, setting):
    """
    Print out a setting
    """
    config = get_config()
    value = config.get(section, setting)
    msg = "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value
    )
    print(msg)
    return value
 
 
def update_setting(section, setting, value):
    """
    Update a setting
    """
    config = get_config()
    config.set(section, setting, value)
    with open("data.ini", "w", encoding = 'utf-8') as config_file:
        config.write(config_file)
