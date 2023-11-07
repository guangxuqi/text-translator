# 文本翻译器（Text Translator）

这是一个简单的文本翻译器，用于将一系列文本从一种语言翻译成另一种语言。它基于 `googletrans` 库，需要确认网络能够访问google翻译。

## 安装

在使用此文本翻译器之前，请确保你已经安装了以下依赖项：

- pandas
- tqdm
- googletrans==4.0.0-rc1

你可以使用 `pip` 安装它们：pip install pandas tqdm googletrans==4.0.0-rc1


## 使用

为了使用这个文本翻译器，你需要导入它并创建一个 `TextTranslator` 类的实例。以下是一个简单的示例：

```python
from text_translator import TextTranslator
import pandas as pd

# 创建文本翻译器实例
# src是需要翻译的文本语言，dest是翻译后的文本语言。（默认src是葡语，dest是汉语）
translator = TextTranslator(src='pt', dest='zh-cn')

# 定义需要翻译的文本
portuguese_samples = [
    "Como vai você?",
    "Eu gosto de viajar para Portugal.",
    "A cultura portuguesa é rica e diversificada."
]
# 转成Dataframe格式的数据，方便后续进行数据处理
data = {'Portuguese Sentences': portuguese_samples}
df = pd.DataFrame(data)

# 使用批处理进行翻译，并接受返回的数据
df['translated_result'] = translator.batch_translate(df['Portuguese Sentences'])


# 打印翻译结果
print(df)

# 当不知道语言对应的code时，可以调用detect_language方法进行查看
print(translator.detect_language("Como vai você?"))

```


## 翻译效果
```python
# 正常语句，翻译效果还可以

portuguese_samples = [
    "a verdadeira vida é assim. sem maquiagem",
    "esses vídeos deveriam ser proibido na plataforma",
    "a polícia demora muito a chegar me dar nervoso....ainda bem que salvaram ela"
]
data = {'Portuguese Sentences': portuguese_samples}
df = pd.DataFrame(data)

df['translated_result'] = translator.batch_translate(df['Portuguese Sentences'])

print(df)
```


```python
# 存在语法和拼写错误时，翻译效果不理想

"""
我只需要肉，因为调味料已经准备好了。
愿神保佑工作大家庭的工作，奉我们主耶稣基督的名，阿门
太好了，这就是生活！我现在要解决我的问题。
"""

portuguese_samples = [
    "só faltou a carne porque o tempeiro tá completo",
    "Só faltou a carne porque o tempero está completo.",
    "Deus abençoe o trabalho à família do trabalho em nome do nosso senhor Jesus Cristo amém",
    "Deus abençoe o trabalho e a família do trabalho em nome do nosso Senhor Jesus Cristo. Amém.",
    "top aí sim é vida já vou resolver meu problema",
    "Top, aí sim é vida. Já vou resolver meu problema."
]
data = {'Portuguese Sentences': portuguese_samples}
df = pd.DataFrame(data)

df['translated_result'] = translator.batch_translate(df['Portuguese Sentences'])

print(df)
```
