from googletrans import Translator

translator = Translator()
result = translator.detect('Good')
print("Detected language:", result.lang)
