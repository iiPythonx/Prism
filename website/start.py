# Modules
import website
from threading import Thread

# Functions
def startServer(bot):

    website.setbot(bot)

    t = Thread(target = website.app.run, args = ["0.0.0.0", 80])

    t.start()