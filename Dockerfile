FROM python:3.7
WORKDIR phonebook
COPY *.py *.txt /phonebook/
RUN pip install -r requirements.txt
CMD [ "python", "phonebook.py" ]