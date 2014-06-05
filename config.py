# separator used by search.py, categories.py, ...
SEPARATOR = ";"

LANG            = "en_US" # can be en_US, fr_FR, ...
ANDROID_ID      = "33E2C8585B8FB514"  #"xxxxxxxxxxxxxxxx"
GOOGLE_LOGIN    = "dflower.android.1@gmail.com" # "username@gmail.com"
GOOGLE_PASSWORD = "semigod-_-"
AUTH_TOKEN      = None # "yyyyyyyyy"

# force the user to edit this file
if any([each == None for each in [ANDROID_ID, GOOGLE_LOGIN, GOOGLE_PASSWORD]]):
    raise Exception("config.py not updated")

