# scrapers-for-journalists
Scraper(s) to help the journalists retrieve data or monitor sites for potential leads for stories.

Every file in `utils/`can be imported in your scrapers, as it is added as a package in pyproject.toml. For example, you can import the BaseScraper with generic utilities like: `from base import BaseScraper`.

## Description of current scrapers

### domstol.dk

This scrapers retrieves information about current court cases ("retslister") in Danish "byretter" (Currently, Højesteret etc. are not included). Civil cases and tvangsauktioner are filtered away. Relevance of the cases are estimated based on keywords and "gerningskoder" (types of crimes) from the Danish Police.

The scrapers runs every second Monday at 9.00. To run it manually, use:
```
poetry run python domstol-dk/retrieve.py --outfile test.xlsx
```
