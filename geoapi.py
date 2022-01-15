from ip2geotools.databases.noncommercial import DbIpCity
#response = DbIpCity.get('147.229.2.90', api_key='free')
#print(response.city)

filepath = 'IPnodup.csv'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
        try:
            response = DbIpCity.get(line.strip(), api_key='free')
            f = open('final.csv', 'a',encoding="utf-8")
            f.write(response.ip_address)
            f.write(",")
            f.write(response.country)
            f.write(",")
            f.write(response.city)
            f.write(";")
            f.write("\n")
        except KeyError:
            print("Line {}: {}".format(cnt, "unknown"))
        line = fp.readline()
        cnt += 1
        if cnt>100:
            break