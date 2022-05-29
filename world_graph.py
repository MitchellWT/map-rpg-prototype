
class WorldGraph:
    def __init__(self, location_list, init_location, connector_list):
        self.location_list = location_list
        self.init_location = init_location
        self.graph = {}
        for connection in connector_list:
            if connection[0] not in self.graph.keys():
                self.graph[connection[0]] = [(connection[1], connection[2])]
                continue
            self.graph[connection[0]].append((connection[1], connection[2]))
