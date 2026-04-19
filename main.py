from artifact import Artifact, Painting, Sculpture, give_name_artifact


def give_name_main():
    return f"main name: {__name__}"


if __name__ == "__main__":
    a1 = Artifact("a1", 1598)
    a2 = Artifact("a2", 1958)
    a3 = Artifact("a3", 1002)

    p1 = Painting("p1", 1587, "art1", "oil")
    p2 = Painting("p2", 902, "art2", "pastel")
    p3 = Painting("p3", 1877, "art3", "crayon")

    s1 = Sculpture("s1", 1950, "marble", 15)
    s2 = Sculpture("s2", 1801, "bronze", 100)

    print(f"{s1.is_old(10)=}")
    print(give_name_artifact())
    print(give_name_main())
    print(__name__)

from renaissance import painting11, building11, sculpture11

print("Painting:")
print("Name:", painting11.name)
print("Date:", painting11.date)
print("Artist:", painting11.artist)
print("Medium:", painting11.medium)

print()
print("Building:")
print("Name:", building11.name)
print("Date:", building11.date)
print("Architect:", building11.architect)

print()
print("Sculpture:")
print("Name:", sculpture11.name)
print("Date:", sculpture11.date)
print("Material:", sculpture11.material)
print("Size:", sculpture11.size)