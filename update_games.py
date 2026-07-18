import feedparser
import json

# FitGirl ගේ RSS එකෙන් දත්ත ගන්නවා
url = "https://fitgirl-repacks.site/feed/"
feed = feedparser.parse(url)
games = []

# අලුත්ම ගේම් 10 අරන් ෆයිල් එකට දානවා
for entry in feed.entries[:10]:
    games.append({"title": entry.title, "link": entry.link})

with open('games.json', 'w', encoding='utf-8') as f:
    json.dump(games, f, indent=4)