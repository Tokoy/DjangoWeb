# -*- coding: utf-8 -*-
from django.shortcuts import render
from djng.views.crud import NgCRUDView
from django.http import HttpResponse
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import routers, serializers, viewsets
from models import Person,Article
from HelloDjango.serializers import ArticleSerializer,UserSerializer

# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def index(request, format=None):
    return render(request, 'index.html')

def User_list(request, format=None):
    if request.method == "GET":
        Email = request.GET['email']
        Password = request.GET['password']
        # data = JSONParser().parse(request)
        findUser=Person.objects.get(email=Email,password=Password)
        # serializer = UserSerializer(findUser)
        if findUser is not None:
            return HttpResponse(findUser)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
    # return render(request, 'index.html')

def Contents_list(request,format=None):
        html = '''<div class="herald box aside reviews" data-topics="article112704 reviews novels">
    <div class="category-line reviews"></div>
    <div class="thumbnail" style="background-image: url(/thumbnails/cover400x200/encyc/A19213-2600108680.1487776406.jpg); background-position: 52.000% 1.970%;">
      <div class="overlay">
        <div class="category reviews">
          review
        </div>
        <div class="comments"><a href="/cms/discuss/112704">14 comments</a></div>
      </div>

      <a href="/review/my-big-sister-lives-in-a-fantasy-world/novel-1/.112704" data-track="id=39363&amp;from=HP.A"></a>
    </div>
    <div class="wrap">
      <div>
        <h3>
          <a href="/review/my-big-sister-lives-in-a-fantasy-world/novel-1/.112704" data-track="id=39363&amp;from=HP.A">My Big Sister Lives in a Fantasy World Novel 1</a>
        </h3>
        <div class="byline">
          <time datetime="2017-02-26T15:00:00Z">
            Feb 26, 23:00
          </time>
          <div class="comments"><a href="/cms/discuss/112704">14 comments</a></div>
          <span class="topics">
            <span class="novels">novels</span>
          </span>
        </div>
        <div class="preview">
          <span class="intro">This wide-ranging parody of <em>chuunibyou</em> tropes pushes the envelope in some eyebrow-raising ways, but it's still bound to offer otaku fans a fun read.</span>
          <span class="full">― Whether you have a weird sibling or are the weird sibling, families often have dynamics that can feel odd to an outside perspective. In the case of Yuichi Sakaki's family in My Big Sister Lives in a Fantasy World, his older sister Mutsuko suffers from ...</span>
        </div>
      </div>
    </div>
  </div>
  <div class="herald box aside reviews" data-topics="article112268 reviews manga">
    <div class="category-line reviews"></div>
    <div class="thumbnail" style="background-image: url(/thumbnails/cover400x200/cms/review/112268/91dlwbx72wl.jpg); background-position: 43.357% 7.669%;">
      <div class="overlay">
        <div class="category reviews">
          review
        </div>
        <div class="comments"><a href="/cms/discuss/112268">5 comments</a></div>
      </div>

      <a href="/review/the-ancient-magus-bride/gn-5/.112268" data-track="id=39333&amp;from=HP.A"></a>
    </div>
    <div class="wrap">
      <div>
        <h3>
          <a href="/review/the-ancient-magus-bride/gn-5/.112268" data-track="id=39333&amp;from=HP.A">The Ancient Magus' Bride GN 5</a>
        </h3>
        <div class="byline">
          <time datetime="2017-02-25T15:00:00Z">
            Feb 25, 23:00
          </time>
          <div class="comments"><a href="/cms/discuss/112268">5 comments</a></div>
          <span class="topics">
            <span class="manga">manga</span>
          </span>
        </div>
        <div class="preview">
          <span class="intro">Both the visual ambition and depth of story in the Ancient Magus's Bride take a leap forward in this memorable volume.</span>
          <span class="full">― The Ancient Magus' Bride's recent volumes have been reasonably focused affairs, prioritizing Chise and Elias' collective character development over the whimsical vignettes of the manga's early chapters. This fifth volume marks a return to episodic storytelling, as the leannan sidhe...</span>
        </div>
      </div>
    </div>
  </div>'''
        # fullcontents = trs[i].contents[5].contents[1].contents[5].contents[3].text //有些没有内容，所以不能预览
        # img = re.findall(ur"(?<=[\(（])[^\)）]+(?=[\)）])", trs[i].contents[3].attrs['style'])
        htmlurl = open('netnews.html').read()
        soup = BeautifulSoup(html, "html.parser")
        trs = soup.findAll('div', {'class': "herald"})
        length = len(trs)
        jsondatas = []
        arr = {}
        for i in range(length):
            title = trs[i].h3.text
            datetime = trs[i].time.text
            intro = trs[i].findAll('span', {'class': "intro"})[0].text
            img = trs[i].findAll('div', {'class': "thumbnail"})[0].attrs['style']
            tag = trs[i].findAll('span', {'class': "topics"})[0].text
            commnets=trs[i].findAll('div', {'class': "comments"})[0].text
            arr = {'Title': title, 'Img': img, 'Intro': intro, 'Tag': tag, 'Time': datetime,'Comments':commnets}
            jsondatas.append(arr)
        return JsonResponse(jsondatas,safe=False)

