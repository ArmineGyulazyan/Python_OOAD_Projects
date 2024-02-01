import Properties
import Agents
import Client


def main():
    res_property = Properties.Residential('Ulneci 5',1000000,'kanach kturov shenq')
    my_agent = Agents.Agent('Helen', '033556688')
    new_client = Client.Client('Lea', '055668877')

    my_agent.put_on_sale(res_property)
    new_client.view_catalog(my_agent)
    my_agent.sell_property(res_property)


if __name__ == '__main__':
    main()
