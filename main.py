
import sys
from datetime import datetime, date

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate

from PyQt5.QtWidgets import QDialog, QApplication,  QMessageBox

from Model.handler import DataBase
from Ui.tableview import Ui_TableDialog
from Ui.tableview2user import Ui_TableDialog2

from Ui.welcomescreen import Ui_Dialog
from Ui.signup import Ui_SignUpDialog
from Ui.recoveryPassword import Ui_RecoveryPasswordDialog
from Ui.renewPassword import Ui_RenewPasswordDialog
from Ui.birthday import Ui_BirthDayTableDialog
from Ui.alluser import Ui_AllUserTableDialog
from Ui.helpscreen import Ui_HelpScreenDialog

saveuser = ""
savepassword = ""



class MessageBox(QMessageBox):
    def __init__(self):
        QMessageBox.__init__(self)
        self.setText("This is a MessageBox, typically used to convey short messages to the user.")
        self.setInformativeText("Informative text provides more space to explain the message ")
        self.setIcon(QMessageBox.Information)
        self.setStandardButtons(QMessageBox.Close)

class BaseForm(QDialog):
    """
    Основные методы работы с табличной формой TableWidget
    """
    def __init__(self):
        self.db = DataBase()
        super().__init__()
        self.ui = Ui_TableDialog()
        self.ui.setupUi(self)
        self.message = QMessageBox()


    def editLineClear(self):
        """
        Обнуляет поля LineEdit (4 шт)
        :return:
        """
        for line in self.list_line_edit:
            line.clear()

    def SearchRows_Letter(self, a, b):
        """
        Слот - Передает sql в метод выборки SearchRows
        :return:
        """
        sql = self.sqlBase(a, b)
        self.SearchRows(sql)


    def SearchRows_All(self):
        """
        Слот-метод , загружает все записи из Таблицы
        :return:
        """
        sql = f"SELECT id, name, nomer, birthday from phonebook ORDER By name"
        self.SearchRows(sql)

    def sqlBase(self, a, b):
        """
        Подготавливает SQL запрос
        :param a: начальная точка поиска
        :param b: конечная точка поиска
        :return: sql
        """
        sql = f"SELECT id, name, nomer, birthday FROM phonebook WHERE name >=" \
              f" '{a}' AND name <= '{b}'  ORDER BY name ASC"
        return sql

    def SearchRows(self, sqlStatement=f"SELECT id, name, nomer, birthday from phonebook ORDER By birthday"):
        """
        Поиск записей по SQL запросу.
        По умолчанию загружает все записи из Таблицы
        :param sqlStatement:
        :return:
        """
        self.db.search(sqlStatement)
        rows = self.db.cur.fetchall()
        row = 0
        self.ui.tableWidget.setRowCount(len(rows))
        for person in rows:
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(person[0])))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person[1]))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(person[2]))
            self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(person[3])))
            row += 1

    def gotoWelcome(self):
        """
        Переход на главный экран приложения
        :return:
        """
        global saveuser, savepassword
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        # сохраняем пользователя и пароль в текущей сессии
        welcome.ui.nameuserLineEdit.setText(saveuser)
        welcome.ui.passwordLineEdit.setText(savepassword)


    def gotoHelp(self):
        help = HelpScreen()
        widget.addWidget(help)
        widget.setCurrentIndex(widget.currentIndex()+1)

