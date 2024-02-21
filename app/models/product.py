import uuid
from sqlalchemy import String, Numeric, Text
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import Base 
from sqlalchemy.orm import Mapped, mapped_column


class Product(Base):
    __tablename__ = "product"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    name: Mapped[str] = mapped_column(
        String(254), nullable=False
    )
    description: Mapped[str] = mapped_column(
        Text, nullable=True
    )
    price: Mapped[Numeric] = mapped_column(
        Numeric(10, 2), nullable=False
    )