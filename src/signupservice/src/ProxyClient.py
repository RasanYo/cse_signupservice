import pyrebase
import os

path = os.path.dirname(__file__) +"/serviceAccountKey.json"

config = {
    "apiKey": "AIzaSyBHPwniesoLkpFUJRpR-ebt7kqCmTfhTGE",
    "authDomain": "cse-loginservice.firebaseapp.com",
    "projectId": "cse-loginservice",
    "storageBucket": "cse-loginservice.appspot.com",
    "serviceAccount": path,
    "messagingSenderId": "655431064989",
    "appId": "1:655431064989:web:e37b3ccb837d39a37ea374",
    "measurementId": "G-19ETGCMBKF",
    "databaseURL": ""
}

class ProxyClient :
        
    def __init__(self):
        # cred = credentials.Certificate("../serviceAccountKey.json")
        # self.firebase = firebase_admin.initialize_app(cred)
        print(f"[SERIVCE ACCOUNT DIR] {path}")
        firebase = pyrebase.initialize_app(config)
        self.auth = firebase.auth()
        self.connected = True
        self.logged_in = False
        self.user = None
        
    def get_uid(self):
        if (self.user):
            return self.auth.get_account_info(self.user['idToken'])['users'][0]['localId']
        else:
            return "guest"
       
    def sign_up(self, email, password):
        self.user = self.auth.create_user_with_email_and_password(email, password)
        self.logged_in = True
        print(f"[SIGNED UP] {self.user['email']}")
    
    def print_user(self):
        info = self.auth.get_account_info(self.user['idToken'])
        return self.get_uid(), info
        
    
    
