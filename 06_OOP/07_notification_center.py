from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, receiver, message):
        self.receiver = receiver
        self.message = message

    @abstractmethod
    def send(self):
        ...


class EmailNotification(Notification):
    def __init__(self, receiver, message, subject):
        super().__init__(receiver, message)
        self.subject = subject

    def send(self):
        return f"Sending EMAIL to {self.receiver}: {self.subject} – {self.message}"


class SMSNotification(Notification):
    def __init__(self, receiver, message):
        super().__init__(receiver, message[:160])

    def send(self):
        return f"Sending SMS to {self.receiver}: {self.message}"


class PushNotification(Notification):
    def __init__(self, receiver, message):
        super().__init__(receiver, message.upper())

    def send(self):
        return f"Sending PUSH to {self.receiver}: {self.message}"


def dispatch(notifications):
    return [n.send() for n in notifications]