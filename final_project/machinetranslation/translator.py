"""This module allows to perform translation English To/From French"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

print(apikey)

authenticator = IAMAuthenticator('ES2r4BzftyGHa4Wgkzu7mUlIotISPkMCb-w4ZhcVSvUZ')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-south.language-translator.watson.\
cloud.ibm.com/instances/013f58d4-1e31-44a4-b010-0db10d251ce7')


def english_to_french(english_text):
    """Translates English to French"""
    fr_trans = language_translator.translate(text=english_text,
                                             model_id='en-fr').get_result()
    return fr_trans.get("translations")[0].get("translation")


def french_to_english(french_text):
    """Translates French to English"""
    eng_trans = language_translator.translate(text=french_text,
                                              model_id='fr-en').get_result()
    return eng_trans.get("translations")[0].get("translation")
