from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponse
from django.shortcuts import redirect
from models import Question, Pool,Category,Difficulty
from pprint import pprint
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
question_template = ""









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

import json
from pprint import pprint
 
def populate_questions(request):
  if Question.objects.count() == 0:
    with open('game/questions.json') as f:
      for question in json.loads(f.read())
        difficulty = Difficulty.objects.get(points=int(question['difficulty'])[0] 
        category = Category.objects.get(name=question['category'])[0] 

        category =
      return HttpResponse(json.loads(f.read())[0]['question_text'])



