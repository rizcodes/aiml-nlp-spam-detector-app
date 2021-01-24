import os
import nltk
import pickle
import pandas as pd
from django.conf import settings
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Load the trained ML model and fitted TFIDF vectorizer
model_file_path = os.path.join(settings.STATIC_DIR, 'dt_model.pkl')
tfidf_file_path = os.path.join(settings.STATIC_DIR, 'tfidf.pkl')

model = pickle.load(open(model_file_path, 'rb'))
tfidf = pickle.load(open(tfidf_file_path, 'rb'))

# NLP stuff
nltk_data_path = os.path.join(settings.STATIC_DIR, 'nltk_data')
nltk.data.path.append(nltk_data_path);
tokenizer = RegexpTokenizer(r'\w+')
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))


class MessageDetection:
    def __init__(self, msg):
        self.msg = msg

    def _decode_label(self, num):
        if num == 1:
            return 'spam'
        return 'ham'

    def _normalize(self):
        norm_msg = []
        sentence = tokenizer.tokenize(self.msg)
        for word in sentence:
            if (word in stop_words) or (word.isspace()) or (word==''):
                continue
            s_word = stemmer.stem(word)
            norm_msg.append(s_word)
        return " ".join(norm_msg)

    def _parse(self, message):
        raw_input = {'data': [message]}
        df = pd.DataFrame(raw_input)
        return df.data

    def _vectorize(self, data):
        feature_vector = tfidf.transform(data)
        return feature_vector

    def classify(self):
        message = self._normalize()
        data = self._parse(message)
        vector = self._vectorize(data)
        y_hat= model.predict(vector)
        y_pred = self._decode_label(y_hat)
        return y_pred
