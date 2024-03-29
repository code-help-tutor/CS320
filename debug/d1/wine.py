WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
import os, sys, json, csv

def wine_search(path, key, value):
    wines = []
    if os.path.exists(path):
        with open(path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row[key] == value:
                    wines.append(f"{row['Variety']} by {row['Winery']}")
    return wines
