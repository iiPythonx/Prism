# Modules
from flask import Flask
from threading import Thread

# Initialization
app = Flask(
    "Prism Dashboard",
    template_folder = "website/templates"
)

app.static_url_path = "/website/static"

app.static_folder = app.root_path + app.static_url_path

# Routes
from website.views import public

# Bot instance
def setbot(_bot):

    global bot

    bot = _bot
