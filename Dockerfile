<<<<<<< HEAD
FROM python:3.7
WORKDIR phonebook
COPY *.py *.txt /phonebook/
RUN pip install -r requirements.txt
CMD [ "python3", "phonebook.py" ]
=======
FROM python:3
ADD phonebook.py /
ADD phonebook.db /
RUN pip install pystrich
CMD [ "python", "./phonebook.py" ]
>>>>>>> master
