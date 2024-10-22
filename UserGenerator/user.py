"""Module to generate users"""
import logging
import faker
from pathlib import Path

fake = faker.Faker(locale="fr_FR")
BASE_DIR = Path(__file__).parent
logging.basicConfig(level=logging.DEBUG,
                    filename=BASE_DIR / "users.log",
                    filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")

def get_user():
    """Génère un nom aléatoire avec Faker

    Returns:
        str: nom et prénom séparé par un espace
    """
    logging.info("Création d'un utilisateur")
    return f"{fake.first_name()} {fake.last_name()}"

def get_users(nb):
    """Génère une liste de 'nb' noms

    Args:
        nb (int): nombre de noms à générer

    Returns:
        list[str]: une liste contenant le nombre de noms demandés
    """
    logging.info(f"Création de {nb} utilisateur")
    return [get_user() for _ in range(nb)]
    # users = []
    # for i in range(nb):
    #     users.append(get_user())
    # return users

if __name__ == "__main__":
    user = get_user()
    print(user)
    users = get_users(5)
    print(users)
