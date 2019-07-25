from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm


def setUp(self):
    user = User.objects.create(username='test')
    user.set_password('test_password')
    user.save()


class TestAccountsLoginForm(TestCase):

    def test_login_form_valid_data(self):
        user = {'username': 'test', 'password': 'test_password'}
        form = UserLoginForm(data=user)
        self.assertTrue(form.is_valid)


    def test_login_form_invalid_data(self):
        form = UserLoginForm(data={'username':'','password':''})
        self.assertEqual(form.errors, {'username': ['This field is required.'],
                                       'password': ['This field is required.']})


class TestAccountsRegistrationForm(TestCase):
    
    def test_successfull_register(self):
        form = UserRegistrationForm({'username':"test",
                                     "password1": "test_password",
                                     "password2": "test_password",
                                     "email": "test@test.com"})
        self.assertTrue(form.is_valid())


    def test_register_with_already_created_username(self):
        setUp(self)
        form = UserRegistrationForm({'username':"test",
                                     "password1": "test_password",
                                     "password2": "test_password",
                                     "email": "test@test.com"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['A user with that username already exists.'])


    def test_passwords_match(self):
        form = UserRegistrationForm({'username': 'test',
                                     'password1': 'test_password1',
                                     'password2': 'test_password2'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'password2': ['Passwords must match!']})


    def test_required_fields(self):
        form = UserRegistrationForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'username': ['This field is required.'],
                                       'password1': ['This field is required.'],
                                       'password2': ['This field is required.']})
