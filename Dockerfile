FROM python:3
ADD phonebook.py /
ADD phonebook.db /
RUN pip install pystrich
CMD [ "python", "./phonebook.py" ]