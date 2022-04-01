import re
import requests
from bs4 import BeautifulSoup

LIMIT = 50

def get_last_pages(url) -> int:
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find("h2", {"class": "jobTitle"}).string
    if title is None:
        title = html.select_one(".jobTitle > span").string
    company = html.find("span", {"class": "companyName"}).string
    location = html.find("div", {"class": "companyLocation"}).string
    job_id = html["data-jk"]
    return {"title": title, 
            "company": company,
            "location": location,
            "link": f"https://kr.indeed.com/viewjob?jk={job_id}&tk=1fv7kk5etk3pt800&from=serp&vjs=3"}


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Indeed: Page: {page}")
        result = requests.get(f"{url}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')
        #print(result.status_code)
        results = soup.find_all("a", {"class": "tapItem"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs(word):
    url = f"https://kr.indeed.com/jobs?q={word}&limit={LIMIT}"
    last_page = get_last_pages(url)
    jobs = extract_jobs(last_page, url)
    return jobs