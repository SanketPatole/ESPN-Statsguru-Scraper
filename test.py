from espn_cricinfo_scraper import ESPNScraper as es

df = es().get_score()

print(df.info())

print(df.head())
