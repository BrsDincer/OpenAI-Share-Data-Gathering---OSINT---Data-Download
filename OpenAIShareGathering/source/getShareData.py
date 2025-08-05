from utils.initial_classes import ICLASS,IPROCESS
from utils.initial_directories import DIRECTORIES
from utils.initial_messages import FILENAMEMESSAGE
from typing import Type
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time,os,json

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

class ShareDataCollection(object):
    def __init__(self)->Type[ICLASS]:
        pass
    def __str__(self)->Type[str]:
        return "SHARE DATA COLLECTION MODULATION - INTERNAL MODULATION"
    def __call__(self)->Type[None]:
        return None
    def __getstate__(self)->Type[NotImplementedError]:
        raise NotImplementedError(NotImplemented)
    def __repr__(self)->Type[str]:
        return ShareDataCollection.__doc__
    def __len__(self)->Type[int]:
        return 0
    def SaveDataOnFile(self,fileCode:Type[str],rawData:Type[str])->Type[IPROCESS]:
        newFile = os.path.join(DIRECTORIES.cachePath,f"{fileCode}.json")
        try:
            with open(newFile,"w",encoding="utf-8") as wFile:
                json.dump(rawData,wFile,ensure_ascii=False,indent=2)
            print(FILENAMEMESSAGE.format(fileCode=fileCode))
        except:
            pass
    def GetData(self,url:Type[str])->Type[IPROCESS]:
        try:
            option = Options()
            option.add_argument("--headless")
            option.add_argument("--disable-gpu")
            option.add_argument("--disable-extensions")
            option.add_argument("--disable-blink-features=AutomationControlled")
            option.add_argument("--log-level=3")
            option.add_argument("--start-maximized")
            option.add_argument("--no-sandbox")
            option.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(options=option)
            driver.get(url)
            time.sleep(3)
            source = driver.page_source
            if source and (source is not None) and len(source) != 0:
                soup = BeautifulSoup(source,"html.parser")
                driver.quit()
                messages = soup.find_all(attrs={"data-message-author-role":True})
                if len(messages) > 0:
                    conversation = []
                    fileCode = url.split("/")[-1].replace("-","_")
                    for id,msg in enumerate(messages):
                        role = msg["data-message-author-role"]
                        text = msg.get_text(strip=False)
                        conversation.append(
                            {
                                "id":f"turn_{id+1}",
                                "role":role,
                                "text":text
                            }
                        )
                    self.SaveDataOnFile(fileCode=fileCode,rawData=conversation)
                else:
                    pass
            else:
                pass
        except:
            pass



