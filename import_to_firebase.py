from firebase import firebase

firebase= firebase.FirebaseApplication("https://lifevestdb.firebaseio.com/",None)
data = {
        'Name':'Reinaliza',
        'Age':22
}

result=firebase.post('/lifevestdb/Passenger:',data)
print(result)