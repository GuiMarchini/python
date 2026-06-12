from ...A_locadora.models import db
from .base import ModeloBase

# Dica: data_inicio/data_fim usam db.Date (importe Date se precisar)


class Locacao(ModeloBase):
    __tablename__ = "locacoes"

    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForgeinKey("cliente_id"), nullable=False)
    veiculo_id = db.Column(db.Integer, db.ForgeinKey("veiculo_id"), nullable=False)

    locacoes = db.relationship("locacoes", back_populates="clientes", back_populates="veiculos")

    @classmethod
    def listar_com_detalhes(cls):
        return cls.query.order_by(cls.data_criacao.desc()).all()
