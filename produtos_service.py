from fastapi import FastAPI

app = FastAPI()

@app.get("/produtos")
async def listar_produtos():
    return {"produtos": [{"id": 1, "nome": "Produto A", "preco": 100},
                         {"id": 2, "nome": "Produto B", "preco": 150}]}

def salvar_produtos(produtos_cache: dict):
    with open("produtos_cache.txt",  "w") as file:
        for id, nome, preco in produtos_cache.items():
            file.write(f"{id}:{nome}:{preco}\n")

def carregar_produtos_cache() -> dict[int, str, int]:
    cache = {}
    try:
        with open("produtos_cache.txt", "r") as file:
            for line in file:
                id, nome, preco = line.strip().split(":")
                cache[id] = nome, preco
    except FileNotFoundError:
        pass
    return cache

# Rota para buscar GET
@app.get("/cache/produtos")
async def get_cache():
    cache_data = carregar_produtos_cache()
    return cache_data
