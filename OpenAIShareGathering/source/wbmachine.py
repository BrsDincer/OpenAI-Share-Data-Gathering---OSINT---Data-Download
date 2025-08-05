from utils.initial_classes import ICLASS,IPROCESS
from utils.initial_messages import INFORMATIONMESSAGE
from utils.initial_directories import DIRECTORIES
from typing import Type
from bs4 import BeautifulSoup
import os,requests,json

os.makedirs(DIRECTORIES.sourcePath,exist_ok=True)

class WaybackMachineIntelligence(object):
    def __init__(self)->Type[ICLASS]:
        self.baseURL = "https://web.archive.org/cdx/search/cdx?url=chat.openai.com/share/*&output=json&fl=original&filter=statuscode:200"
        self.basePATH = DIRECTORIES.sourcePath
        print(INFORMATIONMESSAGE.format(processType="WAYBACKMACHINE"))
    def __str__(self)->Type[str]:
        return "WAYBACKMACHINE INTELLIGENCE MODULATION - EXTERNAL MODULATION"
    def __call__(self)->Type[None]:
        return None
    def __getstate__(self)->Type[NotImplementedError]:
        raise NotImplementedError(NotImplemented)
    def __repr__(self)->str:
        return WaybackMachineIntelligence.__doc__
    def __len__(self)->Type[int]:
        return 0
    def CustomExtractor(self,HTMLContent:Type[ICLASS])->Type[str]:
        soup = BeautifulSoup(HTMLContent,"html.parser")
        divs = soup.find_all("div",class_="whitespace-pre-wrap")
        print(divs)
        return divs
    def GetIntelligence(self)->Type[IPROCESS]:
        if os.path.exists(self.basePATH):
            with open(self.basePATH,"r",errors="ignore",encoding="utf-8") as rFile:
                data = json.load(rFile)
            for dt in data:
                try:
                    print(dt[0])
                    session = requests.get(dt[0],verify=True,stream=True,timeout=100,allow_redirects=True)
                    if 300 > session.status_code >= 200:
                        soup = BeautifulSoup(session.text,"html.parser")
                        body = soup.find_all("body")
                        print(body)
                        for div in body:
                            att = div.find_all(attrs={"data-message-author-role": "user"})
                            print(att)
                        break
                except:
                    pass
        

