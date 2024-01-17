import os
from pytube import YouTube, Playlist
from pytube.cli import on_progress
from tqdm import tqdm  # Bibliothèque pour la barre de progression


# Fonction pour obtenir les détails d'une vidéo YouTube à partir de son URL
def get_video_details(url):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        return yt
    except Exception as e:
        print("Erreur lors de la récupération des détails de la vidéo :", e)
        return None


def print_video_details(yt):
    if yt is not None:
        print("\nDétails de la vidéo :")
        print("Titre :", yt.title)
        print("Nombre de vues :", yt.views)
        print("Durée :", yt.length, "secondes")
        print("Note moyenne :", yt.rating)


def download_video(yt, quality, only_audio):
    if yt is not None:
        try:
            print("\nTéléchargement en cours...")
            if only_audio:
                ys = yt.streams.get_audio_only()
            else:
                if quality == 'high':
                    ys = yt.streams.get_highest_resolution()
                else:
                    ys = yt.streams.get_lowest_resolution()

            output_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'Youtube download', 'data')

            # Utilisation de tqdm pour la barre de progression
            with tqdm(total=ys.filesize, unit='bytes', unit_scale=True, desc=ys.title) as progress_bar:
                def progress_callback(chunk, _):
                    progress_bar.update(len(chunk))

                ys.download(output_path=output_path, on_progress=progress_callback)

            print("\nTéléchargement terminé !")
        except Exception as e:
            print("Erreur lors du téléchargement de la vidéo :", e)



import os
from pytube import YouTube, Playlist
from pytube.cli import on_progress
from tqdm import tqdm

# Fonction pour obtenir les détails d'une vidéo YouTube à partir de son URL
def get_video_details(url):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        return yt
    except Exception as e:
        print("Erreur lors de la récupération des détails de la vidéo :", e)
        return None

# Fonction pour afficher les détails d'une vidéo YouTube
def print_video_details(yt):
    if yt is not None:
        print("\nDétails de la vidéo :")
        print("Titre :", yt.title)
        print("Nombre de vues :", yt.views)
        print("Durée :", yt.length, "secondes")
        print("Note moyenne :", yt.rating)

# Fonction pour télécharger une vidéo YouTube avec une barre de progression
# Fonction pour télécharger une vidéo YouTube avec une barre de progression
def download_video(yt, quality, only_audio):
    if yt is not None:
        try:
            print("\nTéléchargement en cours...")
            if only_audio:
                ys = yt.streams.get_audio_only()
            else:
                if quality == 'high':
                    ys = yt.streams.get_highest_resolution()
                else:
                    ys = yt.streams.get_lowest_resolution()

            output_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'Youtube download', 'data')

            # Vérification de l'âge pour les vidéos restreintes
            if ys.age_restricted:
                print("Cette vidéo est restreinte par âge. Vous devez vous connecter pour la télécharger.")
                if not authenticate():
                    print("Échec de l'authentification. Impossible de télécharger la vidéo.")
                    return

            # Utilisation de tqdm pour la barre de progression
            with tqdm(total=ys.filesize, unit='bytes', unit_scale=True, desc=ys.title) as progress_bar:
                def progress_callback(chunk, _):
                    progress_bar.update(len(chunk))

                ys.download(output_path=output_path, on_progress=progress_callback)

            print("\nTéléchargement terminé !")
        except Exception as e:
            print("Erreur lors du téléchargement de la vidéo :", e)


def authenticate():
    print("\nPour télécharger des vidéos restreintes par âge, veuillez vous connecter.")
    username = input("Nom d'utilisateur YouTube : ")
    password = input("Mot de passe YouTube : ")

    try:
        # Tentative de connexion avec les informations fournies
        YouTube(username, password)
        print("Authentification réussie.")
        return True
    except Exception as e:
        print("Échec de l'authentification :", e)
        return False



def download_playlist(url, quality, only_audio):
    try:
        playlist = Playlist(url)
        for video in playlist.videos:
            download_video(video, quality, only_audio)
    except Exception as e:
        print("Erreur lors du téléchargement de la playlist :", e)


def read_urls_from_file(filename):
    try:
        with open(filename, 'r') as file:
            urls = file.readlines()
        return urls
    except Exception as e:
        print("Erreur lors de la lecture du fichier :", e)
        return []


def display_help():
    print("\nMenu d'aide :")
    print("Entrez '1' pour entrer une URL de vidéo YouTube.")
    print("Entrez '2' pour lire les URL de vidéos à partir d'un fichier .txt.")
    print("Entrez '3' pour entrer une URL de playlist YouTube.")
    print("Entrez 'q' pour quitter.")


# Fonction principale
def main():
    display_help()
    try:
        while True:
            choice = input("\nVotre choix : ")
            if choice == 'q':
                print("Programme terminé.")
                break

            quality = input("Choisissez la qualité de la vidéo (high/low) : ")
            only_audio = input("Télécharger uniquement l'audio (yes/no) : ").lower() == 'yes'

            data_directory = os.path.join(os.path.expanduser('~'), 'Downloads', 'Youtube download', 'data')
            if not os.path.exists(data_directory):
                os.makedirs(data_directory)

            if choice == '1':
                url = input("Entrez l'URL de la vidéo YouTube : ")
                yt = get_video_details(url)
                if yt:
                    print_video_details(yt)
                    download_video(yt, quality, only_audio)
            elif choice == '2':
                filename = os.path.join(data_directory, 'url.txt')
                if os.path.exists(filename):
                    urls = read_urls_from_file(filename)
                    for url in urls:
                        yt = get_video_details(url.strip())
                        if yt:
                            print_video_details(yt)
                            download_video(yt, quality, only_audio)
                else:
                    print("Le fichier", filename, "n'existe pas.")
            elif choice == '3':
                url = input("Entrez l'URL de la playlist YouTube : ")
                download_playlist(url, quality, only_audio)
            else:
                print("Choix invalide. Veuillez réessayer.")
    except KeyboardInterrupt:
        print("\nInterruption clavier détectée. Programme arrêté.")



if __name__ == "__main__":
    main()
