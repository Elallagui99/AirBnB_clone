#!/usr/bin/python3
"""
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.updated_at)
        self.assertIsNotNone(my_model.created_at)

    def test_init_with_kwargs(self):
        kwargs = {
            'id': 'some_custom_id',
            'created_at': '2022-01-28T12:34:56.789012',
            'updated_at': '2022-01-28T12:34:56.789012',
            'custom_attribute': 'some_value'
        }

        my_model = BaseModel(**kwargs)

        self.assertEqual(my_model.id, 'some_custom_id')
        self.assertEqual(my_model.created_at.isoformat(),
                         '2022-01-28T12:34:56.789012')
        self.assertEqual(my_model.updated_at.isoformat(),
                         '2022-01-28T12:34:56.789012')
        self.assertEqual(my_model.custom_attribute, 'some_value')

    def test_save(self):
        my_model = BaseModel()
        current_save = my_model.updated_at
        my_model.save()
        self.assertNotEqual(current_save, my_model.updated_at)

    def test_to_dict(self):
        my_model = BaseModel()
        my_dict = my_model.to_dict()
        self.assertIsInstance(my_dict, dict)

        self.assertEqual(my_dict["__class__"], "BaseModel")
        self.assertEqual(my_dict["id"], my_model.id)
        self.assertEqual(my_dict["updated_at"][:19],
                         my_model.updated_at.isoformat()[:19])
        self.assertEqual(my_dict["created_at"][:19],
                         my_model.created_at.isoformat()[:19])

    def test_str(self):
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith("[BaseModel]"))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()
