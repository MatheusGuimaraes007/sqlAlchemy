import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase
from models.tipo_picole import TipoPicole
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped, mapped_column

class Lote(ModelBase):
  __tablename__: str = 'lotes'

  id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
  data_criacao: Mapped[int] = mapped_column(sa.DateTime, default=datetime.now, index=True)
  id_tipo_picole: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('tipos_picole.id')) #tabela.campo
  tipo_picole: Mapped[TipoPicole] = orm.relationship('TipoPicole', lazy='joined') # Conf interna do SQL Alchemy
  quantidade: Mapped[int] = mapped_column(sa.Integer, nullable=False)
  
  def __repr__(self) -> str:
    return f'<Lote: {self.id}>'
  