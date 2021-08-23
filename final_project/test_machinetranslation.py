from machinetranslation import translator
import unittest

english_sentence = "How are you?"
french_sentence ="Comment es-tu?"

class RestfulTest(unittest.TestCase):
    def setUp(self):
        None
    def test_EnglishToFrench(self):
        assert translator.EnglishToFrench(english_sentence)==french_sentence, 'english to french failed!'

    def test_FrenchToEnglish(self):
        assert translator.FrenchToEnglish(french_sentence)==english_sentence, 'french to english failed'

if __name__=='__main__':
    unittest.main()
