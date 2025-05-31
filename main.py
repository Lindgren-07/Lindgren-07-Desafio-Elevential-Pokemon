from flask import Flask, render_template,request, flash, redirect
from conexao import session
import crud
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from model.Pokemon import Pokemon
from model.Tipo import Tipo
from util import tipos_pokemon,tipos_invertido




app = Flask(__name__)

app.secret_key = 'desafio'


@app.route('/')
def index():
    return render_template('index.html')


#Pokemon

@app.route('/salvar_pokemon', methods=['POST'])
def salvar_pokemon():
    codigo = int(request.form['codigo'])
    nome = request.form['nome']
    tipo1 = int(request.form['tipo1'])
    tipo2 = request.form.get('tipo2')
    tipo2 = int(tipo2) if tipo2 else None

    modo = request.form.get('modo')  

    try:
        if modo == 'editar':
            crud.editar_pokemon(session, codigo, nome, tipo1, tipo2)
            flash("Pokémon atualizado com sucesso!")
        else:
            crud.cadastrar_pokemon(session, codigo, nome, tipo1, tipo2)
            flash("Pokémon cadastrado com sucesso!")

    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            flash("Erro: Já existe um Pokémon com esse código!")
        else:
            flash(f"Erro ao salvar: {e}")
            print(e)
        return redirect('/cadastrar_pokemon')

    except Exception as e:
        flash(f"Erro ao salvar: {e}")
        print(e)
        return redirect('/cadastrar_pokemon')

    return redirect('/exibir_pokemons')


@app.route('/cadastrar_pokemon', methods=['GET'])
def cadastrar_pokemon():
    global tipos_pokemon, tipos_invertido
    tipos_pokemon = crud.atualizar_dicionario_tipos(session)
    tipos_invertido = crud.atualizar_dicionario_invertido(session)
    return render_template('cadastrar_pokemon.html', edicao=False, tipos=tipos_pokemon)



@app.route('/deletar_pokemon/<int:codigo>', methods=['POST'])
def deletar_pokemon_route(codigo):
    if crud.deletar_pokemon(session, codigo):
        flash("Pokémon deletado com sucesso!")
    else:
        flash("Pokémon não encontrado.")
    return redirect('/exibir_pokemons')



@app.route('/editar_pokemon/<int:codigo>', methods=['GET'])
def editar_pokemon(codigo):
    global tipos_pokemon, tipos_invertido
    tipos_pokemon = crud.atualizar_dicionario_tipos(session)
    tipos_invertido = crud.atualizar_dicionario_invertido(session)
    
    pokemon = session.query(Pokemon).filter_by(codigo=codigo).first()
    if not pokemon:
        flash("Pokémon não encontrado.")
        return redirect('/exibir_pokemons')
    
    return render_template('cadastrar_pokemon.html', pokemon=pokemon, edicao=True, tipos=tipos_pokemon)



@app.route('/exibir_pokemons')
def exibir_pokemons():
    global tipos_pokemon, tipos_invertido
    tipos_pokemon = crud.atualizar_dicionario_tipos(session)
    tipos_invertido = crud.atualizar_dicionario_invertido(session)
    nome = request.args.get('nome', '').strip()
    tipo_str = request.args.get('tipo', '').strip().lower()

    tipo = None
    if tipo_str:
        if tipo_str in tipos_invertido:
            tipo = tipos_invertido[tipo_str]
        else:
            flash(f"Tipo '{tipo_str}' não encontrado.")
           
            return render_template('exibir_pokemons.html', pokemons=[], tipos=tipos_pokemon)

    pokemons = crud.filtrar_pokemons(session, nome, tipo)

    if not pokemons:
        flash("Nenhum Pokémon encontrado com os filtros informados.")

    return render_template('exibir_pokemons.html', pokemons=pokemons, tipos=tipos_pokemon)

#Tipos

@app.route('/salvar_tipos', methods=['POST'])
def salvar_tipos():
    codigo = int(request.form['codigo'])
    nome = request.form['nome']
   

    modo = request.form.get('modo')  

    try:
        if modo == 'editar':
            crud.editar_tipo(session, codigo, nome)
            flash("Tipo atualizado com sucesso!")
        else:
            crud.cadastrar_tipo(session, codigo, nome)
            flash("Tipo cadastrado com sucesso!")

    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            flash("Erro: Já existe um Tipo com esse código!")
        else:
            flash(f"Erro ao salvar: {e}")
            print(e)
        return redirect('/cadastrar_tipos')

    except Exception as e:
        flash(f"Erro ao salvar: {e}")
        print(e)
        return redirect('/cadastrar_tipos')

    return redirect('/exibir_tipos')


@app.route('/cadastrar_tipos', methods=['GET'])
def cadastrar_tipos():
    return render_template('cadastrar_tipos.html', edicao=False, tipo=None)


@app.route('/editar_tipos/<int:codigo>', methods=['GET'])
def editar_tipos(codigo):
    pokemon = session.query(Tipo).filter_by(codigo=codigo).first()
    if not pokemon:
        flash("Tipo não encontrado.")
        return redirect('/exibir_tipos')
    return render_template('cadastrar_tipos.html', tipo=pokemon, edicao=True)



@app.route('/deletar_tipo_route/<int:codigo>', methods=['POST'])
def deletar_tipo_route(codigo):
    try:
        crud.deletar_tipo(session, codigo)  
        session.commit()
        flash("Tipo excluído com sucesso!")
    except IntegrityError:
        session.rollback()
        flash("Não é possível excluir este Tipo porque ele está associado a um Pokémon.")
    except Exception as e:
        session.rollback()
        flash(f"Erro ao excluir: {e}")
    return redirect('/exibir_tipos')



@app.route('/exibir_tipos')
def exibir_tipos():
    global tipos_pokemon, tipos_invertido
    tipos_pokemon = crud.atualizar_dicionario_tipos(session)
    tipos_invertido = crud.atualizar_dicionario_invertido(session)

    codigo_str = request.args.get('codigo', '').strip()
    nome = request.args.get('nome', '').strip()

    codigo = None
    if codigo_str.isdigit():
        codigo = int(codigo_str)
    elif codigo_str != '':
        flash(f"Código inválido: {codigo_str}")
        return render_template('exibir_tipos.html', tipos=[])

    tipos = crud.filtrar_tipos(session, codigo=codigo, nome=nome)

    if not tipos:
        flash("Nenhum Tipo encontrado com os filtros informados.")

    return render_template('exibir_tipos.html', tipos=tipos)





if __name__ == '__main__':
    app.run(debug=True)