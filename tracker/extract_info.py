'''Get information from McDonald Observatory website.'''
import re
import bs4 as bs
import urllib.request

def set_page_source(page):
    '''Takes a page name of the McDonald Observatory website and returns a beautiful soup object.'''
    source = urllib.request.urlopen('https://mcdonaldobservatory.org/' + page).read()
    soup = bs.BeautifulSoup(source,'lxml')
    
    return soup

def is_open():   
    '''Evaluates whether the Observatory may be open.'''
    soup = set_page_source('visitors')
    full_text = soup.get_text()

    if "remains closed to the public" not in full_text:
        is_open = "The McDonald Observatory may now be open! Check here: " + "https://mcdonaldobservatory.org/visitors"
    else:
        is_open = "The McDonald Observatory is still not open to the public.\n"
    return is_open

def get_release_max_date(soup):
    '''Extracts the latest press release date.'''
    words = [a['href'] for a in soup.find_all('a', href=True) if a.text]
    pr_2020 = [(word[15:19]+word[19:21]+word[21:23])
               for word in words if "news/releases/2020" in word]
    pr_date = max(pr_2020)
    return pr_date


def get_latest_pr():
    '''Extracts the title of the latest press release'''
    soup = set_page_source('news/releases')

    max_pr_date = get_release_max_date(soup)
    max_pr_date_clean = max_pr_date[0:4]+"-"+max_pr_date[4:6]+"-"+max_pr_date[6:8]
    
    latest_pr = soup.find("a", href=re.compile(max_pr_date)).text
    
    pr_msg = "\nA new press release was written on " + max_pr_date_clean + "... " + latest_pr + "." + "\nClick here to read full article: " + "https://mcdonaldobservatory.org/news/releases."
    return pr_msg