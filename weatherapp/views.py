from django.shortcuts import render
import json
import urllib.request as ul


# Create your views here.
def samp(request):
    return render(request, 'sample.html')


# wrapped the post data in a try except to catch the url error incase user inputs an invalid location 
def index(request):
    if request.method == 'POST':
        location = request.POST['city']
        try:
            address = 'http://api.openweathermap.org/data/2.5/weather?q='+location+'&appid=#add your open weather api access id #'
            res = ul.urlopen(address).read()
            json_data = json.loads(res)
            data = { 'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon'])[0:4] + ', ' + str(json_data['coord']['lat'])[0:4],
            'temperature': str(json_data['main']['temp'] -273)[:5],
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
            'state':location
        }
        except :  # this is bad practice .. the error to be caught is a URLError see how to catch this specific error
                  # as using except generally catches all types of errors 
           
            data = {'state':location }
            return render(request, 'index.html', data)


    # handles a case where the request.method is a GET request
    else:
        location = ''
        data = {}
        
    return render(request, 'index.html', data)

