import os, json

class addUser:
    def addNewUser(userData):
        with open(r'users.json', 'r+') as outfile:
            if not os.stat("users.json").st_size:
                data = {"users":[]}
                data["users"].append(userData)
                json.dump(data, outfile, indent=4)
            else:
                data = json.load(outfile)
                data["users"].append(userData)
                outfile.seek(0)
                json.dump(data, outfile, indent=4)
