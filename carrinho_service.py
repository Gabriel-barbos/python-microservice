from fastapi import FastAPI

app = FastAPI()

cart = {}

@app.post("/carrrinho/{user_id}/add")
async def add_carrinho(user_id: int, produto_id: int, quantidade: int):
    cart[user_id] = {"produto_id": produto_id, "quantidade": quantidade}
    return {"status": "sucesso", "mensagem": "Produto adicionado ao carrinho"}

def salvar_carrinho(carrinho_cache: dict):
    with open("carrinho_cache.txt",  "w") as file:
        for produto_id, quantidade in carrinho_cache.items():
            file.write(f"{produto_id}:{quantidade}\n")

def carregar_carrinho_cache() -> dict[str, int]:
    cache = {}
    try:
        with open("carrinho_cache.txt", "r") as file:
            for line in file:
                produto_id, quantidade = line.strip().split(":")
                cache[produto_id] = quantidade
    except FileNotFoundError:
        pass
    return cache

# Rota para buscar GET
@app.get("/cache/carrinho")
async def get_cache():
    cache_data = carregar_carrinho_cache()
    return cache_data
