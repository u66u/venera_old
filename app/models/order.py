import uuid
from sqlalchemy import String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import Base 
from sqlalchemy.orm import Mapped, mapped_column


class Order(Base):
    __tablename__ = "order"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("user.id"), nullable=False
    )
    product_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("product.id"), nullable=False
    )
    comments: Mapped[str] = mapped_column(
        Text, nullable=True
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    user: Mapped[User] = relationship("User")
    product: Mapped[Product] = relationship("Product")
