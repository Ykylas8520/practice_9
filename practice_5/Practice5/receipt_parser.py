import re
import json

f = open("raw.txt", "r", encoding="utf-8")
text = f.read()

products = re.findall(r'\d+\.\s*\n\s*(.+)', text)

prices = re.findall(r'\d+\s*x\s*([\d\s]+,\d{2})', text)

total = re.search(r'ИТОГО:\s*\n\s*([\d\s]+,\d{2})', text)

date = re.search(r'Время:\s*([\d\.]+\s[\d:]+)', text)

pay = re.search(r'(Банковская карта|Наличные)', text)

data = {}

data["products"] = products
data["prices"] = prices

if total:
    data["total"] = total.group(1)

if date:
    data["date_time"] = date.group(1)

if pay:
    data["payment_method"] = pay.group(1)

print(json.dumps(data, indent=4, ensure_ascii=False))