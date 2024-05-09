from fastapi import FastAPI


app = FastAPI(
    title="Word2"
)

fake_users = [
    {"id": 1, "role": "Admin", "name":"Bob"},
    {"id": 2, "role": "Investor", "name":"John"},
    {"id": 3, "role": "Trader", "name":"Stella"}
]

fake_users2 = [
    {"id": 1, "role": "Admin", "name":"Bob"},
    {"id": 2, "role": "Investor", "name":"John"},
    {"id": 3, "role": "Trader", "name":"Stella"}
]

fake_trands = [
    {"id":1, "user_id": 1, "currency":"BTC", "side": "Buy", "Price": 123, "amount": 2.12},
    {"id":2, "user_id": 1, "currency":"BTC", "side": "Sell", "Price": 125, "amount": 2.12},
]




@app.get('/home/{user_id}')
async def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


@app.get("/trands")
def get_trands(limit: int = 1, offset: int = 0):
    return fake_trands[offset:][:limit]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users2))[0]
    current_user['name'] = new_name
    return {'status': 200, "data": current_user}