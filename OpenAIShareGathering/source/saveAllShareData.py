from utils.initial_classes import IPROCESS
from utils.initial_directories import DIRECTORIES
from source.getShareData import ShareDataCollection
from typing import Type
import json

def SaveShareData()-> Type[IPROCESS]:
    shareEngine = ShareDataCollection()
    dataPath = DIRECTORIES.sourcePath
    with open(dataPath,"r",errors="ignore",encoding="utf-8") as rFile:
        data = json.load(rFile)
        for initial in data:
            url = initial[0]
            if url.lower() != "original":
                shareEngine.GetData(url=url)
            else:
                pass


