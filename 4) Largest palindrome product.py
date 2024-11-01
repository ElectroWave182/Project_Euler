prod,jsp,jspTrop = [[digit1*digit2 for digit1 in range(900,1000)] for digit2 in range(900,1000)],[],[]
for liste1d in prod:
    jsp.extend(liste1d)
for nb in jsp:
    if list(str(nb)) == list(reversed(str(nb))): jspTrop.append(nb)
print(max(jspTrop))