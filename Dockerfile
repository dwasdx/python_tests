FROM python:3.7
WORKDIR phonebook
COPY *.py /phonebook/
CMD [ "python", "phonebook.py" ]