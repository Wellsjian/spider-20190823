import json

from django.http import JsonResponse

from user.models import UserProfile
from topic.models import Topic
from tools.login_check import get_user_by_request, login_check
from django.shortcuts import render
from . import models

# Create your views here.

@login_check('POST')
def mesages(request, topic_id):
    # post请求
    #http://127.0.0.1:8000/messages/topic_id
    #请求格式{'content':'aaa', 'parent_id':1}'parent_id'存在 则表示回复 否则为留言
    #响应格式 {'code':200}
    #注意   POST请求需要检查token
    if request.method == "POST":
        user = request.user
        json_str = request.body
        if not json_str:
            result = {'code':402, 'error':'Please give me json'}
            return JsonResponse(result)
        data = json.loads(json_str)
        parent_message = data.get('parent_id', 0)
        content = data.get('content')
        if not content:
            result = {'code':403, 'error':'Please give me content'}
            return JsonResponse(result)
        topics = Topic.objects.filter(id=topic_id)
        if not topics:
            result = {'code':404, 'error':'Please give me topic'}
            return JsonResponse(result)
        print(topics[0].author,topics[0].title)

        # publisher = UserProfile.objects.filter(id=user_id)

        models.Message.objects.create(
            content=content,
            publisher=user,
            topic=topics[0],
            parent_message=parent_message
        )

        result = {'code': 200}
        return JsonResponse(result)





