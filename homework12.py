def send_email(massage, recipient, sender = 'university.help@gmail.com'):
    x1 = recipient.count('@') != 1 or sender.count('@') != 1
    x2 = not (recipient.endswith('.com') or recipient.endswith('.net') or recipient.endswith('.ru'))
    x3 = not (sender.endswith('.com') or sender.endswith('.net') or sender.endswith('.ru'))
    if x1 or x2 or x3:
        print("Невозможно отправить письмо(", massage, ")с адреса", sender, "на адрес", recipient)
    elif recipient == sender:
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