class FormUser(BaseForm):
    """
    TableWidget для юзера, кнопки, таблица
    """
    def __init__(self):
        super().__init__()

        # Кнопки сортировки
        self.ui.ABsearchPushButton_1.clicked.connect(lambda: self.SearchRows_Letter("А", "В"))
        self.ui.VGsearchPushButton_2.clicked.connect(lambda: self.SearchRows_Letter("В", "Д"))
        self.ui.DEsearchPushButton_3.clicked.connect(lambda: self.SearchRows_Letter("Д", "Ж"))
        self.ui.GZIIsearchPushButton_4.clicked.connect(lambda: self.SearchRows_Letter("Ж", "К"))
        self.ui.KLsearchPushButton_5.clicked.connect(lambda: self.SearchRows_Letter("К", "М"))
        self.ui.MNsearchPushButton_6.clicked.connect(lambda: self.SearchRows_Letter("М", "О"))
        self.ui.OPsearchPushButton_7.clicked.connect(lambda: self.SearchRows_Letter("О", "Р"))
        self.ui.RSsearchPushButton_8.clicked.connect(lambda: self.SearchRows_Letter("Р", "Т"))
        self.ui.TYsearchPushButton_9.clicked.connect(lambda: self.SearchRows_Letter("Т", "Ф"))
        self.ui.FHsearchPushButton_10.clicked.connect(lambda: self.SearchRows_Letter("Ф", "Ц"))
        self.ui.ZHSSsearchPushButton_11.clicked.connect(lambda: self.SearchRows_Letter("Ц", "Ъ"))
        self.ui.IEsearchPushButton_12.clicked.connect(lambda: self.SearchRows_Letter("Ъ", "Ю"))
        self.ui.YouYjasearchPushButton_13.clicked.connect(lambda: self.SearchRows_Letter("Ю", "Яя"))
        self.ui.AZsearchPushButton_14.clicked.connect(lambda: self.SearchRows_Letter("A", "Zz"))

        self.ui.helpPushButton.clicked.connect(self.gotoHelp)

        # кнопка загрузки всех данных в главную страницу таблицы
        self.ui.ALLsearchPushButton_16.clicked.connect(self.SearchRows_All)

        self.ui.labelUser.setText(saveuser)

        self.ui.cancelPushButton.clicked.connect(self.gotoWelcome)

        # Ширина колонок таблицы
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setColumnWidth(2, 200)
        self.ui.tableWidget.setColumnWidth(3, 300)
        self.ui.tableWidget.setSortingEnabled(True)

        self.SearchRows()

class AllUserForm(QDialog):
    """
    TableWidget для просмотра всех пользователей
    """
    def __init__(self):
        self.db = DataBase()
        super().__init__()
        self.ui = Ui_AllUserTableDialog()
        self.ui.setupUi(self)
        self.ui.HeadLabel.text()
        self.ui.userTableWidget.setSortingEnabled(True)
        self.ui.cancelPushButton.clicked.connect(self.gotoFormAdmin)
        self.ui.emailLabel.text()
        self.ui.emailLineEdit.text()
        self.ui.delPushButton.clicked.connect(self.deleteUserFunction)
        self.ui.userTableWidget.cellClicked.connect(self.cellClick)

        # Ширина колонок таблицы
        self.ui.userTableWidget.setColumnWidth(0, 200)
        self.ui.userTableWidget.setColumnWidth(1, 170)
        self.ui.userTableWidget.setColumnWidth(2, 100)
        self.ui.userTableWidget.setColumnWidth(3, 200)

        self.ui.labelUser.setText(saveuser)

        self.loadUser()

    def editLineClear(self):
        """
        Обнуляет поля LineEdit (4 шт)
        :return:
        """
        self.ui.emailLineEdit.clear()

    def deleteUserFunction(self):
        """
        Удалить пользователя из БД
        :return:
        """
        email = self.ui.emailLineEdit.text()
        query = f"SELECT * FROM users WHERE email='{email}'"
        query_delete = f"DELETE from users WHERE email='{email}'"
        self.db.read(query)
        row = self.db.cur.fetchone()
        if row != None:
            self.db.delete(query_delete)
            self.editLineClear()
            self.loadUser()

    def cellClick(self, row, col):
        """
        обработка щелчка мыши по таблице
        :param row: номер строки
        :param col: номер столбца
        :return:
        """
        self.ui.emailLineEdit.setText(self.ui.userTableWidget.item(row, 0).text().strip())

    def gotoFormAdmin(self):
        admin = FormAdmin()
        widget.addWidget(admin)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def loadUser(self):
        """
        Поиск записей по SQL запросу.
        По умолчанию загружает все записи из Таблицы
        :param sqlStatement:
        :return:
        """
        sqlStatement = f"SELECT email, password, save, birthday from users ORDER By email"
        self.db.read(sqlStatement)
        rows = self.db.cur.fetchall()
        row = 0
        self.ui.userTableWidget.setRowCount(len(rows))
        for person in rows:
            print(person)
            self.ui.userTableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(person[0])))
            self.ui.userTableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(person[1])))
            self.ui.userTableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(person[2])))
            self.ui.userTableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(person[3])))
            row += 1

