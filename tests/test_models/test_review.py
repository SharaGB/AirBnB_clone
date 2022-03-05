#!/usr/bin/python3
"""
Unittest for review([..])
"""
import pep8
import unittest
from models.review import Review
from models.base_model import BaseModel

review = Review()


class TestReview(unittest.TestCase):
    """ Write unittests for the class Review. """

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_attr_review(self):
        """ Test that checks the Review class. """
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertEqual(review.place_id, '')
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertEqual(review.user_id, '')
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.text, '')
        review.place_id = '666hola666'
        review.user_id = '3da_sa6'
        review.text = 'Hello World!'
        self.assertEqual(review.place_id, '666hola666')
        self.assertEqual(review.user_id, '3da_sa6')
        self.assertEqual(review.text, 'Hello World!')

    def test_review(self):
        """ Test that checks the Review class. """
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))


if __name__ == '__main__':
    unittest.main()
