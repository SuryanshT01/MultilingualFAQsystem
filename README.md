# FAQ System 📖

A Django-based multilingual FAQ system with WYSIWYG editor, caching, REST API, and automated translation support.

## Features 🚀
- 📄 **Rich-text FAQ management** using WYSIWYG editor (django-ckeditor)
- 🌍 **Multi-language support** with auto-translation using Google Translate API
- ⚡ **Fast API** with Redis caching for optimized performance
- 🔍 **Efficient data retrieval** with language-based pre-translation
- 🏛 **Admin Panel** for easy FAQ management
- 🧪 **Unit testing** with pytest for model and API validation
- 🐳 **Dockerized setup** for easy deployment

## Table of Contents 📌
1. [Installation](#installation)
2. [API Usage](#api-usage)
3. [Model Design](#model-design)
4. [WYSIWYG Editor Integration](#wysiwyg-editor-integration)
5. [Caching Mechanism](#caching-mechanism)
6. [Testing](#testing)
7. [Code Quality](#code-quality)
8. [Deployment](#deployment)
9. [Contribution Guidelines](#contribution-guidelines)

---

## Installation ⚙️

### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Django (>=4.0)
- Redis (for caching)
- Docker (optional, for containerized setup)

### Steps
```sh
git clone https://github.com/SuryanshT01/MultilingualFAQsystem
cd faq_system
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # Create an admin user
python manage.py runserver
```

### Running with Docker 🐳
```sh
docker-compose up --build
```

---

## API Usage 📡

### Fetch FAQs in Default Language (English)
```sh
curl http://127.0.0.1:8000/api/faqs/
```

### Fetch FAQs in Hindi
```sh
curl http://127.0.0.1:8000/api/faqs/?lang=hi
```

### Fetch FAQs in Bengali
```sh
curl http://127.0.0.1:8000/api/faqs/?lang=bn
```

---

## Model Design 🏗️
The FAQ model is designed to store frequently asked questions in multiple languages.

### **FAQ Model**
```python
from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)

    def get_translated_question(self, lang):
        translations = {'hi': self.question_hi, 'bn': self.question_bn}
        return translations.get(lang, self.question)
```

---

## WYSIWYG Editor Integration ✍️
To enable rich-text formatting in the FAQ answer field, we use **django-ckeditor**.

### Installation
```sh
pip install django-ckeditor
```

### Configuration
In `settings.py`, add:
```python
INSTALLED_APPS = [
    'ckeditor',
    'faq',
]
```

---

## Caching Mechanism 🗄️
To improve performance, we use Redis to cache FAQ translations.

### Install Redis
```sh
sudo apt install redis-server
```

### Configure Django Caching
In `settings.py`:
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

---

## Testing 🧪
This project includes unit tests to ensure API correctness and caching efficiency.

### Run Tests
```sh
pytest
```

### Example Test Case
```python
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
```

---

## Code Quality 🧹
### PEP8 Linting
```sh
pip install flake8
flake8 .
```

---

## Deployment 🚀
### Deploy to Heroku
```sh
heroku login
heroku create faq-system
heroku config:set DJANGO_SETTINGS_MODULE=faq.settings
heroku addons:add heroku-redis:hobby-dev
heroku container:push web -a faq-system
heroku container:release web -a faq-system
```

---

## Contribution Guidelines 🤝
We welcome contributions! Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "feat: Add new API endpoint"`)
4. Push to your branch (`git push origin feature-name`)
5. Create a Pull Request

Follow **conventional commit messages**:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation updates

---

## License 📜
This project is licensed under the MIT License.

---


