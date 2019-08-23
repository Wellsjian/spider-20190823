import html
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from message.models import Message
from tools.login_check import login_check, get_user_by_request
from topic import models


@login_check('POST')
def topic_view(request, author_id):
    if request.method == "POST":

        json_str = request.body
        if not json_str:
            result = {'code': 302, 'error': 'Please give me data !!'}
            return JsonResponse(result)
        data = json.loads(json_str.decode())
        title = data.get('title')

        # 博 客 内 容 带 HTML 格式
        content = data.get('content')
        # 截取的30个字符字符
        content_text = data.get('content_text')
        limit = data.get('limit')
        category = data.get('category')
        if not title:
            result = {'code': 303, 'error': 'Please give me title !!'}
            return JsonResponse(result)
        ####csrf
        ####xss     cross  site  script  防止xss攻击
        ####sql注入
        title = html.escape(title)
        if not content:
            result = {'code': 304, 'error': 'Please give me content !!'}
            return JsonResponse(result)
        if not content_text:
            result = {'code': 305, 'error': 'Please give me content_text !!'}
            return JsonResponse(result)
        if not limit:
            result = {'code': 306, 'error': 'Please give me limit!!'}
            return JsonResponse(result)
        if not category:
            result = {'code': 307, 'error': 'Please give me category !!'}
            return JsonResponse(result)

        introduce = content_text[:30]
        if request.user.username != author_id:
            result = {'code': 308, 'error': 'Can not touch me !!'}
            return JsonResponse(result)
        try:
            models.Topic.objects.create(
                title=title,
                limit=limit,
                content=content,
                introduce=introduce,
                category=category,
                author_id=author_id
            )
        except Exception as e:
            print(e)
            result = {'code': 309, 'error': 'Databases is connected error !!'}
            return JsonResponse(result)
        result = {'code': 200, 'username': request.user.username}
        return JsonResponse(result)


    elif request.method == "GET":

        # vistor 访问者
        # author 作者
        # 查找作者
        authors = models.u_model.UserProfile.objects.filter(username=author_id)
        if not authors:
            request = {'code': 310, 'error': 'The author is not existed'}
            return JsonResponse(request)
        author = authors[0]
        # 查找访问者
        vistor = get_user_by_request(request)
        vistor_username = None
        if vistor:
            vistor_username = vistor.username
        # 获取t_id
        t_id = request.GET.get('t_id')
        if t_id:
            t_id = int(t_id)
            ##查询指定文章
            is_self = False
            if vistor_username != author.username:#author.username
                author_topics = models.Topic.objects.filter(id=t_id, limit='public')
                author_topic = author_topics[0]
                if not author_topic:
                    request = {'code': 312, 'error': 'The topic is not existed'}
                    return JsonResponse(request)
            else:
                is_self = True
                author_topics = models.Topic.objects.filter(id=t_id)
                author_topic = author_topics[0]
                if not author_topic:
                    result = {'code': 311, 'error': 'No Topic !!'}
                    return JsonResponse(result)
            result = make_topic_res1(author, author_topic, is_self)
            # print(result)
            return JsonResponse(result)
        ##查询全部文章
        else:
            # 判断是否有查询字符串[category]
            category = request.GET.get('category')
            if category in ['tec', 'no-tec']:
                if vistor_username == author.username:
                    author_topics = models.Topic.objects.filter(author_id=author.username, category=category)

                else:
                    author_topics = models.Topic.objects.filter(author_id=author.username, limit='public',
                                                                category=category)
            else:
                if vistor_username == author.username:
                    author_topics = models.Topic.objects.filter(author_id=author.username)
                else:
                    author_topics = models.Topic.objects.filter(author_id=author.username, limit='public')
            res = make_topics_res(author, author_topics)
            return JsonResponse(res)



    elif request.method == 'DELETE':
        users = get_user_by_request(request)
        if not users:
            result = {'code': 311, 'error': '未登录'}
            return JsonResponse(result)
        if users.username != author_id:
            result = {'code': 312, 'error': 'URL 中欲删除的用户和登陆用户不一致'}
            return JsonResponse(result)
        topic_id = request.GET.get('topic_id')
        if not topic_id:
            result = {'code': 313, 'error': 'Please give me the id'}
            return JsonResponse(result)
        author_topic = models.Topic.objects.filter(id=topic_id)
        if not author_topic:
            result = {'code': 314, 'error': '想删除的 topic 不存在'}
            return JsonResponse(result)
        author_topic.delete()
        result = {'code': 200}
        return JsonResponse(result)


