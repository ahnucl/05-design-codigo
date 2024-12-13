from abc import ABC, abstractmethod

# Classe de interface
# Definir a regra de construção das demais classes que a implementam
class NotificationSender(ABC):
    @abstractmethod
    def send_notification(seld, message: str) -> None: pass


class EmailNotificationSender(NotificationSender):
    
    def send_notification(seld, message) -> None:
        print(message)


# Inversão de dependência
class Notificator:
    def __init__(self, notification_sender: NotificationSender):
        self.__notification_sender = notification_sender
    
    def send(self, message) -> None:
        self.__notification_sender.send_notification(message)
        

obj = Notificator(EmailNotificationSender())
obj.send('Ola mundo')