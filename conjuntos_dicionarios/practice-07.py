main_permissions = input("Permissões principais\t->")
solicited_permissions = input("Permissões solicitadas\t->")

main_list = main_permissions.lower().split(',')
solicited_list = solicited_permissions.lower().split(',')

main_set = set(permission.strip() for permission in main_list)
solicited_permissions_set = set(permission.strip() for permission in solicited_list)

count_solicited = len(solicited_permissions_set)

if count_solicited != len(solicited_permissions_set.intersection(main_set)):
    print("\nAs permissões solicitadas não fazem parte das permissões principais.")
else:
    print("\nAs permissões solicitadas fazem parte das permissões principais.")
