import requests, re, csv, sqlite3, pathlib, sys, time
db = pathlib.Path("bookkeeping.db")
conn = sqlite3.connect(db)
conn.execute("""CREATE TABLE IF NOT EXISTS expense(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 item TEXT, amount REAL, category TEXT, date TEXT)""")
pages = int(sys.argv[sys.argv.index('-p')+1]) if '-p' in sys.argv else 2
for page in range(1, pages+1):
    url = f"https://example.com/page/{page}"          # 演示 URL
    text = requests.get(url, timeout=10).text
    rows = re.findall(r'(?i)(餐饮|交通|购物).*?¥(\d+\.\d{1,2})', text)
    for cat, amt in rows:
        conn.execute("INSERT INTO expense(item,amount,category,date) VALUES (?,?,?,?)",
                     (cat, float(amt), cat.lower(), "2025-12-13"))
    time.sleep(1)                                     # 礼貌爬取
conn.commit(); conn.close()
print(f"Page {pages} done → {db.resolve()}")