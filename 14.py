def today1():
    import datetime as dt
    today = dt.datetime.now()
    list1 = []
    h1 = today.hour
    m1 = today.minute
    s1 = today.second

    list1.append(h1)
    list1.append(m1)
    list1.append(s1)
    return list1

print(today1())
