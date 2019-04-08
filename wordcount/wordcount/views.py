from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist= fulltext.split()

    word_dictonary = {}

    for word in wordlist:
        if word in word_dictonary:
            #increase
            word_dictonary[word] += 1
        else:
            #add to the dictonary
            word_dictonary[word] = 1


    sorted(word_dictonary.items(), key= operator.itemgetter(1), reverse= True)
    return render(request, 'count.html',{'fulltext': fulltext,'count': len(wordlist),
                                         'sortedwords': word_dictonary.items()})
