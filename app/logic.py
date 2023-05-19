from bs4 import BeautifulSoup as bs
from textblob import TextBlob as tb
from gtts import gTTS
import requests as req
import os


class NewsReader:
    language_selected = None

    source_lang_list = []
    selected_language = None
    converted_language_list = []
    def __init__(self):
        print("--------------------------", os.getcwd())
    def language_selecter(self,lang,out_lang):
        self.output_language = out_lang
        self.selected_language = lang
        # print(f"----->>> your language {lang}")
        if lang == "English":
            self.english()
        elif lang == "Russia":
            self.russia()
        elif lang == "China":
            self.china()
        elif lang == "Arab":
            self.arabic()
        elif lang == "Japan":
            self.japan()
        elif lang == "French":
            self.french()
        elif lang == "Korea":
            self.korean()
        elif lang == "Spain":
            self.spain()

    def HTML_Object(self,baseURL):
        url = baseURL
        agent = {
                    "UserAgent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0"
                }
        try:
            requesting = req.get(
                                    url=url,
                                    headers=agent
                                )
        except Exception:
            print("Check internet connection")
            exit()
        contManu = requesting.content
        soupObject = bs(contManu, 'html.parser')
        return soupObject

    def english(self):
        url = 'https://www.nytimes.com/section/us'
        resultObject = self.HTML_Object(url)
        
        headList = []
        for tmp in resultObject.findAll("h2")[1:6]:
            headList.append(tmp.text.strip()+';')
        
        self.source_lang_list = headList
        return headList   

    def russia(self):
        url = 'https://rt.rs/'
        resultObject = self.HTML_Object(url)
        tags = { "class":"Link-root" }
        headList = []
        for tmp in resultObject.find_all("a",tags)[29:34]:
            headList.append(tmp.text.strip()+';')
        
        self.source_lang_list = headList
        return headList 
     
    def arabic(self):
        tNews = 'https://www.albawabhnews.com/'
        resultObject = self.HTML_Object(tNews)
        headList = []   
        tags = {
                    "class":"list-group-item"
                }
        for tmp in resultObject.findAll("h3")[0:6]:
            headList.append(tmp.text.strip()+';')
        
        self.source_lang_list = headList
        print(headList)
        return headList
        
    def french(self):
        tNews = 'https://www.liberation.fr/'
        resultObject = self.HTML_Object(tNews)
        headList = []   
        tags = {
                    "class":"color_black"
                }
        for tmp in resultObject.find_all("a",tags)[:5]:
            headList.append(tmp.text.strip()+';')
        
        self.source_lang_list = headList
        return headList
    
    def japan(self):
        url = 'https://www.asahi.com/'
        resultObject = self.HTML_Object(url)
        
        headList = []   
        Tags = {
                     "class":"c-articleModule__link"
               }
        for tmp in resultObject.find_all('a', "c-articleModule__link")[:5]:
             headList.append(tmp.span.text.strip()+';')
        
        self.source_lang_list = headList
        return headList 
    
    def korean(self):
        url = 'https://www.donga.com/'
        resultObject = self.HTML_Object(url)
        
        tags = {"class":"tit"}
        headList = []   
        for tmp in resultObject.find_all("h3",tags)[:5]:
             headList.append(tmp.a.text.strip()+';')
        
        self.source_lang_list = headList
        return headList
    
    def spain(self):
        url = 'https://elpais.com/'
        resultObject = self.HTML_Object(url)
        
        tags = {"class":"c_t"}
        headList = []   
        for tmp in resultObject.find_all("h2",tags)[:5]:
             headList.append(tmp.a.text.strip()+';')
        
        self.source_lang_list = headList
        return headList
    
    def china(self):
        url = 'http://cn.chinadaily.com.cn/'
        resultObject = self.HTML_Object(url)
        
        headList = []   
        for tmp in resultObject.find_all("h1")[:5]:
             headList.append(tmp.a.text.strip()+';')
        
        self.source_lang_list = headList
        return headList

    def find_shorcut_language(self):
        if self.selected_language == "English":
            return "en"
        elif self.selected_language == "Russia":
            return "ru"
        elif self.selected_language == "Arab":
            return "ar"
        elif self.selected_language == "Hindhi":
            return "hi"
        elif self.selected_language == "Japan":
            return "ja"
        elif self.selected_language == "China":
            return "zh-TW"
        elif self.selected_language == "French":
            return "fr"
        elif self.selected_language == "Korea":
            return "ko"
        elif self.selected_language == "Spain":
            return "es"


    def conVert(self):
        lists = self.source_lang_list     # original string
        self.sCointain =[]   # converted string
        msource = [] 
        for tmp in lists:
            convertion = tb(tmp)
            self.out = str(convertion.translate(from_lang=self.find_shorcut_language(),to=self.output_language))
            self.sCointain.append(self.out)

    def voice(self):
        lineString = ''.join(self.sCointain)
        auGen = gTTS(lineString, lang=self.output_language)
        auGen.save('news.mp3')