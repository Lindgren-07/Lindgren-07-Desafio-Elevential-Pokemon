from model.Pokemon import Pokemon
from model.Tipo import Tipo
 
def atualizar_dicionario_tipos(session):
    tipos = session.query(Tipo).all()
    return {tipo.codigo: tipo.nome for tipo in tipos}

def atualizar_dicionario_invertido(session):
    tipos = session.query(Tipo).all()
    return {tipo.nome.lower(): tipo.codigo for tipo in tipos}


def cadastrar_tipo(session,codigo,nome):
    try:
        tipo = Tipo(codigo,nome)
        session.add(tipo)
        session.commit()
    except Exception as e:
        session.rollback()
        print("Erro ao cadastrar tipo:", e)

    return tipo

def listar_tipos(session):
    return session.query(Tipo).all()

def editar_tipo(session, codigo, novo_nome):
    tipo = session.query(Tipo).filter_by(codigo=codigo).first()
    if tipo:
        tipo.set_nome(novo_nome)
        session.commit()
    return tipo

def deletar_tipo(session, codigo):
    tipo = session.query(Tipo).filter_by(codigo=codigo).first()
    if tipo:
        session.delete(tipo)
        session.commit()    
        return True
    return False

def buscar_tipo(session, codigo):
    return session.query(Tipo).filter_by(codigo=codigo).first()

def buscar_pokemon(session, codigo):
    return session.query(Pokemon).filter_by(codigo=codigo).first()


def cadastrar_pokemon(session, codigo, nome, codigo_tipo_primario, codigo_tipo_secundario=None):
    try:
        pokemon = Pokemon(codigo, nome, codigo_tipo_primario, codigo_tipo_secundario)
        session.add(pokemon)
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    return pokemon

def listar_pokemons(session):
    return session.query(Pokemon).order_by(Pokemon.codigo).all()

def editar_pokemon(session, codigo, novo_nome=None, novo_tipo_primario=None, novo_tipo_secundario=None):
    pokemon = session.query(Pokemon).filter_by(codigo=codigo).first()
    if pokemon:
        if novo_nome is not None:
            pokemon.set_nome(novo_nome)
        if novo_tipo_primario is not None:
            pokemon.set_tipo_primario(novo_tipo_primario)
        if novo_tipo_secundario is not None:
            pokemon.set_tipo_secundario(novo_tipo_secundario)
        session.commit()
    return pokemon

def deletar_pokemon(session, codigo):
    pokemon = session.query(Pokemon).filter_by(codigo=codigo).first()
    if pokemon:
        session.delete(pokemon)
        session.commit()
        session.expire_all()
        return True
    return False

def listar_pokemons_filtrados(session, nome=None, tipo=None):
    query = session.query(Pokemon)
    if nome:
        query = query.filter(Pokemon.nome.ilike(f"%{nome}%"))
    if tipo:
        query = query.filter(
            (Pokemon.codigo_tipo_primario == tipo) |
            (Pokemon.codigo_tipo_secundario == tipo)
        )
    return query.all()

def filtrar_pokemons(session, nome=None, tipo=None):
    query = session.query(Pokemon)

    if nome:
        query = query.filter(Pokemon.nome.ilike(f'%{nome}%'))
    
    if tipo:
        query = query.filter(
            (Pokemon.codigo_tipo_primario == tipo) | (Pokemon.codigo_tipo_secundario == tipo)
        )
    
    # Ordenar pelo código crescente
    query = query.order_by(Pokemon.codigo.asc())

    return query.all()


def filtrar_tipos(session, codigo=None, nome=None):
    query = session.query(Tipo)
    
    if codigo is not None:
        query = query.filter(Tipo.codigo == codigo)
    
    if nome:
        query = query.filter(Tipo.nome.ilike(f'%{nome}%'))
    
    return query.all()