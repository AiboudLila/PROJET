
import nltk
import pandas as pd 
from keras.preprocessing.text import text_to_word_sequence 
from keras.preprocessing.text import Tokenizer
from nltk.corpus import stopwords

class Data_Processing:
    def __init__(self, subject=False, text=False):
        self.subject=list(subject)
        self.text=text
    def preprocessText(self):
        """Prétraitement des données en remplacant chaque caractere par une expression de façon a garder sa sémantique ..."""
        for id, element in enumerate(self.subject):
            self.subject[id] = self.subject[id].replace(r'£|\$', 'moneysymb')

            self.subject[id] = self.subject[id].replace(r'^\(?[\d]{3}\)?[\s-]?[\d]{3}[\s-]?[\d]{4}$',
                                        'phonenumbr')
            self.subject[id] = self.subject[id].replace(r'\d+(\.\d+)?', 'numbr')
            self.subject[id] = self.subject[id].replace(r'[^\w\d\s]', ' ')
            self.subject[id] = self.subject[id].replace(r'\s+', ' ')      
            self.subject[id] = self.subject[id].replace(r'^\s+|\s+?$', '')
            self.subject[id] = self.subject[id].lower()
            _stopWords = set(stopwords.words('english'))
            _porterStreamer = nltk.PorterStemmer()
            for _id, _element in enumerate(self.subject):
                _elementsplited = _element.split()
                for _keyWord in _elementsplited:
                    if _keyWord in _stopWords:
                        _elementsplited.remove(_keyWord) 
                self.subject[id] = _porterStreamer.stem("".join(_elementsplited))
        return self.subject 
    def tokenize(self):
        """Fonction tokenize elle nous permet de tokenizer et de transformer en matrice ..."""
        for _word in self.text: 
            _tokens = text_to_word_sequence(_word)
            _tokenizer = Tokenizer()
            _tokenizer.fit_on_texts(_tokens)
            _token = _tokenizer.texts_to_matrix(_tokens)
            return _token  

_data = pd.read_csv(r'C:\Users\TRETEC\Desktop\MEMOIRE\data.csv')
_data = _data.fillna(_data['subject'].value_counts().index[0])
_data['subject'] = _data['subject'].astype('str')

#Test processText()
Data_Processing(subject=_data['subject']).preprocessText()
