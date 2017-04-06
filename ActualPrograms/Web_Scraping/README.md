#amazonProducts.py
This is a program that scrapes Amazon for product searches a user provides. It opens a new tab for each product that comes up in the search. This excludes sponsored searches (seems they're really pushing for that now...)

#imgurSearch.py
This is functionally similar to amazonProducts except with imgur, a site for viewing web images.

#redditScrape.py - Unfinished
This is a program where I am ~trying~ to scrape Reddit's front page to collect data about the posts there and ran into an Too Many Requests issue. As I read more about this, it seems as if Reddit purposely limits the request of default web scraping tools in order to keep control of monitoring what is scraping their website. The more I read about their API, the more I realize I am going to need to scrape using their API and using my own unique user_agent which is primarily what they care about.