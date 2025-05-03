"""
1 - Busca o registro a ser atualizado
2 - Faz as alterações no registro
3 - Salva o registro no banco de dados
"""
import asyncio
from sqlalchemy.future import select
from conf.db_session import create_session
from models.sabor import Sabor
from models.picole import Picole



async def select_filtro_picole(id_picole: int) -> None:
  async with create_session() as session:
    query = select(Picole).where(Picole.id == id_picole)
    resultado = await session.execute(query)
    picole: Picole = resultado.unique().scalar_one_or_none()
    if picole:
      print(f'ID: {picole.id}')
      print(f'Nome: {picole.sabor.nome}')
      print(f'Preco: {picole.preco}')
    else:
      print(f'Não existe sabor com ID')


async def atualizar_sabor(id_sabor: int, novo_nome: str) -> None:
  async with create_session() as session:
    # Passo 1
    query = select(Sabor).filter(Sabor.id == id_sabor)
    resultado = await session.execute(query)
    sabor: Sabor = resultado.unique().scalar_one_or_none()

    if sabor:
      # Passo 2
      sabor.nome = novo_nome
      # Passo 3
      await session.commit()
    else:
      print(f'Não existe sabor com ID {id_sabor}')


async def atualizar_picole(id_picole: int, novo_preco: float, novo_sabor: int = None):
  async with create_session() as session:
    # Passo 1
    query = select(Picole).filter(Picole.id == id_picole)
    resultado = await session.execute(query)
    picole: Picole = resultado.unique().scalar_one_or_none()

    if picole:
      # Passo 2
      picole.preco = novo_preco
      # Se quiser alterar o sabor ...
      if novo_sabor:
        picole.id_sabor = novo_sabor
      await session.commit()
    else: 
      print(f'Não existe sabor com ID {id_picole}')

if __name__ == '__main__':
  # from select_main import select_filtro_sabor
  # id_sabor = 42
  # # Antes 
  # select_filtro_sabor(id_sabor=id_sabor)
  # # Atualizando
  # atualizar_sabor(id_sabor=id_sabor, novo_nome='Abacate')
  # select_filtro_sabor(id_sabor)
  
  id_picole = 21
  novo_preco = 9.99
  id_novo_sabor = 42
  asyncio.run(select_filtro_picole(id_picole=id_picole))
  # atualizar_picole(id_picole=id_picole, novo_preco=novo_preco, novo_sabor=id_novo_sabor)
  # select_filtro_picole(id_picole=id_picole)