# Laboratory Work for Data Mining course
## Created by Andrei Zhuravlev 18SE2
*Main idea* 
Data base "Phonebook". There are features like adding new clients, 
deleting and changing data about existing clients. Created on python using SQLite3.
## How to start
All you need for running this peace of ~~crap~~ code is the source file ``phonebook.py`` and database file called ``phonebook.db``. They all are available in this repo. These files must be located in the same directory.
## How to run
1. In your terminal go to the directory with these files 
```
cd <dir_with_files>
```
2. Run source file using this command
```
python3 phonebook.py
```
If everything is done correctly, you should be able to see the menu
## How to run this thing in Docker container
First of all, move into directory with sources you've just downloaded, then enter this command in order to build it
```
docker build -t <image_name> .
```
Once the building is done, run this app in Docker container:
```
docker run -it -v <your path to phonebook.db>:/phonebook/phonebook.db <image_name>
```
You will get the same functional and also changes in ``phonebook.db`` executed in container will also be saved on your local machine
## How to work with this ~~shit~~
After completion of every command you will see menu with list of available commands:
```
Choose one of the commands
add - Add new record to the phonebook
delete - Delete existing record to the phonebook
change - Change some field in existing record
print all - Print all phonebook
print age - Print a certain person's age
search - Search for something in whole phonebook
0 - Exit
```

In order to choose on of them you should type in your terminal the same name of the command as in this menu

Let's walk by every of them:

1. **add** - is a command to add new record. You will be guided through every step. Here is order of adding
```
Enter name and surname or 0 if you want to exit this function
Example - Ivan Ivanov
> Ivan Ivanov
Enter phone number
> 88005553535
Enter birthdate or 0 if you do not want to fill this field
Date should be in format %DD.%MM.%YYYY
> 10.10.2000
Added
```
2. **delete** - is for deleting particular record. To delete one, you need to enter either Name and Surname (unique field), phone number or birth date. In last two cases, if there are more than one record matching the pattern, then you will be provided with hit list and a suggestion to Enter Name and Surname of the particular record. Here is the order:

```
delete
Enter name and surname or phone number or 0 is you want to exit
> Ivan Ivanov
```

Or with matching pattern:

```
Enter name and surname or phone number or 0 is you want to exit
>88005553535
There are several records with this phone
=====================
Ivan Ivanov 88005553535 10.10.2000 
Nikolay Okunkov 88005553535 0 
=====================
Type in name and surname that you want to delete
Enter name and surname or 0 if you want to exit
>Nikolay Okunkov
Deleted
```

3. **change** - command to change existing record
```
Enter name and surname or 0 if you want to exit
> Ilya Bychkov
What field do you want to change?
name, surname, phone, date
> phone
Enter new value for this field
> 88000001235
Changing complete
```

4. **print all** - prints list of all records in database
5. **print age** - prints age of particular person from database
Here is info on record ``Ivan Ivanov``:
```
Ivan 	 Ivanov 	 88005553535 	 10.10.2000
```

```
print age
Enter name and surname or 0 if you want to exit
> Ivan Ivanov
Ivan Ivanov is now 19 years old
```
6. **search** - prints info on all found records. You can search by name, surname, phone number or birth date

To exit from program simply enter ``0`` while in menu