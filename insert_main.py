import asyncio

from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.conservante import Conservante
from models.ingrediente import Ingrediente
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole
from models.revendedor import Revendedor
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole


async def insert_aditivo_nutritivo() -> AditivoNutritivo:
  print('Cadastrando Aditivo Nutritivo')

  nome: str = input('Informe o nome do Aditivo Nutritivo: ')
  formula_quimica: str = input('Informe a fórmula química do aditivo nutritivo: ')

  an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

  async with create_session() as session:
    session.add(an)
    await session.commit()

    return an
    # print('Aditivo Nutritivo Cadastrado com Sucesso')
    # print(f'ID: {an.id}')
    # print(f'Data: {an.data_criacao}')
    # print(f'Nome: {an.nome}')
    # print(f'Fórmula Química: {an.formula_quimica}')


async def insert_sabor() -> None:
  print('Cadastro de Sabor do Picole')

  nome: str = input('Sabor do Picole: ')

  sb: Sabor = Sabor(nome=nome)

  async with create_session() as session:
    session.add(sb)
    await session.commit()

    print('Sabor Cadastrado com Sucesso')
    print(f'ID: {sb.id}')
    print(f'Data: {sb.data_criacao}')
    print(f'Nome: {sb.nome}')

async def insert_tipo_embalagem() -> None:
  print('Cadastro o Tipo da Embalagem')

  nome: str = input('Nome do Tipo da Embalagem: ')

  te: TipoEmbalagem = TipoEmbalagem(nome=nome)

  async with create_session() as session:
    session.add(te)
    await session.commit()

    print('Tipo de Embalage Cadastrado com Sucesso')
    print(f'ID: {te.id}')
    print(f'Data: {te.data_criacao}')
    print(f'Nome: {te.nome}')

async def insert_tipo_picole() -> None: 
  print('Cadastro de Tipo Picole')

  nome: str = input('Nome do Tipo de Picole')

  tp: TipoPicole = TipoPicole(nome=nome)

  async with create_session() as session:
    session.add(tp)
    await session.commit()
    print('Tipo de Picole Cadastrado com Sucesso')
    print(f'ID: {tp.id}')
    print(f'Data: {tp.data_criacao}')
    print(f'Nome: {tp.nome}')
  

async def insert_ingrediente() -> Ingrediente: 
  print('Cadastrando Ingrediente')

  nome: str = input('Ingrediente: ')

  ig: Ingrediente = Ingrediente(nome=nome)

  async with create_session() as session:
    session.add(ig)
    await session.commit()

    return ig
  
  # print('Ingrediente Cadastrado com Sucesso')
  # print(f'ID: {ig.id}')
  # print(f'Data: {ig.data_criacao}')
  # print(f'Nome: {ig.nome}')

async def insert_conservante() -> Conservante:
  print('Cadastrando Conservante')

  nome: str = input('Conservante: ')
  descricao: str = input('Descrição do Conservante: ')

  cvt: Conservante = Conservante(nome=nome, descricao=descricao)

  async with create_session() as session:
    session.add(cvt)
    await session.commit()

    return cvt

  # print('Conservante Cadastrado com Sucesso')
  # print(f'ID: {cvt.id}')
  # print(f'Data: {cvt.data_criacao}')
  # print(f'Nome: {cvt.nome}')

async def insert_revendedor() -> Revendedor:
  print('Cadastrando Revendedor')

  cnpj: str = input('Informe o CNPJ do Revendedor: ')
  razao_social: str = input('Razão Social do Revendedor: ')
  contato: str = input('Contato do Revendedor: ')

  rv: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato )

  async with create_session() as session:
    session.add(rv)
    await session.commit()

    return rv

async def insert_lote() -> Lote:
  print('Cadastrando Lote')

  id_tipo_picole: int = input('Informe o id do tipo Picole: ')
  quantidade: str = input('Quantidade de Picoles: ')

  lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

  async with create_session() as session:
    session.add(lote)
    await session.commit()

    return lote

async def insert_nota_fiscal() -> None:
  print('Cadastrando Nota Fiscal')

  valor: float = input('Informe Valor: ')
  numero_serie: str = input('Número de Série: ')
  descricao: str = input('Descrição: ')
  rev = await insert_revendedor()

  nf: NotaFiscal = NotaFiscal(valor=valor, numero_serie=numero_serie, descricao=descricao, id_revendedor=rev.id)
  lote1 = await insert_lote()
  nf.lote.append(lote1)
  lote2 = await insert_lote()
  nf.lote.append(lote2)
  async with create_session() as session:
    session.add(nf)
    await session.commit()
    await session.refresh(nf)

    print('Nota Fiscal')
    print(f'ID: {nf.id}')
    print(f'Data: {nf.data_criacao}')
    print(f'valor: {nf.valor}')
    print(f'Número de Série: {nf.numero_serie}')
    print(f'Descrição: {nf.descricao}')
    print(f'Foram cadastrados 2 lotes Lote 1: {lote1.quantidade} un \nLote 2: {lote2.quantidade} un')
    print(f'Revendedor: {nf.revendedor.razao_social}')

async def insert_picole() -> None:
  print('Cadastrando Picole')

  preco: float = input('Informe Preco do Picole: ')
  id_sabor: str = input('ID tipo da sabor: ')
  id_tipo_picole: str = input('ID tipo de picole: ')
  id_tipo_embalagem: str = input('ID tipo da embalagem: ')

  picole: Picole = Picole(id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem, id_tipo_picole=id_tipo_picole, preco=preco)

  ingrediente1 = await insert_ingrediente()
  picole.ingredientes.append(ingrediente1)
  ingrediente2 = await insert_ingrediente()
  picole.ingredientes.append(ingrediente2)

  #Tem conservante?
  conservante = await insert_conservante()
  picole.conservantes.append(conservante)

  #Tem aditivos nutritivos
  aditivo_nutritivo = await insert_aditivo_nutritivo()
  picole.aditivos_nutritivos.append(aditivo_nutritivo)

  async with create_session() as session:
    session.add(picole)
    await session.commit()
    await session.refresh(picole)

    print('Picole Cadastrado com Sucesso')
    print(f'ID: {picole.id}')
    print(f'Data: {picole.data_criacao}')
    print(f'preço: {picole.preco}')
    print(f'sabor: {picole.sabor.nome}')
    print(f'Tipo Picole: {picole.tipo_picole.nome}')
    print(f'Tipo da Embalagem: {picole.tipo_embalagem.nome}')
    print(f'Ingredientes: {picole.ingredientes}')
    print(f'Conservantes: {picole.conservantes}')
    print(f'Aditivo Nutritivo: {picole.aditivos_nutritivos}')




if __name__ == '__main__':
  # asyncio.run(insert_aditivo_nutritivo())
  asyncio.run(insert_sabor())
  # insert_tipo_embalagem()
  # insert_tipo_picole()
  # insert_ingrediente()
  # insert_conservante()
  # rev = insert_revendedor()
  # print(f'ID {rev.id}')
  # print(f'Data de Criação {rev.data_criacao}')
  # print(f'nome {rev.cnpj}')
  # print(f'Razão Social {rev.razao_social}')
  # print(f'Contato {rev.contato}')
  # lot = insert_lote()
  # print(f'ID: {lot.id}')
  # print(f'Data: {lot.data_criacao}')
  # print(f'Tipo Picole: {lot.id_tipo_picole}')
  # print(f'Quantidade: {lot.quantidade}')
  # insert_nota_fiscal()
  # insert_picole()