class FormAdmin(FormUser):
    """
    TableWidget для administrator  наследуемый,
     расширенный кнопками, полями ввода.
     Добавлены и переопределены методы
    """
    def __init__(self):
        self.db = DataBase()
        super().__init__()
        self.ui = Ui_TableDialog2()
        self.ui.setupUi(self)

        # Кнопки сортировки
        self.ui.ABsearchPushButton_1.clicked.connect(lambda: self.SearchRows_Letter("А", "В"))
        self.ui.VGsearchPushButton_2.clicked.connect(lambda: self.SearchRows_Letter("В", "Д"))
        self.ui.DEsearchPushButton_3.clicked.connect(lambda: self.SearchRows_Letter("Д", "Ж"))
        self.ui.GZIIsearchPushButton_4.clicked.connect(lambda: self.SearchRows_Letter("Ж", "К"))
        self.ui.KLsearchPushButton_5.clicked.connect(lambda: self.SearchRows_Letter("К", "М"))
        self.ui.MNsearchPushButton_6.clicked.connect(lambda: self.SearchRows_Letter("М", "О"))
        self.ui.OPsearchPushButton_7.clicked.connect(lambda: self.SearchRows_Letter("О", "Р"))
        self.ui.RSsearchPushButton_8.clicked.connect(lambda: self.SearchRows_Letter("Р", "Т"))
        self.ui.TYsearchPushButton_9.clicked.connect(lambda: self.SearchRows_Letter("Т", "Ф"))
        self.ui.FHsearchPushButton_10.clicked.connect(lambda: self.SearchRows_Letter("Ф", "Ц"))
        self.ui.ZHSSsearchPushButton_11.clicked.connect(lambda: self.SearchRows_Letter("Ц", "Ъ"))
        self.ui.IEsearchPushButton_12.clicked.connect(lambda: self.SearchRows_Letter("Ъ", "Ю"))
        self.ui.YouYjasearchPushButton_13.clicked.connect(lambda: self.SearchRows_Letter("Ю", "Яя"))
        self.ui.AZsearchPushButton_14.clicked.connect(lambda: self.SearchRows_Letter("A", "Zz"))

        # кнопка загрузки всех данных в главную страницу таблицы
        self.ui.ALLsearchPushButton_16.clicked.connect(self.SearchRows_All)

        self.ui.userPushButton.clicked.connect(self.gotoAllUserForm)
        self.ui.birthDayPushButtn.clicked.connect(self.gotoBirthDayOnWeek)

        self.ui.addPushButton.clicked.connect(self.insertNewRecord)
        self.ui.updatePushButton.clicked.connect(self.updateRecord)
        self.ui.deletePushButton.clicked.connect(self.deleteRecord)

        self.list_line_edit = [self.ui.idLineEdit_1,
                               self.ui.nameLineEdit,
                               self.ui.nomerLineEdit,
                               self.ui.dayLineEdit,
                               ]
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setColumnWidth(2, 200)
        self.ui.tableWidget.setColumnWidth(3, 300)
        self.ui.tableWidget.setSortingEnabled(True)

        self.SearchRows()
        self.ui.tableWidget.cellClicked.connect(self.cellClick)  # установить обработчик щелча мыши в таблице

    def gotoAllUserForm(self):
        adminform = AllUserForm()
        widget.addWidget(adminform)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoBirthDayOnWeek(self):
        birthday = BirthDayOnWeek()
        widget.addWidget(birthday)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def SearchRows_All(self):
        """
        (Переопределенный метод)
        Слот-метод, очищает поля и выводит все записи
        :return:
        """
        sql = f"SELECT id, name, nomer, birthday from phonebook ORDER By name"
        self.SearchRows(sql)
        self.editLineClear()  # обнуляет 4 поля LineEdit

    def sqlBase(self, a, b):
        """
        (Переопределеннный метод)
        Подготавливает SQL запрос
        :param a: начальная точка поиска
        :param b: конечная точка поиска
        :return: sql
        """
        sql = f"SELECT id, name, nomer, birthday FROM phonebook WHERE name >=" \
              f" '{a}' AND name <= '{b}'  ORDER BY name ASC"
        self.editLineClear()  # обнуляет 4 поля LineEdit
        return sql

    def cellClick(self, row, col):
        """
        обработка щелчка мыши по таблице
        :param row: номер строки
        :param col: номер столбца
        :return:
        """
        self.ui.idLineEdit_1.setText(self.ui.tableWidget.item(row, 0).text().strip())
        self.ui.nameLineEdit.setText(self.ui.tableWidget.item(row, 1).text().strip())
        self.ui.nomerLineEdit.setText(self.ui.tableWidget.item(row, 2).text().strip())
        self.ui.dayLineEdit.setText(self.ui.tableWidget.item(row, 3).text().strip())

    def insertNewRecord(self):
        """
        Вставка новой записи в Таблицу
        :return:
        """
        name = self.ui.nameLineEdit.text().capitalize()
        nomer = self.ui.nomerLineEdit.text()
        birthday = self.ui.dayLineEdit.text()
        query = f"INSERT INTO phonebook (name, nomer, birthday) VALUES ('{name}', '{nomer}', '{birthday}')"
        self.db.insert(query)
        self.editLineClear()
        self.SearchRows_All()

    def updateRecord(self):
        """
        Изменение записи в Таблице
        :return:
        """
        id = self.ui.idLineEdit_1.text()
        name = self.ui.nameLineEdit.text()
        nomer = self.ui.nomerLineEdit.text()
        birthday = self.ui.dayLineEdit.text()
        query = f"SELECT * FROM phonebook WHERE id='{id}'"
        query_update = f"UPDATE phonebook SET name='{name}', nomer='{nomer}', birthday='{birthday}' " \
                       f"WHERE id='{id}'"
        self.db.read(query)
        row = self.db.cur.fetchone()
        if row != None:
            self.db.update(query_update)
            self.editLineClear()
            self.SearchRows_All()

    def deleteRecord(self):
        """
        Удалить запись из БД
        :return:
        """
        id = self.ui.idLineEdit_1.text()
        query = f"SELECT * FROM phonebook WHERE id='{id}'"
        query_delete = f"DELETE from phonebook WHERE id='{id}'"
        self.db.read(query)
        row = self.db.cur.fetchone()
        if row != None:
            self.db.delete(query_delete)
            self.editLineClear()
            self.SearchRows_All()

