import requests
from fake_useragent import UserAgent


class Request:
    def __init__(self):
        self.ua = UserAgent()
        self.formatted_url = "https://stats.espncricinfo.com/ci/engine/stats/index.html?" \
                             "type={data_type};" \
                             "class={match_type};" \
                             "view={view_type};" \
                             "template={template};" \
                             "page={page_num}"

    def build_url(self, data_type, match_type, view_type, template, page_num):
        return self.formatted_url.format(data_type=data_type, match_type=match_type, view_type=view_type,
                                         template=template, page_num=page_num)

    def get_url_object_with_agent(self, url):
        header = {"User-Agent": str(self.ua.random)}
        return requests.get(url, headers=header).text
