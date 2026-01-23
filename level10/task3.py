required_permissions = {"edit", "delete", "publish"}

user_permissions = {"connect", "view", "edit", "publish"}

def check_admin_access(user_perm, req_perm):
    return user_perm in req_perm

print(check_admin_access(user_permissions, required_permissions))