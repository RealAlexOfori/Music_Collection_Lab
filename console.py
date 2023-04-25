import pdb 
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository 

artist_repository.delete_all()
album_repository.delete_all()

artist1 = Artist("Alex Ofori")
artist_repository.save(artist1)

artist2 = Artist("Bob Marley")
artist_repository.save(artist2)

artist3 = Artist("Kanye West")
artist_repository.save(artist3)

album1 = Album("The Testament","Gospel",artist1)
album_repository.save(album1)

album2 = Album("Bob Marley And The Wailers", "Reggae", artist2)
album_repository.save(album2)

album3 = Album("Graduation","Hip Hop", artist3)
album_repository.save(album3)

artist_repository.select_all()

for album in album_repository.select_all():
    print(album.__dict__)



pdb.set_trace()


