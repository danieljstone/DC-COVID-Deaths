# DC-COVID-Deaths
Scraping D.C. COVID Reports for Mortality Demographic Data

As of March 24, 2021 Washington, D.C. publishes summary data about who has died of COVID using ten-year age-brackets, whereas it uses some form of five-year bracketing for all other reporting such as vaccination and case counts. This makes it impossible to calculate numbers such as case fatality rates and determine how vaccine distribution compares to mortality data.

However, the District does publish a daily report listing the age and gender of each COVID fatality.  Here, I include a  script that scrapes these daily reports over a given period of time for more detailed age data. In the early days of the pandemic (and a few days since then), the city reported deaths differently, so I have transcribed data from those periods in csv file also posted in this repo.

![pfr](https://raw.githubusercontent.com/danieljstone/DC-COVID-Deaths-Age-Gender/main/graphs/pfr.png)
![cfr](https://raw.githubusercontent.com/danieljstone/DC-COVID-Deaths-Age-Gender/main/graphs/cfr.png)