class WelcomeScreen(QDialog):
    """
    Для авторизации пользователей
    """
    def __init__(self):
        self.db = DataBase()
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.message = QMessageBox()
        self.message.setStyleSheet("background-color: yellow;")
        self.message.setText("Ошибка авторизации!")
        self.startSave()

        self.ui.cancelPushButton.clicked.connect(self.gotoExit)
        self.ui.signupPushButton.clicked.connect(self.gotoCreate)
        self.ui.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.loginPushButton.clicked.connect(self.loginFunction)

        self.ui.echoPasswordCheckBox.stateChanged.connect(self.dispAmount)
        self.ui.saveMeCheckBox.clicked.connect(self.saveMe)

        self.ui.forgotPasswordPushButton.clicked.connect(self.gotoRecoveryPassword)
        self.ui.changePasswordPushButton.clicked.connect(self.gotoChangePassword)

        self.ui.helpPushButton.clicked.connect(self.gotoHelp)

    def gotoHelp(self):
        help = HelpScreen()
        widget.addWidget(help)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def startSave(self):
        """
        Старт с запомненным пользователем
        :return:
        """
        global saveuser, savepassword
        query = f"SELECT email, password, save FROM users WHERE save='1'"
        self.db.read(query)
        row = self.db.cur.fetchone()
        if row != None:
             self.ui.nameuserLineEdit.setText(row[0])
             self.ui.passwordLineEdit.setText(row[1])

    def saveMe(self):
        """
        Проверка нажата ли галка запомнить пользователя
        :return:
        """
        if self.ui.saveMeCheckBox.isChecked() == True:
            return False

    def saveUser(self, saveuser):
        """
        Запомнить пользователя в БД
        :param saveuser:
        :return:
        """
        if self.saveMe() == False:
            email = saveuser
            save = "1"
            query = f"SELECT * from users where email='{email}'"
            self.db.read(query)
            row = self.db.cur.fetchone()
            if row != None:
                query_update = f"UPDATE users SET save='{save}' WHERE email='{email}'"
                self.db.update(query_update)

    def dispAmount(self):
        """
        Показать / спрятать пароль (password)
        """
        self.ui.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        if self.ui.echoPasswordCheckBox.isChecked() == True:
            self.ui.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)


    def loginFunction(self):
        """
        Авторизация пользователя
        :return:
        """
        global saveuser, savepassword
        user = self.ui.nameuserLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        query = f"SELECT password FROM users WHERE email='{user}'"
        if len(user) == 0 or len(password) == 0:
            self.message.setInformativeText("Заполните все поля правильно!")
            self.message.show()
        else:
            self.db.read(query)
            row = self.db.cur.fetchone()
            if row == None:
                self.message.setInformativeText("Такого пользователя нет!")
                self.message.show()
            elif row != [] and row[0] == password:
                if user == 'admin':
                     saveuser = user
                     savepassword = password
                     self.saveUser(saveuser)
                     mytable = FormAdmin()
                     widget.addWidget(mytable)
                     widget.setCurrentIndex(widget.currentIndex() + 1)

                else:
                     saveuser = user
                     savepassword = password
                     self.saveUser(saveuser)
                     mytable = FormUser()
                     widget.addWidget(mytable)
                     widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
                self.message.setInformativeText("Ошибка имени или пароля!")
                self.message.show()

    def gotoBirthDayOnWeek(self):
        birthday = BirthDayOnWeek()
        widget.addWidget(birthday)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoRecoveryPassword(self):
        recovery = RecoveryPassword()
        widget.addWidget(recovery)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoChangePassword(self):
        change = ChangePassword()
        widget.addWidget(change)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoCreate(self):
        #self.conn.close()
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoExit(self):
        sys.exit(app.exec_())

