import Agents
import Properties
class Client:
    def __init__(self, name: str, contact: str):
        self.name = name
        self.contact = contact

    def view_catalog(self,agent:Agents.Agent):
        for i in agent.on_sale_properties:
            print(i.feature)

    def buy_property(self,propertyy:Properties.Property,agent:Agents.Agent):
        agent.sell_property(propertyy)

    def put_my_property_on_sale(self,propertyy:Properties.Property,agent:Agents.Agent):
        agent.put_on_sale(propertyy)

