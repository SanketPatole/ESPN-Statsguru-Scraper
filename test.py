from espncricket import espncricket as es

df = es().get_score()

print(df.info())

