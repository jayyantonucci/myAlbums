import database

menu = """Please select one of the following options:
1) Add new artist.
2) Artist list.
3) Add new album.
4) View albums.
0) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_tables()


def prompt_add_artist():
    artist_name = input("Artist name: ")
    database.add_artist(artist_name)


def prompt_add_album():
    album_name = input("Album name: ")
    artist_id = input("Artist id: ")
    database.add_album(album_name, artist_id)


def print_artist_list(artists):
    print("--artist list--")
    for artist in artists:
        print(f"id: {artist[0]} | {artist[1]}")
    print("---- \n")


def print_album_list(albums):
    print("--album list--")
    for album in albums:
        # add  artist name to print statement
        print(f"id: {album[0]}, {album[1]}")
    print("---- \n")


while (user_input := input(menu)) != "0":
    if user_input == "1":
        prompt_add_artist()
    elif user_input == "2":
        artists = database.get_artsits()
        print_artist_list(artists)
    elif user_input == "3":
        prompt_add_album()
    elif user_input == "4":
        albums = database.get_albums()
        print_album_list(albums)
    else:
        print("Invalid input, please try again!")
