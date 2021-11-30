from datetime import datetime

from django.http import QueryDict


class ConvertDateMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        if request.method == 'POST':
            rent_date = request.POST.get('rent_date')
            if rent_date:
                rent_date = datetime.strptime(rent_date, '%b %d, %Y').strftime('%d.%m.%Y')
                update_dict = QueryDict.copy(request.POST)
                update_dict['rent_date'] = rent_date
                request.POST = update_dict
            response = self._get_response(request)
            return response
        else:
            response = self._get_response(request)
            return response
