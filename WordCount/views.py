from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html',{'projectName':'WordCount'})

def count(request):
    fulltext = request.GET['fulltext']
    wordCount = fulltext.split()
    wordDictionary = {}
    for word in wordCount:
        if word in wordDictionary:
            #increase
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1
            #add to the dictionary
        sortedWords = sorted(wordDictionary.items(),key = operator.itemgetter(1), reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordCount),'wordSorted':sortedWords})

def about(request):
    return render(request,'about.html')