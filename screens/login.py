from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty


class LoginScreen(MDScreen):
    username_input = StringProperty('admin')
    password_input = StringProperty('password')

    def do_login(self):
        username = self.ids['username_input'].text
        password = self.ids['password_input'].text

        # Add your login logic here
        # Example: Check username and password against a database or hardcoded values
        if username == 'admin' and password == 'password':
            print("Login successful!")
            self.manager.current = 'home'
        else:
            print(username, password)
            print("Invalid login credentials.")