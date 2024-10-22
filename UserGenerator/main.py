import user

print("On démarre")

user1 = user.get_user()
print(f"Utilisateur généré : {user1}")

user2 = user.get_user()
print(f"Utilisateur généré : {user2}")

users = user.get_users(5)
print(users)

print("Fin")
