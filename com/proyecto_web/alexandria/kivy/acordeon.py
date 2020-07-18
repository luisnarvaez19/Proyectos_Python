# How to use Accordion in kivy using .kv file

# Program to Show how to create a switch
# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# The Accordion widget is a form of menu
# where the options are stacked either vertically
# or horizontally and the item in focus
# (when touched) opens up to display its content.
from kivy.uix.accordion import Accordion, AccordionItem

# Label is the text which we want
# to add on our window, give to
# the buttons and so on
from kivy.uix.label import Label


# Create the App class
class AccordionApp(App):

    def build(self):
        root = Accordion()
        root = Accordion(min_space=60)
        # Providing the orentation
        root = Accordion(orientation='vertical')

        # Adding text to each Accordion
        for x in range(5):
            item = AccordionItem(title='Title % d' % x)
            item.add_widget(Label(text='GFG is Good Website foe CSE Students\n' * 5))
            root.add_widget(item)

        # Reurn the root
        return root

    # Run the App


if __name__ == '__main__':
    AccordionApp().run()
