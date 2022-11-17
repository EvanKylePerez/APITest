import requests

url = "https://pixabay.com/api/?key=30096829-641033d3201b67547a24be81b&q=Landscape&image_type=vector&orientation=horizontal&editors_choice=true&per_page=3"

payload={}
headers = {
  'Cookie': '__cf_bm=hy.P.3IqRUJic2OXgBDzmJMTDvaLNh2hhcFLY7PdUlU-1668654936-0-AROZ98eJAoYH6f+eK2R3i4eS5ugBDcNKqd60Kv8VXer+4LL3mz2y2Fz6UB6xbDv+Z9Aljuc4wRryn/xnA3v24V8=; anonymous_user_id=None; csrftoken=Ry0kXWHKJcg6rr7bjygT8o0WJ8xxwfGAVtZV5wQHuZzO3w73EjJvcCKmRs16yplK'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)