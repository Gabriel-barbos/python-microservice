from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/login")
async def login(username: str, password: str):
    if username == "user" and password == "password":
        return {"status": "sucesso", "mensagem": "Usuário autenticado"}
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

def salvar_login(login_cache: dict):
    with open("login_cache.txt",  "w") as file:
        for username, password in login_cache.items():
            file.write(f"{username}:{password}\n")

def carregar_login_cache() -> dict[str, str]:
    cache = {}
    try:
        with open("login_cache.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(":")
                cache[username] = password
    except FileNotFoundError:
        pass
    return cache

# Rota para buscar GET
@app.get("/cache/login")
async def get_cache():
    cache_data = carregar_login_cache()
    return cache_data
