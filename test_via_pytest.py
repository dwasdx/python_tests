import pytest
from phonebook_functional import *
from phonebook_functional import __add_person__, __delete_person__, __phone_check__, __change_field__, __is_exists__

class TestClass:
    def test_for_record(self):
        assert __is_exists__('Artem', 'Saratovtsev') is True
        assert __is_exists__('Dyadya', 'Volodya') is False

    def test_for_creation(self):
        __add_person__('Dmitriy', 'Medvedev', '89340007579', '')
        assert __is_exists__('Dmitriy', 'Medvedev') is True

    def test_for_delete(self):
        __delete_person__('Dmitriy', 'Medvedev')
        assert __is_exists__('Dmitriy', 'Medvedev') is False

    def test_for_field_change(self):
        __add_person__('Dmitriy', 'Medvedev', '89340007579', '')
        __change_field__('name', 'Anatoliy', 'Dmitriy', 'Medvedev')
        fetched_name = cursor.execute('''SELECT name FROM phonebook
                                                WHERE name = "Anatoliy" and surname = "Medvedev"''').fetchall()[0][0]
        assert fetched_name == 'Anatoliy'
        __delete_person__('Anatoliy', 'Medvedev')
        assert __is_exists__('Anatoliy', 'Medvedev') is False

    def test_for_phone_correction(self):
        assert __phone_check__('+79503451234') == '89503451234'
        assert __phone_check__('89503451234') == '89503451234'

    def test_for_new_commit(self):
        assert 1 is 1
