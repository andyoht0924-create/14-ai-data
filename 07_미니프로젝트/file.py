import csv

def save_to_file(articles):
    with open("ajin_news.csv", "w", encoding="utf-8-sig", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["No", "기사제목", "언론사", "기사요약", "Link"])
        
        for i, article in enumerate(articles):
            csv_writer.writerow([i+1, article["title"], article["press"], article["summary"], article["href"]])