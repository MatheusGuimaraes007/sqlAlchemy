import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase
from models.revendedor import Revendedor
import sqlalchemy.orm as orm
from models.lote import Lote
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Nota Fiscal pode ter varios lotes - Montando Entidade de muitos para muitos
lotes_nota_fiscal = sa.Table(
  'lotes_nota_fiscal',
  ModelBase.metadata,
  sa.Column('id_nota_fiscal', sa.BigInteger, sa.ForeignKey('notas_fiscais.id')),
  sa.Column('id_lote', sa.BigInteger, sa.ForeignKey('lotes.id'))
)

class NotaFiscal(ModelBase):
  __tablename__: str = 'notas_fiscais'

  id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
  data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True)
  valor: Mapped[float] = mapped_column(sa.DECIMAL(8,2), nullable=False)
  numero_serie: Mapped[str] = mapped_column(sa.String(45), unique=True, nullable=False)
  descricao: Mapped[str] = mapped_column(sa.String(200), nullable=False)
  id_revendedor: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('revendedores.id', ondelete='CASCADE')) #tabela.campo
  revendedor: Mapped[Revendedor] = relationship('Revendedor', lazy='joined', cascade='delete') # Conf interna do SQL Alchemy
  
  # Uma nota fiscal pode ter varios lotes e um lote está ligado a uma nota fiscal
  lote: Mapped[List[Lote]] = relationship('Lote', secondary=lotes_nota_fiscal, backref='lote', lazy='dynamic')

  
  def __repr__(self) -> str:
    return f'<Nota Fiscal: {self.numero_serie}>'
  