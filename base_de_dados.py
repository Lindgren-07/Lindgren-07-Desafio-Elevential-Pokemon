from model.Tipo import Tipo
import crud
from conexao import session
import json
from util import tipos_pokemon


for codigo, nome in tipos_pokemon.items():
    if not session.query(Tipo).filter_by(codigo=codigo).first():
        crud.cadastrar_tipo(session, codigo, nome)


with open('dados_iniciais.json', 'r') as f:
    pokemons = json.load(f)

for p in pokemons:
    tipo_primario_cod = next((cod for cod, nome in tipos_pokemon.items() if nome == p['tipo_primario']), None)
    tipo_secundario_cod = next((cod for cod, nome in tipos_pokemon.items() if nome == p['tipo_secundario']), None) if p.get('tipo_secundario') else None

    crud.cadastrar_pokemon(
        session,
        codigo=p['codigo'],
        nome=p['nome'],
        codigo_tipo_primario=tipo_primario_cod,
        codigo_tipo_secundario=tipo_secundario_cod
    )

if __name__ == "__main__":
    print("Populando banco de dados...")
