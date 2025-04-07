from langdetect.detector import LangDetectException
import spacy
from langdetect import detect
from utils.map_functions import map_deep

nlp_de = spacy.load("de_core_news_sm")
nlp_en = spacy.load("en_core_web_sm")


def _detect_language(text):
    try:
        if detect(text) == "de":
            return [elem.text for elem in nlp_de(text).sents]
        else:
            return [elem.text for elem in nlp_en(text).sents]
    except LangDetectException:
        return text


def split_text_spacy(data):
    return map_deep(data, _detect_language)
