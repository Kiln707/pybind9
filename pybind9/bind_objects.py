from ipaddress import ip_address, ip_network, ip_interface

class Match:
    def __init__(self, ip_address_only=False, ip_network_only=False, *args):
        self.values = []
        self.ip_address_only = ip_address_only
        self.ip_network_only = ip_network_only
        if args:
            self.add(*args)

    #Valid values are True(all), False(None), 'localhost', 'localnets', ip_address and ip_network objects
    def isvalid(self, value, silent=True):
        if self.ip_address_only and not isinstance(value, ip_address):
            return False if silent else raise TypeError()
        elif self.ip_network_only and not isinstance(value, ip_network):
            return False if silent else raise TypeError()
        elif not isinstance(value, (bool, ip_address, ip_network, str)):
            return False if silent else raise TypeError()
        elif isinstance(value, str) and not (value.toLower() == 'localhost' or value.toLower() == 'localnets'):
            return False if silent else raise ValueError()
        return True

    def add(self, *args):
        for value in args:
            if self.isvalid(value, silent=False):
                self.values.append(value)

    def remove(self, value):
        self.values.remove(value)

    def values(self):
        return list(self.values)

    def count(self, value=None):
        if value:
            return self.values.count(value)
        return len(self)

    @ip_address_only.getter
    def ip_address_only(self):
        return self.ip_address_only

    @ip_network_only.getter
    def ip_network_only(self):
        return self.ip_network_only

    def __len__(self):
        return len(self.values)


class ACL():
    def __init__(self, name='', match=Match(False)):
        self.name=name
        self.match=match

    def isvalid(self):
        if self.name and self.match:
            return True
        return False

class Options():
    def __init__(self):
        self.allow_query=Match(True)
        self.allow_recursion=Match(True)
        self.blackhole=Match(False)
        self.directory='/var/named/'
        self.forwarders=Match(False)
        self.forward='first'
        self.listen_on=None
        self.notify='yes'
        self.pid_file=''
        self.root_delegation_only=False
        self.statistics_file=''

    @allow_query.setter
    def set_allow_query(self, match):
        assert isinstance(match, Match), 'Match must be instance of Match'
        self.allow_query=match




class NamedConf():

    def __init__(self):
        self.acls=[]
        self.options={}
        self.views=[]
        self.zones=[]
