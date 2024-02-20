import uuid
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import Base 
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "user"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), primary_key=True, default=lambda _: str(uuid.uuid4())
    )
    email: Mapped[str] = mapped_column(
        String(254), nullable=False, unique=True, index=True
    )
    hashed_password: Mapped[str] = mapped_column(String(128), nullable=False)
