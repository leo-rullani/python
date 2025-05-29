class Pokemon:
    """
    Eine Klasse zur Repräsentation eines Pokémon mit Basisfunktionen wie Level, Angriff und Darstellung.

    Attribute:
        __n (str): Der Name des Pokémons.
        __lebenspunkte (int): Aktuelle Lebenspunkte (standardmäßig 42).
        __level (int): Level des Pokémons (standardmäßig 1).
    """

    def __init__(self, name):
        """
        Initialisiert ein neues Pokémon-Objekt.

        Args:
            name (str): Der Name des Pokémons.
        """
        self.__n = name
        self.__lebenspunkte = 42
        self.__level = 1

    def __str__(self):
        """
        Gibt eine lesbare String-Darstellung des Pokémons zurück.

        Returns:
            str: Formatierter String mit Name, Lebenspunkten und Level.
        """
        return f"Name: {self.__n}\nLebenspunkte: {self.__lebenspunkte}\nLevel: {self.__level}"

    def __gt__(self, other):
        """
        Vergleichsoperator > (größer als) basierend auf dem Level.

        Args:
            other (Pokemon): Ein anderes Pokémon zum Vergleich.

        Returns:
            bool: True, wenn dieses Pokémon ein höheres Level hat als das andere.
        """
        return self.__level > other.__level

    def vorstellen(self):
        """
        Gibt den Namen des Pokémons zweimal aus, wie in der Serie üblich.
        """
        print(f"{self.__n} {self.__n}!")

    def zeige_lebenspunkte(self):
        """
        Gibt die aktuellen Lebenspunkte zurück.

        Returns:
            int: Lebenspunkte des Pokémons.
        """
        return self.__lebenspunkte

    def zeige_level(self):
        """
        Gibt das aktuelle Level des Pokémons aus.
        """
        print(f" {self.__n} :: {self.__level}")

    def entwickeln(self):
        """
        Erhöht das Level des Pokémons um 1.
        """
        self.__level += 1

    def attackieren(self, other, schaden):
        """
        Greift ein anderes Pokémon an und reduziert dessen Lebenspunkte.

        Args:
            other (Pokemon): Das gegnerische Pokémon.
            schaden (int): Schadenspunkte, die abgezogen werden.
        """
        other.__lebenspunkte -= schaden


if __name__ == "__main__":
    p1 = Pokemon("Pikachu")
    p2 = Pokemon("Bisasam")

    p1.entwickeln()
    p1.entwickeln()
    p1.zeige_level()
    p2.zeige_level()

    p1.attackieren(p2, 10)
    p2.attackieren(p1, 5)
    print(p2.zeige_lebenspunkte())

    print(p1)
    print(p2)

    print(p1 > p2)