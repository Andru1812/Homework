def send_email(massage, recipient, sender = 'university.help@gmail.com'):
    if (recipient.count('@') != 1 and sender.count('@') != 1) and (recipient[-4:-1] != '.com' or recipient[-4:-1] != '.net' or recipient[-3:-1] != '.ru') and (sender[-4:-1] != '.com' or sender[-4:-1] != '.net' or sender[-3:-1] != '.ru'):
        print("Невозможно отправить письмо(", massage, ")с адреса", sender, "на адрес", recipient)
    if recipient == sender:
        print("Нельзя отправить письмо(", massage, ")самому себе!")
    elif sender == 'university.help@gmail.com':
        print("Письмо(", massage, ")успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо(", massage, ")отправлено с адреса", sender, "на адрес", recipient)

recipient = input('Введите получателя')
sender = input('Введите отправителя или введите 0 для отправителя по умочанию')
massage = input('Введите сообщение')

if sender == '0':
    sender = 'university.help@gmail.com'

send_email(massage, recipient, sender)