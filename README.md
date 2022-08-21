# ESPN-Statsguru-Scraper


## Introduction

An easy-to-use python scraper to pull all-time cricket statistics from ESPN Cricinfo.


## Prerequisites

### Python requirements

* You need to install Python with version 3.4 or more. You can find the latest version of Python at https://www.python.org/downloads/

* Install the library as follows.

```
pip install espncricket
```

## How to run the code

```
import espncricket.ESPN as ESPN

df = ESPN().get_score()
print(df.head())

```

* After successful execution, pandas dataframe object is returned.


## License Information

Please refer "LICENSE" file to know the license details.
Before reusing the code, please take a written permission from me.
You can contact me at sanketpatole1994@outlook.com

