from django.shortcuts import get_object_or_404, render
from .models import Artist, Album, song, user

# Create your views here.
def artist_list(request):
    artists = Artist.objects.all()
    context = {
        'artists': artists
    }
    return render(request, 'spotify/artist_list.html', context)