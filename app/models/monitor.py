from sqlalchemy import ForeignKey, String, ARRAY, INTEGER
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import Optional, List
from ..db.session import Base


class Monitor(Base):
    
    __tablename__ = 'monitors'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(nullable=False)
    last_checked: Mapped[Optional[int]] = mapped_column(default=0)
    uptime_percentage: Mapped[int] = mapped_column(default=-1)
    is_active: Mapped[bool] = mapped_column(default=True, index=True)
    expected_status_code: Mapped[List[int]] = mapped_column(ARRAY(INTEGER), default=[200])
    
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    
    user: Mapped['User'] = relationship(back_populates='monitors')