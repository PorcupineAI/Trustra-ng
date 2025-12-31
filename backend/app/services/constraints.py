# backend/app/services/constraints.py
from sqlalchemy import CheckConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_mixin

Base = declarative_base()

@declarative_mixin
class UserConstraints:
    __table_args__ = (
        UniqueConstraint('phone', name='users_unique_phone'),
    )

@declarative_mixin
class EscrowConstraints:
    __table_args__ = (
        CheckConstraint('amount > 0', name='escrow_positive_amount'),
    )

@declarative_mixin
class RevenueConstraints:
    __table_args__ = (
        CheckConstraint('amount > 0', name='revenue_positive_amount'),
    )

@declarative_mixin
class NeonScoreConstraints:
    __table_args__ = (
        UniqueConstraint('id', name='playing_with_neon_unique_id'),
        CheckConstraint('score >= 0', name='playing_with_neon_positive_score'),
    )
