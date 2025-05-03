from typing import List
import asyncio

from sqlalchemy import func # Funções de agregação
from sqlalchemy.future import select
from conf.helpers import formata_data
from conf.db_session import create_session

# Select Simples 
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor

# Select Compostos / Complexos 
from models.picole import Picole

## Select Simples -> SELECT * FROM aditivos_nutritivos

async def select_todos_aditivos_nutrivos():
  async with create_session() as session:
    query = select(AditivoNutritivo)
    aditivos_nutritivos: List[AditivoNutritivo] = await session.execute(query)
    aditivos_nutritivos = aditivos_nutritivos.scalars().all()
    """
    Com uma linha só
    aditivos_nutritivos: List[AditivoNutritivo] = (await session.execute(select(AditivoNutritivo)).scalars().all())
    """
    for an in aditivos_nutritivos:
      print(f'ID: {an.id}')
      print(f'Data: {formata_data(an.data_criacao)}')
      print(f'Nome: {an.nome}')
      print(f'Formula Química: {an.formula_quimica}')


async def select_filtro_sabor(id_sabor: int) -> None:
  async with create_session() as session:
    query = select(Sabor).filter(Sabor.id == id_sabor)
    # query = select(Sabor).where(Sabor.id) == id_sabor
    resultado = await session.execute(query)
    # Forma 1
    sabor: Sabor = resultado.scalars().first()
    # Forma 2
    # sabor: Sabor = resultado.scalars().one_or_none() # Recomendado
    print(f'ID: {sabor.id}')
    print(f'Data: {formata_data(sabor.data_criacao)}')
    print(f'Nome: {sabor.nome}')


async def select_complexo_picole() -> None:
  async with create_session() as session:
    query = select(Picole)
    resultado = await session.execute(query)
    picoles: List[Picole] = resultado.scalars().unique().all()

    for picole in picoles:
      print(f'ID: {picole.id}')
      print(f'Data: {formata_data(picole.data_criacao)}')
      print(f'Preco: {picole.preco}')
      print(f'ID do sabor: {picole.id_sabor}')
      print(f'Sabor: {picole.sabor.nome}')
      print(f'ID Embalagem: {picole.id_tipo_embalagem}')
      print(f'Tipo da Embalagem: {picole.tipo_embalagem.nome}')


async def select_order_by_sabor() -> None:
  async with create_session() as session:
    query = select(Sabor).order_by(Sabor.data_criacao.desc())
    resultado = await session.execute(query)
    sabores: List[Sabor] = resultado.scalars().all()

    for sabor in sabores:
      print(f'ID: {sabor.id}')
      print(f'Data: {formata_data(sabor.data_criacao)}')


async def select_group_by_picole() -> None:
  async with create_session() as session:
    query = select(Picole).group_by(Picole.id, Picole.id_tipo_picole)
    resultado = await session.execute(query)
    picoles: List[Picole] = resultado.scalars().unique().all()

    for picole in picoles:
      print(f'ID: {picole.id}')
      print(f'Tipo Picole: {picole.tipo_picole.nome}')
      print(f'Sabor: {picole.sabor.nome}')
      print(f'Preço: {picole.preco}')


async def select_limit() -> None:
  async with create_session() as session:
    query = select(Sabor).limit(25)
    resultado = await session.execute(query)
    sabores: List[Sabor] = resultado.scalars()

  for sabor in sabores:
    print(f'ID: {sabor.id}')

async def select_count_revendedor() -> None:
  async with create_session() as session:
    query = select(func.count(Revendedor.id))
    resultado = await session.execute(query)
    qtd: int = resultado.scalar()

    print(qtd)

async def select_agregacao() -> None: 
  async with create_session() as session:
    query = select(
      func.sum(Picole.preco).label('soma'),
      func.avg(Picole.preco).label('media'),
      func.min(Picole.preco).label('Mais Barato'),
      func.max(Picole.preco).label('Mais Caro'),
    )
    resultado = await session.execute(query)
    resultado = resultado.all()

    print(f'A soma de todos os picoles é: {resultado[0][0]}')
    print(f'A média de todos os picoles é: {resultado[0][1]}')
    print(f'Picole mais barato: {resultado[0][2]}')
    print(f'Picole mais caro: {resultado[0][3]}')

if __name__ == '__main__':
  # asyncio.run(select_todos_aditivos_nutrivos())
  # select_filtro_sabor(44)
  # asyncio.run(select_complexo_picole())
  # asyncio.run(select_order_by_sabor())
  # select_order_by_sabor()
  # select_group_by_picole()
  # select_limit()
  # select_count_revendedor()
    asyncio.run(select_agregacao())