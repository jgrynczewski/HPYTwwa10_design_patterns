# Abstracja - ukrywamy szczegóły implementacji

class MailService:
    def send_email(self):
        self.__connect()
        self.__authenticate()
        # send mail
        self.__disconnect()

    def __connect(self):
        print("Connected")

    def __authenticate(self):
        print("Authenticated")

    def __disconnect(self):
        print("Disconnected")


m = MailService()
m.send_email()
