"""
translator module
"""
# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def englishToFrench(englishText):
    """
    english to french
    """
    if englishText is not None:
        translation = language_translator.translate(
            text=englishText,
            model_id='en-fr'
            ).get_result()
        frenchText = translation['translations'][0]['translation']
        return frenchText

    return None

def frenchToEnglish(frenchText):
    """
    french to english
    """
    if frenchText is not None:
        translation = language_translator.translate(
            text=frenchText,
            model_id='fr-en'
        ).get_result()
        englishText = translation['translations'][0]['translation']
        return englishText

    return None
