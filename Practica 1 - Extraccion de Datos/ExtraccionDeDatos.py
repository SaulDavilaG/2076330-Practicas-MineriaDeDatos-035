import requests as rq

print("Empezando descarga")
url="https://zenodo.org/record/4265051/files/recogiendo_tomates.csv"

req= rq.get(url)

filename =url.split('/')[-1]

with open(filename, 'wb') as output_file:
	output_file.write(req.content)
print("Descarga completada")