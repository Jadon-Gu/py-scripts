# day04_regex_file_crawler.py
import re, csv, sys, requests, datetime, pathlib
url = sys.argv[sys.argv.index('-u')+1] if '-u' in sys.argv else 'https://httpbin.org/html'
text = requests.get(url, timeout=10).text
prices = re.findall(r'¥(\d+\.\d{1,2})', text)
today = datetime.date.today().isoformat()
out = pathlib.Path(f'prices_{today}.csv')
with out.open('w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows([[p] for p in prices])
print(f'Captured {len(prices)} prices → {out.resolve()}')