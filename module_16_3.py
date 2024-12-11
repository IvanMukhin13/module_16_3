from fastapi import FastAPI, Path
from typing import Annotated
import uvicorn

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/')
async def main_page() -> str:
    return "Главная страница"


@app.get('/users')
async def get_all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_new_user(username: Annotated[
    str, Path(min_length=5, max_length=20, description='Enter username', examples=['UrbanUser'])],
                       age: Annotated[int, Path(ge=18, le=120, description='Enter age', examples=[22])]) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f'User {current_index} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=0, le=120, description='Enter id', examples=[22])],
                      username: Annotated[
                          str, Path(min_length=5, max_length=20, description='Enter username', examples=['UrbanUser'])],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', examples=[22])]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=0, le=120, description='Enter id', examples=[22])]):
    users.pop(str(user_id))



if __name__ == '__main__':
    uvicorn.run(app='module_16_3:app', host="127.0.0.1", port=8000, reload=True)
