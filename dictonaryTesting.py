import pickle

users={
    0: {
        "username": "swagmaster420",
        "password": "yomama"
    }
}

print(users)
print(users[0]['username'])

users[1]={}
users[1]['username']="yolo"

print(users)