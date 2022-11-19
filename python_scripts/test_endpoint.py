from fastapi import FastAPI
app = FastAPI()
@app.get("/account/{id}")
async def root(id):
    return {"account_id":id}