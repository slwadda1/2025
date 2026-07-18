import feedparser
import json

url = "https://fitgirl-repacks.site/feed/"
feed = feedparser.parse(url)
games = []

for entry in feed.entries[:10]:
    game_data = {
        "title": entry.title,
        "link": entry.link,
        "summary": entry.summary,  # මෙතනින් විස්තරය ගන්නවා
        "image": entry.media_content[0]['url'] if 'media_content' in entry else "" # මෙතනින් පින්තූරය ගන්නවා
    }
    games.append(game_data)

with open('games.json', 'w', encoding='utf-8') as f:
    json.dump(games, f, indent=4)