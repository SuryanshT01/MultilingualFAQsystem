from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    
    # Translations
    question_hi = models.TextField(null=True, blank=True)  # Hindi
    question_bn = models.TextField(null=True, blank=True)  # Bengali
    
    def save(self, *args, **kwargs):
        """Auto-translate and save translations"""
        translator = Translator()
        
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text

        cache.set(f'faq_{self.id}', self, timeout=86400)  # Cache for 1 day
        super().save(*args, **kwargs)

    def get_translated_question(self, lang):  # Fixed function name
        """Fetch translated question based on language"""
        return getattr(self, f'question_{lang}', self.question)

    def __str__(self):
        return self.question
