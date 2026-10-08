from pathlib import Path
from pyshacl import validate
from rdflib import Graph, Namespace


SH = Namespace("http://www.w3.org/ns/shacl#")

SHACL_FILE = "SHACL.ttl"
ONTOLOGY_FILE = "ontology_OWL.ttl"
TEST_DIR = Path("tests")


# Load SHACL shapes
shacl_graph = Graph()
shacl_graph.parse(SHACL_FILE, format="turtle")

# Load OWL ontology
ontology_graph = Graph()
ontology_graph.parse(ONTOLOGY_FILE, format="turtle")


print("=" * 100)
print(f"{'Test':<40} {'Result':<10} {'Message'}")
print("=" * 100)


for test_file in sorted(TEST_DIR.glob("*.ttl")):

    # Load test RDF
    data_graph = Graph()
    data_graph.parse(test_file, format="turtle")

    # Run validation
    conforms, results_graph, results_text = validate(
        data_graph,
        shacl_graph=shacl_graph,
        ont_graph=ontology_graph,
        inference="rdfs"
    )

    if conforms:
        result = "PASS"
        message = ""
    else:
        result = "FAIL"
        # Get SHACL messages
        messages = list(set(results_graph.objects(None, SH.resultMessage)))
        message = " | ".join(str(msg) for msg in messages)

    print(f"{test_file.name:<40} {result:<10} {message}")

print("=" * 100)