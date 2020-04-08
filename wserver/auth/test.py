import os
import unittest

from flask import current_app
from flask_testing import TestCase

from wserver.manage import app
from wserver.config import basedir


class TestUserResource(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.DevelopmentConfig')
        return app

    def test_get_all_user(self):
        # self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        # self.assertTrue(app.config['DEBUG'] is True)
        # self.assertFalse(current_app is None)
        # self.assertTrue(
        #     app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
        # )
        pass