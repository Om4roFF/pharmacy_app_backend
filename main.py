from typing import Optional

import uvicorn
from fastapi import *
from endpoints import users, auth
from db.base import database

app = FastAPI(title='Bolat Pharmacy')
app.include_router(users.router, prefix='/users', tags=['users'])
app.include_router(auth.router, prefix='/auth', tags=['auth'])


@app.on_event("startup")
async def startup():
    print('start')
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8000)
