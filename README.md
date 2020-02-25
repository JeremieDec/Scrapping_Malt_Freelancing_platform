## Project: Scraping data over Malt.fr

### Install

This project requires **Python** and the following libraries (+ Pandas) installed :

- [Webdriver Manager](https://www.npmjs.com/package/webdriver-manager)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)

### Components:
1. Web Scraper (Python + Beautiful Soup).
   * Scrapes people profiles from Malt website.
   * Saves results in SQL Server database via flask Web API.
   * Run with `pipenv run python3 scrapping.py'
2. Python Web API for [create, read] access over the data.
