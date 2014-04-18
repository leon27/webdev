from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
import json

# Create your views here.

def sum(request):
    if request.method=='POST':
        rst={}
        raw_data=json.loads(request.body);
        id=raw_data['orderID']
        prds=raw_data['product_list']
        sum=0
        for prd in prds:
            sum+=prd['price']
        rst['orderID']=id
        rst['sum']=sum
        rspn=json.dumps(rst)
        return HttpResponse(rspn)
    
    
def index(request):
    return render_to_response('index.html')