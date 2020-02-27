FROM python:3.7
WORKDIR .
COPY . .
RUN pip install pystrich
CMD [ "python", "phonebook.py" ]