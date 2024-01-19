from rdflib import Graph, plugin
from rdflib.parser import Parser
from rdflib import URIRef, Literal, Graph, RDF, Namespace


# Set the paths to your CSV file and the ontology file
csv_file = "Soil.csv"  # Replace with the data source 
ontology_file = "foo.ttl" # Replace with the ontology

# Create an RDF graph
graph = Graph()

# Load the ontology into the graph
graph.parse(source=ontology_file, format="ttl")

# Set the namespace for your ontology
foo = Namespace("http://w3id.org/def/foo#")
sosa = Namespace("http://w3.org/ns/sosa/")
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
        subject_uri = URIRef(foo + columns[0])

        # Add triples to the graph
        graph.add((subject_uri, RDF.type, sosa.Observation))  # Replace with the appropriate class from your ontology
        graph.add((subject_uri, foo.Site, Literal(columns[1], datatype=xsd.string)))  # Replace with the appropriate predicate from your ontology
        graph.add((subject_uri, foo.Land_Use, Literal(columns[2], datatype=xsd.string)))
        graph.add((subject_uri, foo.Plot_Name, Literal(columns[3], datatype=xsd.string)))
        graph.add((subject_uri, foo.Subplot, Literal(columns[4], datatype=xsd.string)))
        graph.add((subject_uri, foo.NO3_N, Literal(columns[5], datatype=xsd.float)))
        graph.add((subject_uri, foo.NH4_N, Literal(columns[6], datatype=xsd.float)))
        graph.add((subject_uri, foo.Total_N, Literal(columns[7], datatype=xsd.float)))
        graph.add((subject_uri, foo.Ca, Literal(columns[8], datatype=xsd.float)))
        graph.add((subject_uri, foo.Mg, Literal(columns[9], datatype=xsd.float)))
        graph.add((subject_uri, foo.K, Literal(columns[10], datatype=xsd.float)))
        graph.add((subject_uri, foo.P, Literal(columns[11], datatype=xsd.float)))
        graph.add((subject_uri, foo.Fe, Literal(columns[12], datatype=xsd.float)))
        graph.add((subject_uri, foo.Mn, Literal(columns[13], datatype=xsd.float)))
        graph.add((subject_uri, foo.Cu, Literal(columns[14], datatype=xsd.float)))
        graph.add((subject_uri, foo.Zn, Literal(columns[15], datatype=xsd.float)))
        graph.add((subject_uri, foo.B, Literal(columns[16], datatype=xsd.float)))
        graph.add((subject_uri, foo.S, Literal(columns[17], datatype=xsd.float)))
        graph.add((subject_uri, foo.Pb, Literal(columns[18], datatype=xsd.float)))
        graph.add((subject_uri, foo.AI, Literal(columns[19], datatype=xsd.float)))
        graph.add((subject_uri, foo.Cd, Literal(columns[20], datatype=xsd.float)))

# Save the resulting knowledge graph to a file
output_file = "SoilKG.rdf"
graph.serialize(destination=output_file, format="ttl")


