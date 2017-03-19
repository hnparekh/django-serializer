import os, sys
from django_pandas.io import read_frame
import pandas
import json

from django.http import HttpResponseRedirect
from django.shortcuts import render
reload(sys)
sys.setdefaultencoding('utf8')

def first(request):
	if request:
		return render(request, "index.html")

def test(request):
	sort_by = "caseId"
	if sort_by:
		print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
		print sort_by
	cwd = os.path.join(os.getcwd(),"jsonfile.txt")
	readdata = open(cwd, 'r')
	datas = json.load(readdata)
	# data = pandas.read_json("/appletast/jsonfile.json")
	datas = datas[0]
	data = datas["data"]
	key = list(data[0].keys())
	fields = []
	for d in data:
		print d.values()
		fields.append(list(d.values()))
	# fo = open(os.path.join(os.getcwd(),"result.csv"))
	df = pandas.DataFrame(data = fields, columns = key)
	# df.sort(columns = sort_by)
	df.to_csv(os.path.join(os.getcwd(),"result.csv"))
	context = {
		"keys": key,
		"rows" : df.sort(columns = sort_by).to_html() 
	}
	# print context
	# return render(request, "welcome.html", context)
	return render(request, "welcome.html", context)
