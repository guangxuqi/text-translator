import pandas as pd
from tqdm import tqdm
from googletrans import Translator

class TextTranslator:
    def __init__(self, max_length=4500, src='pt', dest='zh-cn'):
        self.max_length = max_length
        self.src = src
        self.dest = dest
        self.translator = Translator()
        
    def detect_language(self, text):
        # Get the code corresponding to the language
        detection = self.translator.detect(text)
        language_code = detection.lang
        return language_code

    def batch_translate(self, series):
        # Translate text in batches
        current_chunk = []
        current_size = 0
        translated_texts = []

        for text in tqdm(series, desc="Translation Progress", unit="character"):
            if current_size + len(text) + 1 < self.max_length:
                current_size = current_size + len(text) + 1
                current_chunk.append(text)
            else:
                batch_texts = "\n".join(current_chunk)
                translated_batch = self.translator.translate(batch_texts, src=self.src, dest=self.dest)
                translated_texts.extend(translated_batch.text.split("\n"))
                current_size = len(text) + 1
                current_chunk = [text]

        if current_chunk:
            batch_texts = "\n".join(current_chunk)
            translated_batch = self.translator.translate(batch_texts, src=self.src, dest=self.dest)
            translated_texts.extend(translated_batch.text.split("\n"))

        translated_series = pd.Series(translated_texts, index=series.index)

        return translated_series
