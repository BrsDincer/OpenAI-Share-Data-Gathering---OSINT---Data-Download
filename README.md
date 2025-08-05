# OpenAI Share Links - Gathering Data & Conversations

This tool is designed for educational purposes and is designed to record OpenAI share links and the conversations within the links.


> For requirenments:

```
cd OpenAIShareGathering
pip install -r requirements.txt
 ```

After saving the file, you can run these commands below in an IDE of your choice.

To save OpenAI Share links as JSON:

```
wbmac = WaybackMachineIntelligence()
wbmac.GetIntelligence()
```

To save individual conversations within OpenAI Share links as JSON:

```
SaveShareData()
```

