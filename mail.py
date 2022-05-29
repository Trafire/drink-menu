import html2text
from promail.clients.gmail import GmailClient
from promail_template.templates.full.hello_world.template import HelloWorld
from main import Drink

from colour_scheme import random_colour_scheme
from menu import Menu

random_colours = random_colour_scheme("ui")

choices = 'Mojito', 'Old Fashioned', 'Negroni', 'Daiquiri', 'Ramos Gin Fizz', 'Orange Push-up'

drinks = [Drink(choice).template for choice in choices]

data = {
    "style": {
        "background_colour": random_colours[0],
        "sub_header":random_colours[1],
        "header_colour": random_colours[2],
        "border_colour": random_colours[3],
        "text_colour": random_colours[4],
    },
    "title": "Social Shindig",
    "drinks":drinks,

}




template = Menu(data)
#template.preview_html()
client = GmailClient("antoinewood@gmail.com")
client.send_email(
    recipients="antoinewood@gmail.com",
    subject="Magic",
    htmltext=template.html,
    plaintext=template.plaintext
)




