from data.neo4j_wrapper import Neo4jWrapper
from daemons.text_to_cypher_daemon import TextToCypherDaemon

class KGMemory:
    def __init__(self):
        neo_url = "bolt://neo4j:7687"
        self.neo = Neo4jWrapper(neo_url, user="neo4j", password="password")

    def record(self, text):
        cypher_query = TextToCypherDaemon.generate_cypher(text)
        self.neo.query(cypher_query)

    def query_memory(self, text):
        pass
