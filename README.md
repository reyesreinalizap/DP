# DP
open cmd:
to run the app go to app directory and type python app.py

to install the database:


1.First, open your command prompt with Administrator.
2.Go to MySQL installed directory and copy path and past on command prompt like:cd C:\Program Files\MySQL\MySQL Server 5.7\bin
3.type mysql -uroot -p
4. mysql> CREATE USER 'db_admin'@'localhost' IDENTIFIED BY 'db_admin';
5.mysql> CREATE DATABASE lifevest;
6.mysql> GRANT ALL PRIVILEGES ON db_admin . * TO 'db_admin'@'localhost';
7.open workbench check if lifevest exist on the list of schemas
8.pip install flask-sqlalchemy
9.pip install flask-mysql
10.pip install flask-mysqldb

to add db to the app.py:
1. go to the directory of app using new cmd then cd to app directory
2. type python
type the following:
3.from app import db
4.db.create_all()
5.exit()

install other needed flask items using pip
run app.py using python app.py
