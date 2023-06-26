"""Configuração do acesso ao banco de dados"""

# Bibliotecas
import motor.motor_asyncio

try:
    from models.PyObjectId import PyObjectId

except:
    from lista_supermercado_mongodb.models.PyObjectId import PyObjectId



# Configuração da conexão com o banco de dados
MONGODB_URL = "mongodb://prometheus:12345@172.17.0.2:27017"
DATABASE_NAME = "prometheus-mongodb"

class Database():
    def __init__(self) -> None:
        self.connected = False
        self.mongodb_client = None

    async def db_connection(self):
        if self.connected == False:
            self.client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
            self.connected = True
        db = self.client[DATABASE_NAME]
        return db

database = Database()

async def adicionar_produto(produto_data: dict):
    db = await database.db_connection()
    produto = await db.supermercado.insert_one(produto_data)
    new_produto = await db.supermercado.find_one({"_id": produto.inserted_id})
    return to_produto(new_produto)

async def encontrar_produto_por_id(id: str):
    db = await database.db_connection()
    produto = await db.supermercado.find_one({"_id": PyObjectId(id)})
    if produto:
        return to_produto(produto)
    return None

async def listar_produtos():
    db = await database.db_connection()
    produtos = db.supermercado.find({})
    
    if produtos:
        produtos = await produtos.to_list(None)
        return to_produto_list(produtos)
    return None

async def apagar_todos_produtos():
    db = await database.db_connection()
    produto = await db.supermercado.delete_many({})
    return None


async def existe_produto_por_id(id: str):
    db = await database.db_connection()
    produto = await db.supermercado.find_one({"_id": PyObjectId(id)})
    if produto:
        return True
    return False

async def atualizar_produto(id: str, produto_data: dict):
    db = await database.db_connection()
    produto_a_atualizar = await db.supermercado.update_one({"_id": PyObjectId(id)}, {"$set": produto_data})

    produto_atualizado = await db.supermercado.find_one({"_id": PyObjectId(id)})
    return to_produto(produto_atualizado)

async def apagar_produto_por_id(id: str):
    db = await database.db_connection()
    produto = await db.supermercado.delete_one({"_id": PyObjectId(id)})
    return True

def to_produto(item) -> dict:
    return {
        "id": str(item.get("_id")),
        "item": item.get("item"),
        "quantidade": item.get("quantidade"),
        "preco": item.get("preco")
    }

def to_produto_list(items) -> list:
    return [to_produto(item) for item in items]

# fonte: https://www.tutorialsbuddy.com/create-rest-api-to-perform-crud-operations-using-fastapi-and-mongodb
