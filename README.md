# text-translator

# 使用示例

from text_translator import TextTranslator

translator = TextTranslator()

# 创建包含葡萄牙语句子的 DataFrame
portuguese_samples = [
    "Como vai você?",
    "Eu gosto de viajar para Portugal.",
    "A cultura portuguesa é rica e diversificada."
]

data = {'Portuguese Sentences': portuguese_samples}
df = pd.DataFrame(data)

df['translated_result'] = translator.batch_translate(df['Portuguese Sentences'])

print(df)
