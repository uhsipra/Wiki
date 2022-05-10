from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry_name):
    entry = util.get_entry(entry_name)

    if entry is None:
        return render(request, "encyclopedia/error.html", {
            "Error": "Page Not Found."
        })

    return render(request, "encyclopedia/entry.html", {
        "entry_name": entry_name,
        "entry": util.get_entry(entry_name)
    })