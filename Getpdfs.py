import os
import requests

url1 = "https://aclanthology.org/E17-"
indices = [str(i) for i in range(5001,5007)]

urls = [url1+index+".pdf" for index in  indices]

outputdirectory = "E:\EACL\PDFS"
i=1046
for url in urls:
    response = requests.get(url)
    file_path = os.path.join("E:\EACL\PDFS", f"Document{i}.pdf")
    i+=1
    with open(file_path, 'wb') as f:
        f.write(response.content)
