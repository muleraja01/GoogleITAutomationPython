def full_emails(people):
    result=[]
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("rajasekhar95.offical@gmail.com", "Raja Sekhar"),("mrunal@gmail.com","mrunal")]))
# Parameters are passing as tuple