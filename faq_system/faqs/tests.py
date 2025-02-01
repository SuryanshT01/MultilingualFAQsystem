from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python web framework.",
            question_hi="Django क्या है?",
            question_bn="Django কি?",
        )

    def test_faq_creation(self):
        self.assertEqual(self.faq.question, "What is Django?")
        self.assertEqual(self.faq.answer, "Django is a Python web framework.")

    def test_translation_method(self):
        # Change `get_translation` to `get_translated_question`
        self.assertEqual(self.faq.get_translated_question("hi"), "Django क्या है?")
        self.assertEqual(self.faq.get_translated_question("bn"), "Django কি?")
        self.assertEqual(self.faq.get_translated_question("en"), "What is Django?")
