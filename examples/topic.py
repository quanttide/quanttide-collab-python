"""
Examples for topic management
"""

from uuid import uuid4
from quanttide_collab.models.topic import Topic


def main():
    topic_pm = Topic(id=uuid4(), name='improving-pm', title='提高项目管理效率', description="客户抱怨沟通不够通畅")


if __name__ == "__main__":
    main()
