# Prism
### The only discord bot you need.
---

Prism is a multipurpose discord bot focused on entertainment & currency.
It is built in Python using `discord.py`.

---

#### Setup

##### Step 1
To get started with Prism, first you need to clone the repository.
To do this, pop into a terminal and enter: `git clone https://github.com/ii-Python/Prism.git`.

Upon completion, you should have a new folder called `Prism`.

##### Step 2
In order to begin using Prism, you need to install the dependencies.
Go into the `Prism` folder and open a new terminal.

Then install the dependencies via pip: `pip install -r requirements.txt`.

##### Step 3
Next, you need to create the database files.
Currently, Prism uses a json database (though we will be switching to mongodb soon).

So, create a new folder called `db`.
Inside of `db`, create 2 files labeled `users` and `guilds`.

IMPORTANT: Make sure the files **DO NOT** have a file extension!

##### Step 4
The final step to running Prism is setting up the configuration.
To do this, create a file called `.env` in the root of the directory.

Label the file like so:
```
TOKEN = "Get this token from https://discord.com/developers/applications"

WOLFRAMALPHA_KEY = "Get this token from https://developer.wolframalpha.com/portal/myapps"
```

Then your going to want to comment out line 32 in `main.py`.

##### Final Steps
Finally, after all of that, your ready to start Prism.
To do this, open up a terminal in the root of the directory.

To start Prism, run the following: `python main.py`.

---

Thanks for reading! 😄
Last update: `8/23/2020`

