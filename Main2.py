from googletrans import Translator

translator = Translator()

out = translator.translate("नमस्ते, पिचर्म", dest="en")

print(out.text)