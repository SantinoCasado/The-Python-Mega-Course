from googletrans import Translator
import asyncio

async def translate(text):
    translator = Translator()
    translation = await translator.translate(text=text, dest='en')
    return translation.text