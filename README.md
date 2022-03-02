# DC COVID Deaths
Scraping D.C. COVID Reports for Mortality Demographic Data

As of March 24, 2021 Washington, D.C. publishes summary data about who has died of COVID using ten-year age-brackets (*e.g.* 50-59, 60-69), whereas it uses some form of five-year bracketing (*e.g.* 55-64,65-74) for all other reporting such as vaccination and case counts. This makes it impossible to calculate numbers such as case fatality rates and determine how vaccine distribution compares to mortality data.

However, the District does publish a daily report listing the age and gender of each COVID fatality.  Here, I include a  script that scrapes these daily reports. I run the scraping script every few days, so you can assume that the "dc covid deaths" file is up to date through when it was last updated.

