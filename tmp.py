import json
phone = '''{"nodes": [{"code": "BJ-u-VgDc5a", "date": 1473091330, "dimensions": {"width": 1080, "height": 810}}, {"code": "bla"}]}'''

data = json.loads(phone)

# print(data.get("nodes").get("code"))


fruits = "['apple', 'orange', 'banana']"
import ast
fruits = ast.literal_eval(phone)
print(fruits)