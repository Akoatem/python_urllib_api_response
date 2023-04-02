import urllib.request
# https://www.youtube.com/watch?v=LosIGgon_KM
# request is used to request a file from the internet
# open is used to open a file

response = urllib.request.urlopen("https://www.google.com/")
print(response)
print('***********')
# print status
# 200 response code everything ok
# 400 response code bad request
# 403 response code is forbidden
# 404 response code Not Found
print(response.status)
print('***********')
# print headers
print(response.headers)
print('***********')
# to read memory location
print(response.read(200))
print('***********')
# size of the response
print(response.length)
print('***********')
print(response.peek)