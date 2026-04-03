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
        
        # 10개의 뉴스 덩어리를 찾는 건 아까 성공했으니 그대로 둡니다.
        news_list = soup.select("ul.c-list-basic > li")
        
        for li in news_list:
            # 💡 필살기 1: 이름표 무시! li 안의 모든 a 태그(링크)를 다 가져옵니다.
            a_tags = li.find_all("a")
            if not a_tags:
                continue
                
            # 가져온 링크들 중에서 '글자 수가 가장 긴 것'을 기사 제목으로 확정해버립니다.
            title_tag = max(a_tags, key=lambda tag: len(tag.get_text(strip=True)))
            title = title_tag.get_text(strip=True)
            href = title_tag.get("href", "#")
            
            # 제목 글자가 5자 이하면 엉뚱한 버튼일 확률이 높으니 버립니다.
            if len(title) < 5:
                continue
            
            # 💡 필살기 2: 언론사도 마찬가지로 'info'라는 글자가 들어간 요소 중 하나를 억지로 잡습니다.
            press_tag = li.select_one("[class*='info']")
            press = press_tag.get_text(strip=True) if press_tag else "언론사"
            
            # 💡 필살기 3: 요약문은 보통 p 태그(문단) 안에 있습니다. p 태그 중 제일 긴 것을 요약으로 잡습니다.
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
    print(f"✅ 총 수집된 기사 수: {len(articles)}")
    return articles