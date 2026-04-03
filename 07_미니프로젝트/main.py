# pip install requests
# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

def search_news(keyword):
    articles = []
    
    for page in range(1, 4): 
        url = f"https://search.daum.net/search?w=news&q={keyword}&p={page}"
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        news_list = soup.select("ul.c-list-basic > li")
        
        for li in news_list:
            a_tags = li.find_all("a")
            
            valid_a_tags = []
            for a in a_tags:
                text = a.get_text(strip=True)
                if len(text) > 5 and "톡으로" not in text:
                    valid_a_tags.append(a)
            
            if not valid_a_tags:
                continue
            
            title_tag = valid_a_tags[0]
            title = title_tag.get_text(strip=True)
            href = title_tag.get("href", "#")
            
            press_tag = li.select_one("[class*='info']")
            press = press_tag.get_text(strip=True) if press_tag else "언론사"
            
            p_tags = li.find_all("p")
            if p_tags:
                summary_tag = max(p_tags, key=lambda tag: len(tag.get_text(strip=True)))
                summary = summary_tag.get_text(strip=True)
            else:
                summary = "요약 없음"
            
            news_data = {
                "title": title,
                "press": press,
                "summary": summary,
                "href": href
            }
            articles.append(news_data)
            
    print("-" * 50)
    print(f"총 수집된 기사 수: {len(articles)}")
    return articles