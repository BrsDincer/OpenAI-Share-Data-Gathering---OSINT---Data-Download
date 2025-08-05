from utils.initial_classes import IDIRECTORY
from typing import Type
import os

class DIRECTORIES:
    cachePath:Type[IDIRECTORY] = os.path.join(os.getcwd(),"cache")
    dataPath:Type[IDIRECTORY] = os.path.join(os.getcwd(),"data")
    cachePath:Type[IDIRECTORY] = os.path.join(os.getcwd(),"cache")
    sourcePath:Type[IDIRECTORY] = os.path.join(os.getcwd(),"data","openai_share_data.json")