import feedparser

def getRss(subreddit: str) -> str:
    headers = { 'User-Agent' : 'Mozilla/5.0' }
    return feedparser.parse(f"https://www.reddit.com/r/{subreddit}.xml")

def parse(entry):
    return {"author":entry["authors"][0]["name"], "title":entry["title"], "body":entry["content"][0]["value"]}