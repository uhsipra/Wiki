#from django import forms
from django.shortcuts import render

from . import util

# Not sure how to make django form always show in layout.html so I did not use it.
#class SearchForm(forms.Form):
#    q = forms.CharField(label="Search Encyclopedia", widget=forms.TextInput(attrs={'class':'search'}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry_name):
    entry = util.get_entry(entry_name)
    entry_names = util.list_entries()

    if entry_name in entry_names:
        return render(request, "encyclopedia/entry.html", {
            "entry_name": entry_name,
            "entry": entry
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "Error": "Page Not Found."
        })

def search(request):
    if request.method == "POST":
        entry_names = util.list_entries()
        q = request.POST['q']
        
        matching_subtring = []
        for entry in entry_names:
            if str(q).lower() == str(entry).lower():
                return render(request, "encyclopedia/entry.html", {
                    "entry_name": q,
                    "entry": util.get_entry(q)
                })
            elif str(q).lower() in str(entry).lower():
                matching_subtring.append(entry)
        
        if len(matching_subtring) == 0:
            return render(request, "encyclopedia/search.html", {
                "query": q,
                "Error": "No matching or similar results."
            })
        else:
            return render(request, "encyclopedia/search.html", {
                "query": q,
                "entries": matching_subtring
            })


