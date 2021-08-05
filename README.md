<h2>Справочник PhoneBook v.1.1</h2>

1. Требования
Для работы сервиса требуется:
    -  Python3 (3.6-3.9)
    -  MySql (MariaDB)
    
2. Установка зависимостей
 pipenv install -r requirements.txt
   
3. База данных

 Field       Type         Null     Key     Default  Extra                                                              
 "id"        int(11)      NONULL   PRIKEY  NULL     AI                                                                 
 "name"      varchar(100) YES              NULL                                                                        
 "nomer"     char(12)     YES      UNI     NULL                                                                        
 "birthday"  date         YES              NULL                                                                        


4. Запуск
- python  main.py

![alt text](screenshots/1-1.jpg "Описание будет тут")
![alt text](screenshots/2.jpg "Описание будет тут")
![alt text](screenshots/4.jpg "Описание будет тут")
![alt text](screenshots/5.jpg "Описание будет тут")
![alt text](screenshots/6.jpg "Описание будет тут")