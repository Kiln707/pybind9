import argparse

options_filename = '/etc/bind/named.conf.options'

if __name__ == "__main__":
    argsp = argparse.ArgumentParser()
    cmdp=argsp.add_subparsers(title="commands", dest="cmd", help="Command")
    cmdp.required = True
    #Acl Subparsers
    acl_cmd = cmdp.add_parser('acl',help='Manage Bind9 ACLs')
    aclcmdp = acl_cmd.add_subparsers(title='action', dest='action', help="Acl Actions")
    acl_create = aclcmdp.add_parser('create', help='Create new ACL')
    acl_create.add_argument('name', type=str, nargs='?', help='ACL Name')
    acl_delete = aclcmdp.add_parser('delete', help='Delete ACL')
    acl_delete.add_argument('name', type=str, nargs='?', help='ACL Name')
    acl_list = aclcmdp.add_parser('list', help='List existing ACLs')

    #acl_member = aclcmdp.add_parser('members', help='List members within given ACL')
    #Zone Subparsers
    zone_cmd = cmdp.add_parser('zone', help='Manage Bind9 Zones')
    args = argsp.parse_args()
    print(args)
    if (args.cmd == "acl"):
        print(args.name)
    elif args.cmd == "zone":
        print("Going into zone")
