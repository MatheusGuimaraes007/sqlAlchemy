import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.aditivo_nutritivo import AditivoNutritivo
import sqlalchemy.orm as orm
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Picole pode ter varios ingredientes
ingredientes_picole = sa.Table(
  'ingredientes_picole',
  ModelBase.metadata,
  sa.Column('id_picole', sa.BigInteger, sa.ForeignKey('picoles.id')),
  sa.Column('id_ingrediente', sa.BigInteger, sa.ForeignKey('ingredientes.id'))
)

# Picole pode ter varios consanvantes
conservantes_picole = sa.Table(
  'conservantes_picole',
  ModelBase.metadata,
  sa.Column('id_picole', sa.BigInteger, sa.ForeignKey('picoles.id')),
  sa.Column('id_conservante', sa.BigInteger, sa.ForeignKey('conservantes.id'))
)

# Picole pode ter varios aditivos nutritivos
aditivos_nutritivos_picole = sa.Table(
  'aditivos_nutritivos_picole',
  ModelBase.metadata,
  sa.Column('id_picole', sa.BigInteger, sa.ForeignKey('picoles.id')),
  sa.Column('id_aditivo_nutritivo', sa.BigInteger, sa.ForeignKey('aditivos_nutritivos.id'))
)


class Picole(ModelBase):
  __tablename__: str = 'picoles'

  id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
  data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True)
  preco: Mapped[float] = mapped_column(sa.DECIMAL(8,2), nullable=True)
  id_sabor: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('sabores.id'))
  sabor: Mapped[Sabor] = orm.relationship('Sabor', lazy='joined')
  id_tipo_embalagem: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('tipos_embalagem.id'))
  tipo_embalagem: Mapped[TipoEmbalagem] = orm.relationship('TipoEmbalagem', lazy='joined')
  id_tipo_picole: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('tipos_picole.id'))
  tipo_picole: Mapped[TipoPicole] = orm.relationship('TipoPicole', lazy='joined')

  # Um picole pode ter vários ingredientes
  ingredientes: Mapped[List[Ingrediente]] = orm.relationship('Ingrediente', secondary=ingredientes_picole, backref='ingrediente', lazy='joined')
  # Um picole pode ter varios conservantes ou mesmo nenhum
  conservantes: Mapped[Optional[List[Conservante]]] = orm.relationship('Conservante', secondary=conservantes_picole, backref='conservante', lazy='joined')
  # Um picole pode ter varios aditivos nutritivos ou mesmo nenhum
  aditivos_nutritivos: Mapped[Optional[List[AditivoNutritivo]]] = orm.relationship('AditivoNutritivo', secondary=aditivos_nutritivos_picole, backref='aditivo_nutritivo', lazy='joined')

  def __repr__(self) -> str:
    return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>'
  