class ChangePassword(QDialog):
    """
    Для изменения пароля
    """
    def __init__(self):
        self.db = DataBase()
        super().__init__()
        self.ui = Ui_RenewPasswordDialog()
        self.ui.setupUi(self)
        self.ui.recoveryPasswordPushButton.clicked.connect(self.renewPasswordFunction)
        self.ui.cancelPushButton.clicked.connect(self.gotoCansel)
        self.message = QMessageBox()
        self.message.setStyleSheet("background-color: red;")
        self.message.setText("Ошибка регистрации!")

    def gotoCansel(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoWelcome(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def renewPasswordFunction(self):
        """
        Смена старого пароля на новый
        :return:
        """
        email = self.ui.emailField.text()
        old_password = self.ui.oldPasswordField.text()
        new_password = self.ui.newPasswordField.text()
        renew_password = self.ui.renewPasswordField.text()
        selectStament  = f" SELECT email, password FROM users WHERE email='{email}' and" \
                         f" password='{old_password}'"
        updateStament = f" UPDATE users set password='{new_password}' " \
                        f" WHERE email='{email}'"
        self.db.read(selectStament)
        row = self.db.cur.fetchone()
        if row == None:
            self.message.setInformativeText("Некорректный email или password!")
            self.message.show()
        elif new_password == renew_password:
            self.db.update(updateStament)
            self.message.setStyleSheet("background-color: green;")
            self.message.setText("Пароль изменен!")
            self.message.setInformativeText(f"Вы успешно изменили пароль")
            self.message.show()
            self.gotoWelcome()
        else:
            self.message.setStyleSheet("background-color: red;")
            self.message.setText("Пароли не сопадают!")
            self.message.setInformativeText(f"Попрообуйте заново")
            self.message.show()

class RecoveryPassword(QDialog):
    """
    Для восстановления пароля, через @email
    """
    def __init__(self):
        self.db = DataBase()
        super().__init__()
        self.ui = Ui_RecoveryPasswordDialog()
        self.ui.setupUi(self)
        self.ui.recoveryPasswordPushButton.clicked.connect(self.recoverysignupFunction)
        self.ui.cancelPushButton.clicked.connect(self.gotoCansel)

        self.message = QMessageBox()
        self.message.setStyleSheet("background-color: red;")
        self.message.setText("Ошибка регистрации!")

    def send_mail(self, mail_addr, parol):
        """
        почтовый клиент
        :param parol:
        :return:
        """
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        login = self.ui.smtpClientField_2.text()
        password = self.ui.smtpPasswordField_3.text()
        url = self.ui.smtpURLField_4.text()
        toaddr = mail_addr

        msg = MIMEMultipart()
        msg['Subject'] = "Ваш забытый пароль от PhoneBook"
        msg['From'] = login
        body = f"Ваш забытый пароль от PhoneBook: {parol}"
        msg.attach(MIMEText(body, 'plain'))
        try:
            server = smtplib.SMTP_SSL(url, 465)
            server.login(login, password)
            server.sendmail(login, toaddr, msg.as_string())
            server.quit()
        except TimeoutError:
            self.message.setStyleSheet("background-color: red;")
            self.message.setText("Нет связи с сервером!")
            self.message.show()
        except smtplib.SMTPAuthenticationError:
            self.message.setStyleSheet("background-color: red;")
            self.message.setText("Отредактируйте адрес SMT- сервера, укажите пароль!")
            self.message.show()

    def gotoCansel(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoWelcome(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def recoverysignupFunction(self):
        """
        Восстановление пароля через отправку на почту пароля
        :return:
        """
        user = self.ui.adresEmailField.text()
        query = f"SELECT * FROM users WHERE email='{user}'"
        self.db.read(query)
        row = self.db.cur.fetchone()
        print(row)
        if row == None:
            self.message.setInformativeText("Такого пользователя нет!")
            self.message.show()
        elif row != []:
            parol = row[2]
            mail_addr = row[1]
            self.send_mail(mail_addr, parol)
            self.gotoWelcome()
        else:
            self.message.setInformativeText("Ошибка имени или пароля!")
            self.message.show()

class CreateAccScreen(QDialog):
    """
    Для регистрации новых пользователей
    """
    def __init__(self):
        self.db = DataBase()
        super().__init__()
        self.ui = Ui_SignUpDialog()
        self.ui.setupUi(self)
        self.ui.signupLabel.text()
        self.ui.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.confirmField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.signUpPushButton.clicked.connect(self.signupFunction)
        self.ui.cancelPushButton.clicked.connect(self.gotoCansel)

        self.message = QMessageBox()
        self.message.setStyleSheet("background-color: red;")
        self.message.setText("Ошибка регистрации!")

    def gotoWelcome(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoCansel(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def check(self, name):
        """
        Проверка на дубликат пользователя
        :param name:
        :return:
        """
        print("name", name)
        query = f"SELECT email FROM users WHERE email='{name}'"
        self.db.read(query)
        row = self.db.cur.fetchone()
        if row != None:
            return True
        else:
            return False

    def signupFunction(self):
        """
        Регистрация нового аккаунта
        :return:
        """
        user = self.ui.nameuserField.text()
        birthday = self.ui.birthdayDateEdit.text()
        print(birthday)
        password = self.ui.passwordField.text()
        confirmpassword = self.ui.confirmField.text()
        query1 = f"INSERT INTO users (email, birthday, password) VALUES ('{user}','{birthday}', '{password}')"
        if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            self.message.setInformativeText("Заполните все поля!")
            self.message.show()

        elif password != confirmpassword:
            self.message.setInformativeText("Пароли не совпадают!")
            self.message.show()

        elif self.check(user) == False:
            self.db.insert(query1)
            self.message.setStyleSheet("background-color: green;")
            self.message.setText("Успешная регистрация!")
            self.message.setInformativeText(f"Вы успешно зарегистрированы с ником - {user}")
            self.message.show()
            self.gotoWelcome()
        else:
            self.message.setStyleSheet("background-color: green;")
            self.message.setText("Такой пользователь уже есть!")
            self.message.setInformativeText(f"Придумайте другой email - {user}")
            self.message.show()


class HelpScreen(QDialog):
    """
    Справочник пользователя
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_HelpScreenDialog()
        self.ui.setupUi(self)

        self.ui.helpCancelPushButton.clicked.connect(self.gotoWelcome)

    def gotoWelcome(self):
        """
        Переход на главный экран приложения
        :return:
        """
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class BirthDayOnWeek(QDialog):
    """
    TableWidget для вывода дней рождения от
    текущей даты и вперед на неделю
    """
    def __init__(self):
        self.db = DataBase()
        super().__init__()
        self.ui = Ui_BirthDayTableDialog()
        self.ui.setupUi(self)

        self.ui.headLabe.text()

        # Ширина колонок таблицы
        self.ui.tableWidget.setColumnWidth(0, 200)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setColumnWidth(2, 300)
        self.ui.tableWidget.setSortingEnabled(True)

        self.ui.labelUser.setText(saveuser)
        self.load_data_birthday()
        self.ui.tableWidget.setSortingEnabled(True)
        self.ui.cancelPushButton.clicked.connect(self.gotoFormAdmin)


    def gotoFormAdmin(self):
        admin = FormAdmin()
        widget.addWidget(admin)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def load_data_birthday(self):
        """
        Выборка дней рождения на неделю вперед
        :return:
        """
        sqlStatement = f"SELECT name, nomer, birthday from phonebook " \
                       f"WHERE DAYOFYEAR(birthday)" \
                       f" BETWEEN DAYOFYEAR(NOW()) AND DAYOFYEAR(DATE_ADD(NOW(), INTERVAL 1 WEEK))" \
                       f" ORDER BY DAYOFYEAR(birthday)"
        self.db.read(sqlStatement)
        rows = self.db.cur.fetchall()
        row = 0
        self.ui.tableWidget.setRowCount(len(rows))
        for person in rows:
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person[0]))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person[1]))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(person[2])))
            row += 1

if __name__=='__main__':
    app = QApplication(sys.argv)
    if DataBase():
        welcome = WelcomeScreen()
        widget = QtWidgets.QStackedWidget()
        widget.addWidget(welcome)
        widget.setFixedHeight(800)
        widget.setFixedWidth(1200)
        widget.show()
    else:
        print("Нет соединения с базой данных")
        sys.exit(1)

    try:
        sys.exit(app.exec_())
    except:
        print("Выход")
