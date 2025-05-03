"""
# 1 - Bucar o registro a ser deletado
# 2 - Fazer a deleção do objeto encontrado
# 3 - Registrar no banco de dados a deleção
"""
import asyncio
from sqlalchemy.future import select
from typing import Optional

from conf.db_session import create_session

from models.revendedor import Revendedor
from models.picole import Picole

async def deletar_picole(id_picole: int) -> None:
  async with create_session() as session:
    # Passo 1
    query = select(Picole).filter(Picole.id == id_picole)
    resultado = await session.execute(query)
    picole: Optional[Picole] = resultado.unique().scalar_one_or_none()

    if picole:
      # Passo 2
      await session.delete(picole)
      # Passo 3
      await session.commit()
    else: 
      print(f'Não encontrei picole com id {id_picole}')


async def deletar_revendedor(id_revendedor: int) -> None:
  async with create_session() as session:
    query = select(Revendedor).filter(Revendedor.id == id_revendedor)
    resultado = await session.execute(query)
    revendedor: Optional[Revendedor] = resultado.unique().scalar_one_or_none()

    if revendedor: 
      await session.delete(revendedor)
      await session.commit()
    else: 
      print(f'Não encontrei nenhum revendedor com id {id_revendedor}')

async def select_filtro_revendedor(id_revendedor: int) -> None:
  async with create_session() as session:
    query = select(Revendedor).filter(Revendedor.id == id_revendedor)
    resultado = await session.execute(query)
    revendedor: Optional[Revendedor] = resultado.scalar_one_or_none() 

    if revendedor:
      print(f'ID: {revendedor.id}')
      print(f'Razão Social: {revendedor.razao_social}')
    else: 
      print(f'Não encontrei nenhum revendedor com id {id_revendedor}')


if __name__ == '__main__':
 # from update_main import select_filtro_picole

  # id_picole = 5
  # # Antes
  # select_filtro_picole(id_picole)
  # # Deletar
  # deletar_picole(id_picole=id_picole)
  # # Depois
  # select_filtro_picole(id_picole)
  id_revendedor = 1
  # Antes
  asyncio.run(select_filtro_revendedor(id_revendedor))
  # # Deletar
  # deletar_revendedor(id_revendedor)
  # # Depois
  # select_filtro_revendedor(id_revendedor)

  