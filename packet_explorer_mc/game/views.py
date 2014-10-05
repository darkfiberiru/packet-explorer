from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponse
from django.shortcuts import redirect
from models import Question, Pool,Category,Difficulty
from pprint import pprint,pformat
import json

game_template = """<html><body>
 
<h1 style="text-align:center"> {{ score }}
</h1>

<table border="2" style="width:80%">
  <tr>
    <td>{{ category_1  }}</td>
    <td>{{ category_2  }}</td>
    <td>{{ category_3  }}</td>
  </tr>
  <tr>
    <td><a href="question?category={{ category_1 }}&difficulty=={{level_1}}">{{level_1}}</a></td>
    <td><a href="question?category={{ category_2 }}&difficulty=={{level_1}}">{{level_1}}</a></td>
    <td><a href="question?category={{ category_3 }}&difficulty=={{level_1}}">{{level_1}}</a></td>
  </tr>
  <tr>
    <td><a href="question?category={{ category_1 }}&difficulty=={{level_1}}">{{level_2}}</a></td>
    <td><a href="question?category={{ category_2 }}&difficulty=={{level_1}}">{{level_2}}</a></td>
    <td><a href="question?category={{ category_2 }}&difficulty=={{level_1}}">{{level_2}}</a></td>
  </tr>
  <tr>
    <td><a href="question?category={{ category_2 }}&difficulty=={{level_1}}">{{level_3}}</a></td>
    <td><a href="question?category={{ category_2 }}&difficulty=={{level_1}}">{{level_3}}</a></td>
    <td><a href="question?category={{ category_2 }}&difficulty=={{level_1}}">{{level_3}}</a></td>
  </tr>
</table> 
</body></html> """
question_template = """<html><body> {{ question }}   





</body></html>"""









def home(request):
  t = Template(game_template)
  cat1 = Category.objects.all()[0].name
  cat2 = Category.objects.all()[1].name
  cat3 = Category.objects.all()[2].name
  levels = list()
  for obj in Difficulty.objects.all():
    levels.append(obj.points) 
  levels.sort()
  c = Context({'category_1': cat1  , 'category_2': cat2, 'category_3' : cat3 , 'level_1' : levels[0], 'level_2' : levels[1] , 'level_3' : levels[2], 'score' : '0 you suck'})    

  return HttpResponse(t.render(c))

def populate_db(request):
  if Category.objects.count() == 0:
     c = Category(name="smtp",adjustment=1)
     c.save()
     c = Category(name="sip",adjustment=1)
     c.save()
     c = Category(name="irc",adjustment=1)
     c.save()
  if Difficulty.objects.count() == 0:
     d = Difficulty(points=100) 
     d.save()
     d = Difficulty(points=300) 
     d.save()
     d = Difficulty(points=200) 
     d.save()
  categories = Category.objects.all()
  difficulties = Difficulty.objects.all()
  return HttpResponse('done')

def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
 
def populate_questions(request):
#  pass
#  return HttpResponse('done')
  wipe = request.GET.get('wipe')
  if wipe != None:
    Question.objects.all().delete()
    return HttpResponse("Wiped")
  if Question.objects.count() == 0:
    error=list()
    with open('game/questions.json') as f:
      for question in json.loads(f.read()):
        question = convert(question)
        error.append(question['answer_text'])
        difficulty1 = Difficulty.objects.get(points = int(question['difficulty'])) 
        error.append(difficulty1.points)
        category1 = Category.objects.get(name = question['category']) 
        q = Question(difficulty=difficulty1, answer_text=question['answer_text'], question_text=question['question_text'], category=category1, pcap=question['pcap'])
        q.save()
      return HttpResponse(pformat(error))
  else:
    return HttpResponse("Questions already built")
def random_record(records):
  return records[random.randint(0,records.count()-1)

def question(request):
  if not  request.user.is_authenticated():  
    return  HttpResponseRedirect('/')
  user = request.user 
  difficulty = request.GET.get('difficulty')
  category  = request.GET.get('category')
  if Pool.objects.filter(user=user).count() != 9:
    Pool.objects.filter(user=user).delete()
    for x in Category.objects:
       for y in Difficulty.objects():
    return HttpResponse('blba')

  return HttpResponse(pformat(user.username))
