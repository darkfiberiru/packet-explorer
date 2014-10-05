from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponse
from django.shortcuts import redirect
from models import Question, Pool
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
    <td><a href="question?category={{ category_1 }}&difficulty=100">100</a></td>
    <td><a href="question?category={{ category_2 }}&difficulty=100">100</a></td>
    <td><a href="question?category={{ category_3 }}&difficulty=100">100</a></td>
  </tr>
  <tr>
    <td><a href="question?category={{ category_1 }}&difficulty=200">300</a></td>
    <td><a href="question?category={{ category_2 }}&difficulty=200">300</a></td>
    <td><a href="question?category={{ category_3 }}&difficulty=200">300</a></td>
  </tr>
  <tr>
    <td><a href="question?category={{ category_1 }}&difficulty=300">300</a></td>
    <td><a href="question?category={{ category_2 }}&difficulty=300">300</a></td>
    <td><a href="question?category={{ category_3 }}&difficulty=300">300</a></td>
  </tr>
</table> 
</body></html> """
question_template = ""









def home(request):
  t = Template(game_template)
  c = Context({'category_1': 'smtp' , 'category_2': 'sip', 'category_3' : 'irc', 'score' : '0 you suck'})    
  return HttpResponse(t.render(c))

def populate_db(request)
  

 return HttpResponse('done')

