from rdflib import Graph, plugin
from rdflib.parser import Parser
from rdflib import URIRef, Literal, Graph, RDF, Namespace



# Set the paths to your CSV file and the ontology file
csv_file = "Seri.csv"  # Replace with the data source 
ontology_file = "foo.ttl" # Replace with the ontology

# Create an RDF graph
graph = Graph()

# Load the ontology into the graph
graph.parse(source=ontology_file, format="ttl")

# Set the namespace for your ontology
foo = Namespace("https://w3id.org/def/foo#")
sosa = Namespace("http://w3.org/ns/sosa/")
pos = Namespace("https://w3.org/2003/01/geo/wgs84_pos#")
xsd= Namespace('http://www.w3.org/2001/XMLSchema#')
# RML mapping code
# Iterate over the CSV file and map the data to RDF triples
with open(csv_file, 'r') as file:
    # Skip the header row if present
    next(file)

    for line in file:
        # Split the CSV line into columns
        columns = line.strip().split(',')
        

        # Create subject URI
        subject_uri = URIRef(foo+columns[0])

        # Add triples to the graph
        graph.add((subject_uri, RDF.type, sosa.Observation)) # Replace with the appropriate class from your ontology
        graph.add((subject_uri, foo.LocalDate, Literal(columns[1], datatype=xsd.date))) # Replace with the appropriate predicate from your ontology
        graph.add((subject_uri, foo.LocalTime, Literal(columns[2], datatype=xsd.time)))
        graph.add((subject_uri, foo.GMTDate, Literal(columns[3], datatype=xsd.date)))
        graph.add((subject_uri, foo.GMTTime, Literal(columns[4], datatype=xsd.time)))
        graph.add((subject_uri, pos.lat, Literal(columns[5], datatype=xsd.float)))
        graph.add((subject_uri, pos.long, Literal(columns[6], datatype=xsd.float)))
        graph.add((subject_uri, foo.Temperature, Literal(columns[8], datatype=xsd.double)))
        graph.add((subject_uri, foo.Speed, Literal(columns[9], datatype=xsd.integer)))
        graph.add((subject_uri, foo.Direction, Literal(columns[10], datatype=xsd.integer)))
        graph.add((subject_uri, foo.Cov, Literal(columns[11], datatype=xsd.integer)))
        graph.add((subject_uri, foo.HDOP, Literal(columns[12], datatype=xsd.integer)))
        graph.add((subject_uri, foo.Distance, Literal(columns[13], datatype=xsd.float)))
      

# Save the resulting knowledge graph to a file
output_file = "SeriKG.rdf"
graph.serialize(destination=output_file, format="ttl")

