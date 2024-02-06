
from rest_framework.response import Response

from rest_framework.decorators import api_view

from project.models import Theme, Word



@api_view(['GET'])
def words(request):
    data = []
        
    themes = Theme.objects.all()
    
    for th in themes:
        data.append({
            'id': th.id,
            'name': th.name,
            'words': [{
                'id': word.id,
                'korean': word.korean,
                'uzbek': word.uzbek,
            } for word in th.words.all()]
        })
        
    return Response(data)