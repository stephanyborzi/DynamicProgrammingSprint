from controller import *

db = [
    {
        "id_pedido": 1,
        "insumo": {
            "id_insumo": 1,
            "nome": "dipirona",
            "validade": add_months(datetime.now(), 18).strftime("%Y-%m-%d")
        },
        "quantidade": 500,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "id_pedido": 2,
        "insumo": {
            "id_insumo": 2,
            "nome": "paracetamol",
            "validade": add_months(datetime.now(), 12).strftime("%Y-%m-%d")
        },
        "quantidade": 1000,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    },
    {
        "id_pedido": 3,
        "insumo": {
            "id_insumo": 3,
            "nome": "ibuprofeno",
            "validade": add_months(datetime.now(), 6).strftime("%Y-%m-%d")
        },
        "quantidade": 700,
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
]

def main():
    while True:
        if menu(db):
            break

if __name__ == "__main__":
    main()