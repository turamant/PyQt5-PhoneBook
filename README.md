<h2>Handbook PhoneBook v.1.1</h2>

<h3>Requirements</h3>
    -  Python3 (3.6-3.9)
    -  MySql (MariaDB)
    
<h3>Installation</h3>
 python -m pip --upgrade pip
 python -m pip install pipenv  
 pipenv install -r requirements.txt
   
<h3>Data base MariDB</h3>

 Field       Type         Null     Key     Default  Extra                                                              
 "id"        int(11)      NONULL   PRIKEY  NULL     AI                                                                 
 "name"      varchar(100) YES              NULL                                                                        
 "nomer"     char(12)     YES      UNI     NULL                                                                        
 "birthday"  date         YES              NULL                                                                        


<h3>How to use</h3>
- python  main.py

<h3>Tested on</h3>
    Manjaro
    Debian
    Fedora


![alt text](screenshots/1-1.jpg "Описание будет тут")
![alt text](screenshots/2.jpg "Описание будет тут")
![alt text](screenshots/4.jpg "Описание будет тут")
![alt text](screenshots/5.jpg "Описание будет тут")
![alt text](screenshots/6.jpg "Описание будет тут")