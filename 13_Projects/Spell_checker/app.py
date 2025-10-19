# step-1 importing the required library
from spellchecker import SpellChecker

# step-2 creating the app class
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()
    
    def correct_text(self, text):
        words = text.split()
        corrected_words = []