def make_topics_res(author, author_topics):
    res = {'code': 200, 'data': {}}
    topics_res = []
    for topic in author_topics:
        d = {}
        d['id'] = topic.id
        d['title'] = topic.title
        d['category'] = topic.category
        d['created_time'] = topic.created_time.strftime("%Y-%m-%d %H:%M:%S")
        d['content'] = topic.content
        d['introduce'] = topic.introduce
        d['author'] = author.nickname
        topics_res.append(d)
    res['data']['topics'] = topics_res
    res['data']['nickname'] = author.nickname
    return res


def make_topic_res(author, author_topic, is_self):
    if is_self:
        ##博主访问自己的博客
        ###取出id 大于 当前访问id 的下一个
        next_topic = models.Topic.objects.filter(id__gt=author_topic.id, author=author).first()
        ###取出id 大于 当前访问id 的上一个
        last_topic = models.Topic.objects.filter(id__lt=author_topic.id, author=author).last()
    else:
        ###取出id 大于 当前访问id 的下一个
        next_topic = models.Topic.objects.filter(id__gt=author_topic.id, author=author, limit='public').first()
        ###取出id 大于 当前访问id 的上一个
        last_topic = models.Topic.objects.filter(id__lt=author_topic.id, author=author, limit='public').last()
    ##生成下一个文章的id   he   title
    if next_topic:
        next_id = next_topic.id
        next_title = next_topic.title
    else:
        next_id = None
        next_title = None
    ##生成上一个文章的id   he   title
    if last_topic:
        last_id = last_topic.id
        last_title = last_topic.title
    else:
        last_id = None
        last_title = None

    res = {'code': 200, 'data': {}}
    res['data']['nickname'] = author.nickname
    res['data']['title'] = author_topic.title
    res['data']['category'] = author_topic.category
    res['data']['created_time'] = author_topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
    res['data']['content'] = author_topic.content
    res['data']['introduce'] = author_topic.introduce
    res['data']['author'] = author.nickname
    res['data']['next_id'] = next_id
    res['data']['next_title'] = next_title
    res['data']['last_id'] = last_id
    res['data']['last_title'] = last_title

    all_messages = Message.objects.filter(topic=author_topic).order_by('-created_time')
    #####留言字典
    # d1 = {}
    dict01 = {}

    ######回复字典
    # d2 = {}r
    list01 = []

    m_count = 0
    for message in all_messages:
        m_count += 1
        if message.parent_message:
            if message.parent_message in dict01:
                dict01[message.parent_message].append({
                    'msg_id': message.id,
                    'content': message.content,
                    'publisher': message.publisher.nickname,
                    'publisher_avatar': str(message.publisher.avatar),
                    'created_time':message.created_time.strftime('%Y-%m-%d %H:%M:%S')
                })
            else:
                dict01[message.parent_message] = []
                dict01[message.parent_message].append({
                    'msg_id': message.id,
                    'content': message.content,
                    'publisher': message.publisher.nickname,
                    'publisher_avatar': str(message.publisher.avatar),
                    'created_time':message.created_time.strftime('%Y-%m-%d %H:%M:%S')
                })
        else:
            list01.append({
                'id': message.id,
                'content': message.content,
                'publisher': message.publisher.nickname,
                'publisher_avatar': str(message.publisher.avatar),
                'created_time':message.created_time.strftime('%Y-%m-%d %H:%M:%S'),
                'reply':[]})
            # print(list01)

    #$关联  回复  和  留言
    #dict  [{留言的信息，reply：[]}]
    for m in list01:
        if m['id'] in dict01:
            m['reply'] = dict01[m['id']]

    res['data']['messages'] = list01
    res['data']['messages_count'] = m_count
    return res


