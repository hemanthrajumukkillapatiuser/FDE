import json

from fastapi import FastAPI, HTTPException

app = FastAPI(title="User CRUD API")

FILE_NAME = "users.json"


# ---------- helper functions ----------

def read_users():
    file = open(FILE_NAME, "r") #open file in read mode 
    users = json.load(file)
    file.close()
    return users


def write_users(users):
    file = open(FILE_NAME, "w") #open file in write mode
    json.dump(users, file, indent=2)
    file.close()


def find_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def check_required_fields(data):
    required_fields = ["name", "email"]
    for field in required_fields:
        if field not in data:
            raise HTTPException(status_code=400, detail=field + " is required")


# ---------- endpoints ----------

@app.get("/users")
def get_all_users():
    users = read_users()
    return users


@app.get("/users/{user_id}")
def get_one_user(user_id: int):
    users = read_users()
    user = find_user(users, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/users", status_code=201)
def add_user(data: dict):
    
    check_required_fields(data)
    users = read_users()

    if "id" in data:
        if find_user(users, data["id"]) is not None:
            raise HTTPException(status_code=409, detail="User id already exists")
        new_id = data["id"]
    else:
        new_id = 1
        for user in users:
            if user["id"] >= new_id:
                new_id = user["id"] + 1

    data["id"] = new_id
    users.append(data)
    write_users(users)
    return data


@app.put("/users/{user_id}")
def replace_user(user_id: int, data: dict):
    check_required_fields(data)
    users = read_users()
    user = find_user(users, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    data["id"] = user_id
    position = users.index(user)
    users[position] = data
    write_users(users)
    return data


@app.patch("/users/{user_id}")
def update_user(user_id: int, data: dict):
    users = read_users()
    user = find_user(users, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    for key in data:
        if key != "id":
            user[key] = data[key]

    write_users(users)
    return user


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    users = read_users()
    user = find_user(users, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    users.remove(user)
    write_users(users)
    return user