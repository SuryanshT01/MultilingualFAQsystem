from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from .serializers import FAQSerializer

@api_view(['GET'])
def get_faqs(request):
    lang = request.GET.get('lang', 'en')
    faqs = FAQ.objects.all()
    
    # Serialize data with translations
    data = []
    for faq in faqs:
        data.append({
             "question": faq.get_translated_question(lang),
            "answer": faq.answer
        })

    return Response(data)
