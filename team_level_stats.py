from fake_useragent import UserAgent
import pandas as pd
import requests
import time

timestamp_str = time.strftime("%Y%m%d-%H%M%S")
match_types = {'Test':'1', 'ODI':'2', 'T20':'3'}
match_type = ''
if sys.argv[1:][0] not in match_types:
	print("The match type provided is invalid. Please provide valid match type: Test/ODI/T20"
	exit(0)
else:
	match_type = match_types[sys.argv[1:][0]]

ua = UserAgent()
page_num = 1
url = "https://stats.espncricinfo.com/ci/engine/stats/index.html?class="+match_type+";page="+str(page_num)+";result=1;result=2;result=3;result=4;template=results;type=team;view=year"
header = {"User-Agent": str(ua.random)}
url_with_agent = requests.get(url, headers=header).text
df = pd.read_html(url_with_agent)
number_of_pages = int(str(df[1][0]).split("\n")[0].split(" ")[7])

result_set = pd.DataFrame()

while (page_num <= number_of_pages):
    header = {"User-Agent": str(ua.random)}
    url_with_agent = requests.get(url, headers=header).text
    df = pd.read_html(url_with_agent)[2]
    result_set = result_set.append(df)
    print("Page "+str(page_num)+" of "+str(number_of_pages)+" downloaded.")
    page_num += 1
result_set.to_csv(f'resultset_{timestamp_str}.csv')
