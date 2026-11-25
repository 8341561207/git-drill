def apply_discount(price,percent):
    if percent<0 or percent>100:
        raise ValueError("percent value must be between 0 and 100")
    discount=price*percent/100
    return price-discount
def get_user(users,user_id):
    try:
        for user in users:
                if user["id"]==user_id:
                    return user
    except:
         raise ValueError("User not found")
       