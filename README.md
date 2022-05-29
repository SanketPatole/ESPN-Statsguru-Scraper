# ESPN-Statsguru-Scraper


## Introduction

This repository contains the codebase, which can be used to scrape all-time cricket statistics from ESPN Cricinfo.
The entire code is purely written in Python. At the moment, this utility supports scraping of only team-level statistics.
The work is in progress to make it more generic for wider use.


## Prerequisites

### Python requirements

* You need to install Python with version 3.0 or more. You can find the latest version of Python at https://www.python.org/downloads/

* You need to have following Python libraries to be installed.
```sh
pip install numpy
pip install pandas
pip install fake_useragent
pip install requests
```


## How to run the code

* You need to clone the repository to your local system. Open command line/terminal or git bash and run following command.
```sh
git clone https://github.com/SanketPatole/One-Minute-Stats.git
```

* Open command line/terminal and execute following command.
```sh
python "<absolute path of the repository>/team_level_stats.py <match_type>" #match_type can be either Test, ODI or T20 
```

* After successful execution, a csv file will be created at current path with all the scraped data.


## License Information

Please refer "LICENSE" file to know the license details.
Before reusing this code, you will need to take a written permission from me.
You can contact me at sanketpatole1994@outlook.com

