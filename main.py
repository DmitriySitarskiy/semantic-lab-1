from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import FOAF, XSD

# Створюємо граф
g = Graph()

# Створюємо власний простір імен
EX = Namespace("http://example.org/")

# Додаємо дані про Кейда
kade = URIRef(EX.Cade)
g.add((kade, RDF.type, FOAF.Person))
g.add((kade, FOAF.name, Literal("Cade")))
g.add((kade, FOAF.age, Literal(33, datatype=XSD.integer)))  # Його вік
g.add((kade, FOAF.homepage, URIRef("http://example.org/cade")))
g.add((kade, FOAF.based_near, Literal("1516 Henry Street, Berkeley, California 94709, USA")))
g.add((kade, FOAF.knows, URIRef(EX.Emma)))  # Кейд знає Емму

# Додаємо дані про його інтереси та місця, які відвідав
g.add((kade, FOAF.interest, Literal("Birds")))
g.add((kade, FOAF.interest, Literal("Ecology")))
g.add((kade, FOAF.interest, Literal("Environment")))
g.add((kade, FOAF.interest, Literal("Photography")))
g.add((kade, FOAF.interest, Literal("Traveling")))
g.add((kade, FOAF.pastProject, Literal("Canada")))
g.add((kade, FOAF.pastProject, Literal("France")))

# Додаємо дані про Емму
emma = URIRef(EX.Emma)
g.add((emma, RDF.type, FOAF.Person))
g.add((emma, FOAF.name, Literal("Emma")))
g.add((emma, FOAF.age, Literal(36, datatype=XSD.integer)))  # Їй 36 років
g.add((emma, FOAF.homepage, URIRef("http://example.org/emma")))
g.add((emma, FOAF.based_near, Literal("Carrer de la Guardia Civil 20, 46020 Valencia, Spain")))

# Додаємо її інтереси
g.add((emma, FOAF.interest, Literal("Cycling")))
g.add((emma, FOAF.interest, Literal("Music")))
g.add((emma, FOAF.interest, Literal("Traveling")))
g.add((emma, FOAF.pastProject, Literal("Portugal")))
g.add((emma, FOAF.pastProject, Literal("Italy")))
g.add((emma, FOAF.pastProject, Literal("France")))
g.add((emma, FOAF.pastProject, Literal("Germany")))
g.add((emma, FOAF.pastProject, Literal("Denmark")))
g.add((emma, FOAF.pastProject, Literal("Sweden")))

# Додаємо факт їхньої зустрічі за допомогою власного предикату
g.add((kade, EX.met, Literal("Paris, August 2014", datatype=XSD.string)))

# Серіалізуємо граф у формат TURTLE і записуємо у файл
g.serialize("graph.ttl", format="turtle")

# Виводимо всі трійки графу
print("Усі трійки графу:")
for s, p, o in g:
    print(s, p, o)

# Виводимо трійки, що стосуються Емми
print("\nТрійки про Емму:")
for s, p, o in g.triples((emma, None, None)):
    print(s, p, o)

# Виводимо трійки, що містять імена людей
print("\nТрійки, що містять імена людей:")
for s, p, o in g.triples((None, FOAF.name, None)):
    print(s, p, o)