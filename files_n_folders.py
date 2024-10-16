# https://www.docstring.fr/blog/gerer-des-chemins-de-fichiers-avec-pathlib/
from pathlib import Path

p = Path.cwd()
print(p)

# p = p / "dev" / "python-code"
# print(p)

for f in p.glob("*"):
    print(f" - {f.name}")
    print(f" - - {f.stem} - {f.suffix}")