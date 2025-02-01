# FAQ System 📖
A Django-based multilingual FAQ system with WYSIWYG editor, caching, and REST API.

## Features 🚀
- 📄 Rich-text FAQ management (WYSIWYG editor)
- 🌍 Multi-language support (Auto-translate)
- 🚀 Fast API with Redis caching
- 🧪 Unit testing with pytest
- 🐳 Dockerized setup

## Installation ⚙️
```sh
git clone https://github.com/SuryanshT01/MultilingualFAQsystem
cd faq_system
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Fetch FAQs in English
curl http://127.0.0.1:8000/api/faqs/

# Fetch FAQs in Hindi
curl http://127.0.0.1:8000/api/faqs/?lang=hi

#Run test 
pytest

