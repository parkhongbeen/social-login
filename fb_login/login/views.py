import requests
from django.http import HttpResponse
from django.shortcuts import render

app_id = 247987559730617
app_secret = 'c7731b561ca0d70442fd3262fca2c56c'


def index(request):
    context = {
        "app_id": app_id,
    }
    return render(request, 'login.html', context)


def login(request):
    # 인증 후 GET 요청으로 리다이렉트 되어서 온 주소에 포함된 'code' 를 가져온다.
    code = request.GET['code']
    # 처음 입력한 리다이렉트 주소와 동일한 주소를 입력한다.
    # 아래는 동적으로 동일한 주소를 다시 구성하도록 한 것이다.
    # request.scheme: 현재 페이지에 전달된 요청의 유형 정보이다. 지금의 경우 'http'
    # request.META['HTTP_HOST']: 호스트 URI 주소 정보이다. 지금의 경우 'localhost:8000'
    # revers('login'): login 이라는 URL 명에 연결되어 있는 실제 URL을 가져온다. 지금의 경우 '/fb-login/'
    redirect_uri = f"{'http'}://{'localhost:8000'}{'/fb-login/'}"
    # access_token을 받기위해 요청을 보내야하는 URL
    url_access_token = "https://graph.facebook.com/v2.11/oauth/access_token"
    # access_token을 받기위해 보내야하는 매개변수들
    params_access_token = {
        "client_id": app_id,
        "redirect_uri": redirect_uri,
        "client_secret": app_secret,
        "code": code,
    }
    # requests 패키지를 사용해서 URL에 매개변수들을 추가하여 GET 요청을 보낸다.
    # pip install requests 로 설치
    response = requests.get(url_access_token, params=params_access_token)
    # 돌려받은 응답을 JSON 형식으로 변환한다.
    result = response.json()
    # JSON 형식을 화면에 띄워준다.
    return HttpResponse(result.items())
