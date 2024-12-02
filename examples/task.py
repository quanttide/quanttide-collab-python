"""
Example for task management
"""

import uuid

from quanttide_collab.models import Task


def main():
    task = Task(id=uuid.uuid4(), title='测试任务删除功能', description='删除成功并保存已删除事件')


if __name__ == "__main__":
    main()
