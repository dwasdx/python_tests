import unittest
from phonebook_functional import *
from phonebook_functional import __add_person__, __delete_person__, __phone_check__, __change_field__, __is_exists__


class PhonebookTests(unittest.TestCase):
    def test_for_record(self):
        self.assertTrue(__is_exists__('Artem', 'Saratovtsev'))
        self.assertFalse(__is_exists__('Dyadya', 'Volodya'))

    def test_for_creation(self):
        __add_person__('Dmitriy', 'Medvedev', '89340007579', '')
        self.assertTrue(__is_exists__('Dmitriy', 'Medvedev'))

    def test_for_delete(self):
        __delete_person__('Dmitriy', 'Medvedev')
        self.assertFalse(__is_exists__('Dmitriy', 'Medvedev'))

    def test_for_field_change(self):
        __add_person__('Dmitriy', 'Medvedev', '89340007579', '')
        __change_field__('name', 'Anatoliy', 'Dmitriy', 'Medvedev')
        fetched_name = cursor.execute('''SELECT name FROM phonebook
                                        WHERE name = "Anatoliy" and surname = "Medvedev"''').fetchall()[0][0]
        self.assertEqual(fetched_name, 'Anatoliy')
        __delete_person__('Anatoliy', 'Medvedev')
        self.assertFalse(__is_exists__('Anatoliy', 'Medvedev'))

    def test_for_phone_correction(self):
        self.assertEqual('89503451234', __phone_check__('+79503451234'))
        self.assertEqual('89503451234', __phone_check__('89503451234'))


if __name__ == '__main__':
    unittest.main()
