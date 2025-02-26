"""
Examples for topic management
"""

from uuid import uuid4
from datetime import datetime
from quanttide_collab.topic import Topic

class Topic:
    def __init__(self, id, name, title, description, content, status, priority):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.content = content
        self.status = status
        self.priority = priority
        self.created_at = datetime.now()
        self.updated_at = None


def main():
    topic_pm = Topic(
        id=uuid4(),
        name='improving-pm',
        title='提高项目管理效率',
        description="客户抱怨沟通不够通畅",
        content="详细描述项目管理中的问题和改进措施",
        status="open",
        priority="high"
    )

if __name__ == "__main__":
    main()
