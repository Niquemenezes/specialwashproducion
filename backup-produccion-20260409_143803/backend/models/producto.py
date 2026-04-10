from .base import db, iso, now_madrid
from sqlalchemy.orm import relationship

class Producto(db.Model):
    __tablename__ = "producto"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    categoria = db.Column(db.String(120))
    codigo_barras = db.Column(db.String(64), unique=True, index=True)
    stock_minimo = db.Column(db.Integer, default=0)
    stock_actual = db.Column(db.Integer, default=0)
    pedido_en_curso = db.Column(db.Boolean, default=False)
    pedido_fecha = db.Column(db.DateTime)
    pedido_cantidad = db.Column(db.Integer)
    pedido_canal = db.Column(db.String(80))
    pedido_proveedor_id = db.Column(db.Integer)
   

    created_at = db.Column(
        db.DateTime(timezone=True),
        default=now_madrid,
        nullable=False,
    )

    entradas = relationship("Entrada", back_populates="producto", lazy="selectin", cascade="all, delete-orphan")
    salidas = relationship("Salida", back_populates="producto", lazy="selectin", cascade="all, delete-orphan")
    codigos_barras_extra = relationship(
        "ProductoCodigoBarras",
        lazy="selectin",
        cascade="all, delete-orphan",
        passive_deletes=True,
        primaryjoin="Producto.id==ProductoCodigoBarras.producto_id",
    )

    def to_dict(self):
        codigos = []
        seen = set()

        if self.codigo_barras:
            seen.add(self.codigo_barras)
            codigos.append({"codigo_barras": self.codigo_barras, "marca": None})

        for item in self.codigos_barras_extra:
            if not item.codigo_barras or item.codigo_barras in seen:
                continue
            seen.add(item.codigo_barras)
            codigos.append({"id": item.id, "codigo_barras": item.codigo_barras, "marca": item.marca})

        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "codigo_barras": self.codigo_barras,
            "stock_minimo": self.stock_minimo,
            "stock_actual": self.stock_actual,
            "pedido_en_curso": bool(self.pedido_en_curso),
            "pedido_fecha": iso(self.pedido_fecha),
            "pedido_cantidad": self.pedido_cantidad,
            "pedido_canal": self.pedido_canal,
            "pedido_proveedor_id": self.pedido_proveedor_id,
            "codigos_barras": codigos,
            "created_at": iso(self.created_at),
        }
