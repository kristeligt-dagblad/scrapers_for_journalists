# scrapers-for-journalists
Scraper(s) to help the journalists retrieve data or monitor sites for potential leads for stories

 - **Tools?** To build new scrapers, try to keep the dependencies to a minimum. You can do a lot with just requests and BeautifulSoup.
 - **Automation?** To make scheduled runs, we are using Github Actions, as the workloads are relatively short-running.
 - **Data storage?** Data is uploaded to [...]

Every file in `utils/`can be imported in your scrapers, as it is added as a package in pyproject.toml. For example, you can import the BaseScraper with generic utilities like: `from base import BaseScraper`.

## Description of current scrapers

### domstol.dk

This scrapers retrieves information about current court cases ("retslister") in Danish "byretter" (Currently, Højesteret etc. are not included). Civil cases and tvangsauktioner are filtered away. Relevance of the cases are estimated based on keywords and "gerningskoder" (types of crimes) from the Danish Police.

The scrapers runs every second Monday at 9.00. To run it manually, use:
```
poetry run python domstol-dk/retrieve.py
```
