from rdflib import Graph, plugin
from rdflib.parser import Parser
from rdflib import URIRef, Literal, Graph, RDF, Namespace



# Set the paths to your CSV file and the ontology file
csv_file = "lianas.csv"  # Replace with the data source 
ontology_file = "foo.ttl" # Replace with the ontology

# Create an RDF graph
graph = Graph()

# Load the ontology into the graph
graph.parse(source=ontology_file, format="ttl")

# Set the namespace for your ontology
foo = Namespace("https://w3id.org/def/foo#")
sosa = Namespace("http://www.w3.org/ns/sosa/")
xsd = Namespace('http://www.w3.org/2001/XMLSchema#')

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
        graph.add((subject_uri, foo.Plot_no, Literal(columns[1], datatype=xsd.integer)))  # Replace with the appropriate predicate from your ontology
        graph.add((subject_uri, foo.Site_plot_code, Literal(columns[2], datatype=xsd.string)))
        graph.add((subject_uri, foo.Date, Literal(columns[3], datatype=xsd.date)))
        graph.add((subject_uri, foo.Tree_individual_no, Literal(columns[4], datatype=xsd.integer)))
        graph.add((subject_uri, foo.Tree_ID, Literal(columns[5], datatype=xsd.string)))
        graph.add((subject_uri, foo.Tree_dbh_cm, Literal(columns[6], datatype=xsd.float)))
        graph.add((subject_uri, foo.Tree_height_m, Literal(columns[7], datatype=xsd.Literal)))
        graph.add((subject_uri, foo.Tree_N_lianas, Literal(columns[8], datatype=xsd.integer)))
        graph.add((subject_uri, foo.Liana_dbh_cm, Literal(columns[9], datatype=xsd.float)))
        graph.add((subject_uri, foo.Tree_notes, Literal(columns[10], datatype=xsd.string)))
        graph.add((subject_uri, foo.Subplot_radius_m, Literal(columns[11], datatype=xsd.integer)))
      

# Save the resulting knowledge graph to a file
output_file = "VegKG.rdf"
graph.serialize(destination=output_file, format= "ttl")




      