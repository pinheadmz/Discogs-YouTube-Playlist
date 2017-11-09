# YouTube playlist from Discogs collection


Get your Discogs personal access token by logging in and then "generating new token":
https://www.discogs.com/settings/developers

That token will go in line 11 of `discvid.py`

Getting a YouTube API OAuth token is a little trickier. Follow the steps listed here:
https://developers.google.com/youtube/v3/getting-started

You need an OAuth 2.0 client ID for an "other"-type project. Download the json file and make sure it is called `client_secrets.json`

Create a playlist on YouTube and add the playlist ID to line 89 on `youtubeapi.py`

Install the dependencies:
```
pip install --upgrade google-api-python-client
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
pip install discogs_client
```

First run the Discogs scraper:

`python discvid.py`

This script should output a json file called `vidlist.json` with an array of all your YouTube links.

Next run the YouTube importer:

`python youtubeapi.py`