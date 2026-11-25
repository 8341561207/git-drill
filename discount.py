def apply_discounte(price,percent):
    discount=price*percent/100
    return price-discount
def get_user(users,user_id):
    for user in users:
        if user["id"]==user_id:
            return user
    print("not found")    