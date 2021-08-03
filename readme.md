# Vulnerable Flask Application
A Vulnerable Flask Application for beginning pen-testers. 
Contains a few minor vulnerabilities, could be fun for beginners.

Suggestions to improvements is welcome.

Originally designed as a Final Year Project for my BSc.


## Installation
Should work on both Windows and Linux (Ubuntu 18.04), with some minor tweaking to fit your system
* pip install -r requirements.txt
* Create database
* IMPORTANT: Put it in project folder. Ex: flask_auth_app/project/db.sqlite
```sql
CREATE TABLE user (
	id	INTEGER,
	email	VARCHAR(50),
	password	VARCHAR(50),
	name	VARCHAR(50),
	PRIMARY KEY(id AUTOINCREMENT)
);
```

```sql
CREATE TABLE products (
	id INT,
	item_name VARCHAR(50),
	qty INT,
	price VARCHAR(50)
);
```
* Code is written for SQLite 3, your mileage may vary using other databases
* Create a virtualenv and use it
* export FLASK_APP={Path/to/your/project}
* flask run

## LICENSE

[MIT](https://github.com/JFalnes/vulnerable_flask_application/blob/master/LICENSE)
