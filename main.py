from kivy.app import App
from kivy.uix.label import Label

class ContentApp(App):
    def build(self):
        return Label(text='CONTENT Messenger\nСкоро здесь будет чат!')

if __name__ == '__main__':
    ContentApp().run()
