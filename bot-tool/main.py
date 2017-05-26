import requests
import configparser
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QMessageBox
from interface import Ui_Dialog

version = "v0.1 ALPHA"

#chats = {"Upadmin":  "-174866231", "General": "-1001059668815", "DNC": "-119968344", "GOP": "-1001087584069"}
admin_id = "116450987"  # Sends message to @AxonC

config = configparser.ConfigParser()
config.read("config.ini")

class CommandLineFallback():
    def menu(self):
        print("-" * 20)
        print("Welcome to the USG Bot Application. "
              "To get started, please select a Bot below by entering its corresponding number.")
        print("-" * 20)
        print("1. McQuixon Chat")
        print("2. General Chat (GenPop)")
        print("3. Democratic Party Chat")
        print("4. Republican Party Chat")
        print("P. All Party Chats")
        print("-" * 20)
        print("S. Settings")
        print("X. Exit")
        print("-" * 20)
        bot_selection = input(str("Selected Action:\n"))
        if bot_selection == "1":
            message = self.messagePrompt()
            self.sendMessage(config["CHATS"]["Upadmin"], message)
        elif bot_selection == "2":
            message = self.messagePrompt()
            self.sendMessage(config["CHATS"]["General"], message)
        elif bot_selection == "3":
            message = self.messagePrompt()
            self.sendMessage(config["CHATS"]["DNC"], message)
        elif bot_selection == "DEBUG":
            message = self.messagePrompt()
            self.sendMessage(admin_id, message)
        elif bot_selection == "4":
            message = self.messagePrompt()
            self.sendMessage(config["CHATS"]["GOP"], message)
        elif bot_selection == "P":
            message = self.messagePrompt()
            self.sendToAllParties(config["CHATS"]["DNC"], config["CHATS"]["GOP"], message)
        elif bot_selection == "S":
            auth = input(str("Enter Admin Password:"))
            if auth == "Noxa":
                print("Welcome to the Admin Area!")
            else:
                print("You are not authoried to access this area.\nThe Application will now close.")
                exit()
        elif bot_selection == "X":
            exit()

    def messagePrompt(self):
        print("=" * 20 + "WARNING: Messages may not contain ampersand (&) characters. If you are attaching URLs, please use a URL shortner such as bit.ly " + "=" * 20)
        message = input(str("Enter the message for the Bot to send to your selected chat:\n"))
        return message


    def sendMessage(self, botid, text):
        bot_url = "https://api.telegram.org/bot306638866:AAHyGKFYWF8FCDiAZTz6K6HKJkIh8Xu-Lp0/sendMessage" + "?text=" + text + "&chat_id=" + botid
        bot_submit = requests.get(bot_url)
        print("Message sent!")


    def sendToAllParties(self, botid1, botid2, text):
        boturl1 = "https://api.telegram.org/bot306638866:AAHyGKFYWF8FCDiAZTz6K6HKJkIh8Xu-Lp0/sendMessage" + "?text=" + text + "&chat_id=" + botid1
        boturl2 = "https://api.telegram.org/bot306638866:AAHyGKFYWF8FCDiAZTz6K6HKJkIh8Xu-Lp0/sendMessage" + "?text=" + text + "&chat_id=" + botid2
        requests.get(boturl1)
        requests.get(boturl2)


class MainApp(QDialog, Ui_Dialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.btnDebug.clicked.connect(self.debugMessage)
        self.btnSend.clicked.connect(self.getMessage)

        self.btnClear.clicked.connect(self.clear)

        for x in config["CHATS"]:
            if len(x) <= 3:
                formatted = x.upper()
            else:
                formatted = x.title()
            self.cboChat.addItem(formatted)

    def clear(self):
        self.txtMessage.clear()

    def debugMessage(self):
        message = self.txtMessage.toPlainText()
        self.sendMessageUi(admin_id, message)


    def getMessage(self):
        message = self.txtMessage.toPlainText()
        bot = self.cboChat.currentText()
        bot_number = 0
        if bot in config["CHATS"]:
            bot_number = config["CHATS"][bot.lower()]
        else:
            exit()
        if "&" in message:
            self.formatErrorBox()
        else:
            self.sendMessageUi(bot_number, message)


    def sendMessageUi(self, botid, text):
        bot_url = "https://api.telegram.org/bot306638866:AAHyGKFYWF8FCDiAZTz6K6HKJkIh8Xu-Lp0/sendMessage?text=" + text + "&chat_id=" + botid
        requests.get(bot_url)
        box = QMessageBox()
        box.setText("Message sent successfully!")
        box.setIcon(QMessageBox.Information)
        box.setWindowTitle("Confirmation")
        box.exec_()

    def formatErrorBox(self):
        box = QMessageBox()
        box.setText("Your message cannot contain an ampersand (&) or question mark (?). Please revise your message")
        box.setIcon(QMessageBox.Warning)
        box.setWindowTitle("Format Error")
        box.exec_()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
