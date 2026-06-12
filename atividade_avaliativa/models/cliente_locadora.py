# O ponto em "from ." = import da MESMA pasta models (vizinho de quarto)
from ...A_locadora.models import db
from .base import ModeloBase


class ClienteLocadora(ModeloBase):
    __tablename__ = "clientes_locadora"

    nome = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    cnh = db.Column(db.String(11), nullable=False)

    locacoes = db.relationship("locacoes", back_populates="clientes")

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.nome).all()
