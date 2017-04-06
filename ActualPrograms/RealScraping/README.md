# Century 21 Web Scraper
This is an application that scrapes a cached version of Century 21's web site listings.
Please refer to the following url to understand how the program operates:
http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/

- Requirement:
	- This program scrapes the Century 21 listings in Rock Springs, Wyoming and captures
the data about the available houses, then outputs them into a CSV file for potential further
analysis.
- Packages Used:
	- BeautifulSoup (bs4)
	- Pandas
- Data Source:
	- Cached Century 21 Website.

# Data Scraped Includes (These can be Null):
	
	- 'Street' Address
	- 'Address' being the City, State, ZIP Code
	- Price of the listing.
	- # of Beds
	- # of Full Baths
	- Square Footage
	- # of Half Baths
	- Lot Size if available.