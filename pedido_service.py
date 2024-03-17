from fastapi import FastAPI

app = FastAPI()

@app.post("/pedido/{user_id}/add")
async def criar_pedido(user_id: int):
   return {"status": "sucesso", "mensagem": "Pedido criado", "order_id": 123}

def salvar_pedido(order_cache: dict):
    with open("order_cache.txt",  "w") as file:
        for user_id, order_id in order_cache.items():
            file.write(f"{user_id}:{order_id}\n")

def carregar_order_cache() -> dict[int, str]:
    cache = {}
    try:
        with open("order_cache.txt", "r") as file:
            for line in file:
                user_id, order_id = line.strip().split(":")
                cache[user_id] = order_id
    except FileNotFoundError:
        pass
    return cache

# Rota para buscar GET
@app.get("/cache/orders")
async def get_cache():
    cache_data = carregar_order_cache()
    return cache_data
