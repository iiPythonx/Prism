# Modules
import website
from os import environ, getenv

from dotenv import load_dotenv
from logging import getLogger, ERROR

from flask import Flask, render_template
from flask import url_for, make_response

from requests_oauthlib import OAuth2Session
from flask import session, request, redirect

# Initialization
app = website.app

load_dotenv()

# Discord OAuth2 Variables
OAUTH2_CLIENT_ID = 685550504276787200
OAUTH2_CLIENT_SECRET = getenv("CLIENT_SECRET")
OAUTH2_REDIRECT_URI = "https://prismdiscord.cf/discord/callback"

API_BASE_URL = "https://discordapp.com/api"
AUTHORIZATION_BASE_URL = f"{API_BASE_URL}/oauth2/authorize"
TOKEN_URL = f"{API_BASE_URL}/oauth2/token"

# Environment Variables
environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"

app.config["SECRET_KEY"] = OAUTH2_CLIENT_SECRET

# Setup our logging
flasklog = getLogger("werkzeug")
flasklog.setLevel(ERROR)

# Discord Connections
def token_updater(token):
    
    session["oauth2_token"] = token

def make_session(token = None, state = None, scope = None):
    
    return OAuth2Session(
        
        client_id = OAUTH2_CLIENT_ID,
        token = token,
        scope = scope,
        auto_refresh_kwargs = {
            "client_id": OAUTH2_CLIENT_ID,
            "client_secret": OAUTH2_CLIENT_SECRET,
        },
        auto_refresh_url = TOKEN_URL,
        token_updater = token_updater,
        redirect_uri = OAUTH2_REDIRECT_URI,
        state = state
        
    )

def get_user():

    discord = make_session(token = session.get("oauth2_token"))
    
    user = discord.get(f"{API_BASE_URL}/users/@me").json()

    if not "code" in user:

        user["avatar"] = f"https://cdn.discordapp.com/avatars/{user['id']}/{user['avatar']}"

    else:

        if user["code"] == 0:

            return None

    return user

def get_guilds():

    discord = make_session(token = session.get("oauth2_token"))
    
    guilds = discord.get(f"{API_BASE_URL}/users/@me/guilds").json()

    if "code" in guilds:

        if guilds["code"] == 0:

            return None

    _guilds = {}
    _guildids = []

    for guild in website.bot.guilds:

        _guildids.append(guild.id)

    for guild in guilds:

        if (int(guild["permissions_new"]) & 0x20 == 0x20):

            _guilds[str(guild["id"])] = guild

            if int(guild["id"]) in _guildids:

                guild["in_server"] = True

            else:

                guild["in_server"] = False
                
    return _guilds

# Routes
@app.route("/")
def index():

    return render_template(
        "index.html",
        user = get_user()
    ), 200

@app.route("/manage")
def manage():

    guilds, user = get_guilds(), get_user()

    if not guilds:

        return redirect(url_for("discord_connect"))

    return render_template(
        "dashboard.html",
        user = user,
        guild = None,
        guilds = guilds
    )

@app.route("/logout")
def logout():

    resp = make_response("<script>window.location.href = '/';</script>")

    resp.set_cookie("session", "", expires = 0)

    return resp, 200

@app.route("/discord/auth")
def discord_connect():

    scope = request.args.get(
        "scope",
        "identify guilds"
    )

    discord = make_session(scope = scope.split(" "))

    authorization_url, state = discord.authorization_url(AUTHORIZATION_BASE_URL)

    session["oauth2_state"] = state
    
    return redirect(authorization_url)

@app.route("/discord/callback")
def discord_callback():
        
    if request.values.get("error"):
        
        return request.values["error"]
    
    discord = make_session(state = session.get("oauth2_state"))
    
    token = discord.fetch_token(
        
        TOKEN_URL,
        client_secret = OAUTH2_CLIENT_SECRET,
        authorization_response = request.url
        
    )
    
    session["oauth2_token"] = token
    
    return redirect(url_for("index"))