def make_topic_res1(author, author_topic, is_self):
  '''
  生成 topic 详情 数据
  :param author:
  :param author_topic:
  :param is_self:
  :return:
  '''
  if is_self:
    #博主访问自己的博客
    # 1 , 2 , 4, 5, 6, 8, 20
    # 取出ID大于当前博客ID的数据的第一个 -> 当前文章的下一篇
    next_topic = models.Topic.objects.filter(id__gt=author_topic.id, author=author).first()
    # 取出ID小于当前博客ID的数据的最后一个 -> 当前文章的上一篇
    last_topic = models.Topic.objects.filter(id__lt=author_topic.id, author=author).last()
  else:
    # 访客(陌生人)访问当前博客
    next_topic = models.Topic.objects.filter(id__gt=author_topic.id, author=author,limit='public').first()
    last_topic = models.Topic.objects.filter(id__lt=author_topic.id, author=author,limit='public').last()
  #生成下一个文章的id 和 title
  if next_topic:
    next_id = next_topic.id
    next_title = next_topic.title
  else:
    next_id = None
    next_title = None
  #生成上一个文章的id 和 title
  if last_topic:
    last_id = last_topic.id
    last_title = last_topic.title
  else:
    last_id = None
    last_title = None

  result = {'code': 200, 'data': {}}
  result['data']['nickname'] = author.nickname
  result['data']['title'] = author_topic.title
  result['data']['category'] = author_topic.category
  result['data']['created_time'] = author_topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
  result['data']['content'] = author_topic.content
  result['data']['introduce'] = author_topic.introduce
  result['data']['author'] = author.nickname
  result['data']['next_id'] = next_id
  result['data']['next_title'] = next_title
  result['data']['last_id'] = last_id
  result['data']['last_title'] = last_title
  #留言&回复数据
  #获取所有messages
  all_messages = Message.objects.filter(topic=author_topic).order_by('-created_time')
  #拼接返回
  msg_dict = {}
  msg_list = []

  m_count = 0
  for msg in all_messages:
    m_count += 1
    if msg.parent_message:
      #回复
      if msg.parent_message in msg_dict:
        msg_dict[msg.parent_message].append({'msg_id':msg.id, 'publisher':msg.publisher.nickname,'publisher_avatar':str(msg.publisher.avatar),'content':msg.content, 'created_time': msg.created_time.strftime('%Y-%m-%d %H:%M:%S')})
      else:
        msg_dict[msg.parent_message] = []
        msg_dict[msg.parent_message].append(
          {'msg_id': msg.id, 'publisher': msg.publisher.nickname, 'publisher_avatar': str(msg.publisher.avatar),
           'content': msg.content, 'created_time': msg.created_time.strftime('%Y-%m-%d %H:%M:%S')})
    else:
      #留言
      msg_list.append({'id':msg.id, 'content':msg.content,'publisher':msg.publisher.nickname,'publisher_avatar':str(msg.publisher.avatar),'created_time': msg.created_time.strftime('%Y-%m-%d %H:%M:%S'),'reply':[]})

  #关联 留言和对应的回复
  #msg_list - >[{留言相关的信息, 'reply':[]}, ]
  for m in msg_list:
    if m['id'] in msg_dict:
      #证明当前的留言有回复信息
      m['reply'] = msg_dict[m['id']]

  result['data']['messages'] = msg_list
  result['data']['messages_count'] = m_count

  return result

