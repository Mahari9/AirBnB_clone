#!/usr/bin/python3
"""This module defines unittest for the storagefile engine
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Defines Unittests, test cases for instantiation
    of the FileStorage class.
    """

    def test_FileStorage_instantiation_no_args(self):
        # Checks storage creation without argument.
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_wa_arg(self):
        # Checks storage creation with argument.
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        # Checks the storage file path private attribute string.
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objs_is_private_dict(self):
        # checks the storage type for dictionary.
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        # Checks for initialition of file storage.
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Defines Unittests, test cases for the methods
    of the FileStorage class.
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        # Test for all filestorage type for dictionary.
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_w_arg(self):
        # Test for all filestorage type with arg for dictionary.
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        # Tests for creation of new classes.
        parent = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(parent)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        self.assertIn("BaseModel." + parent.id, models.storage.all().keys())
        self.assertIn(parent, models.storage.all().values())
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())

    def test_new_w_args(self):
        # Checks for new with arg.
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        parent = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(parent)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + parent.id, save_text)
            self.assertIn("User." + user.id, save_text)
            self.assertIn("State." + state.id, save_text)
            self.assertIn("Place." + place.id, save_text)
            self.assertIn("City." + city.id, save_text)
            self.assertIn("Amenity." + amenity.id, save_text)
            self.assertIn("Review." + review.id, save_text)

    def test_save_w_arg(self):
        # checks for save with arg.
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        parent = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(parent)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + parent.id, objs)
        self.assertIn("User." + user.id, objs)
        self.assertIn("State." + state.id, objs)
        self.assertIn("Place." + place.id, objs)
        self.assertIn("City." + city.id, objs)
        self.assertIn("Amenity." + amenity.id, objs)
        self.assertIn("Review." + review.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
