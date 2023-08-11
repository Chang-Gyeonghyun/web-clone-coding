from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    results = []
    for page in range(pages):
        options = Options()
        driver = webdriver.Chrome(options=options)
        #웹이 bot 방지를 위해 Ai 접근 차단함 -> 브라우저로 직접 접근
        base_url = "https://kr.indeed.com/jobs"
        driver.get(f"{base_url}?q={keyword}&start={page*10}")

        soup = BeautifulSoup(driver.page_source,"html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all('li', recursive=False) #바로 아래 요소만을 가져오기 위해서 파라미터 설정
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a") #h2 태그를 찾고 그 안에 a태그를 가져와라
                title = anchor['aria-label']
                link = anchor['href'] #a태그는 내부 속성이 dict entity형태로 나타난다.
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                'link': f"https://kr.indeed.com{link}",
                'company': company.string.replace(","," "),
                'location': location.string.replace(","," "),
                'position': title.replace(","," ")
                }
                results.append(job_data)
    return results
            
def get_page_count(keyword):
    options = Options()
    driver = webdriver.Chrome(options=options)
    base_url = "https://kr.indeed.com/jobs?q="
    driver.get(f"{base_url}{keyword}")

    soup = BeautifulSoup(driver.page_source,"html.parser")
    pagination = soup.find('nav', attrs={"aria-label": "pagination"}) #태그에 대한 클래스가 아닌 속성 값을 받기 위해서는 다음 과 같이 key:value로 이용할 수도 있다.
    if pagination == None:
        return 1 #페이지 목록이 없는 경우 함수 종료
    
    pages = pagination.find_all("div", recursive=False)
    count = len(pages)
    
    if count >= 5:
        return 5 #5페이지만 스크래핑 하도록 한다.
    else: return count
    