# https://www.docstring.fr/glossaire/dictionnaire/?utm_source=udemy&utm_campaign=dictionnaire-glossary
from pathlib import Path

# Init :
# mkdir Dossier_a_trier && cd Dossier_a_trier
# for ext in mp3 wav flac avi mp4 gif bmp png jpg txt pptx csv xls odp pages abc titi
# do
# seq 5 | while read i;do touch fichier$i.$ext;done
# done

dictionnaire = {".mp3" : "Musique",
    ".wav" : "Musique",
    ".flac" : "Musique",
    ".avi" : "Videos",
    ".mp4" : "Videos",
    ".gif" : "Videos",
    ".bmp" : "Images",
    ".png" : "Images",
    ".jpg" : "Images",
    ".txt" : "Documents",
    ".pptx" : "Documents",
    ".csv" : "Documents",
    ".xls" : "Documents",
    ".odp" : "Documents",
    ".pages" : "Documents"
}
# autres : Divers

p = Path.cwd() / "Dossier_a_trier"
if p.is_dir:
    print("===== Démarrage du tri =====")
    for f in p.iterdir():
        print(f)
        # print(f" - {f.suffix} {dictionnaire.get(f.suffix, "Autres")}")
        dest_dir = p / dictionnaire.get(f.suffix, "Autres")
        dest_f = dest_dir / f.name
        dest_dir.mkdir(exist_ok=True)
        print(f" => {dest_f}")
        f.rename(dest_f)

