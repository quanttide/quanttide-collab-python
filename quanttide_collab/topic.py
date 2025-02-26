"""
Models for topic management subdomain
"""

from uuid import UUID


class Topic:
    """
    QuantTide Collaboration Topic
    """
    id: UUID
    name: str
    title: str 
    description: str
