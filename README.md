Справочник PhoneBook v.1.1

1. Требования
Для работы сервиса требуется:
    -  Python3 (3.6-3.9)
    -  MySql (MariaDB)
    
2. Установка зависимостей
 pipenv install -r requirements.txt
   
3. База данных

 Field    Type         Null     Key     Default  Extra

 id       int(11)      NONULL   PRIKEY  NULL     AI
 name     varchar(100) YES      -----   NULL     -----              
 nomer    char(12)     YES      UNI     NULL     -----              
 birthday date         YES      -----   NULL     -----              
   
4. Запуск
- python  main.py
