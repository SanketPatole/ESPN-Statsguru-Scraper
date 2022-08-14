from ESPNScraper import ESPNScraper as es

df = es().get_score()

print(df.info())

print(df.head())
