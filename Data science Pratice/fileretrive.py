import requests

# import pandas as pd

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"

async def download(url,filename):
    response = requests.get(url)
    if(response.status_code == 200):
        with open(filename, 'wb') as f:
            f.write(response.text.encode('utf-8'))
            return response.text
           
async def main():
    text = await download(url, "example1.txt")
    print(text)
    
import asyncio
asyncio.run(main())     

