import uuid

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import json

# 定义用户类
class User(BaseModel):
    id: uuid.UUID
    name: str

# 定义任务类
class Task(BaseModel):
    title: str  # 标题
    description: Optional[str] = None  # 描述
    priority: Optional[int] = None  # 优先级
    status: Optional[str] = None  # 状态
    owner: User  # 负责人
    reviewer: User  # 复核人


class Topic(BaseModel):
    id: uuid.UUID
    title: str  # 标题
    description: Optional[str] = None  # 描述
    work_document: Optional[str] = None  # 工作文档
    owner: User  # 负责人
    reviewer: User  # 复核人
    responsible_department: str  # 负责部门
    task: Optional[List[Task]] = []  # 任务
    plan: Optional[str] = None  # 计划
    discussion: Optional[str] = None  # 研讨
    thesis: Optional[str] = None  # 议题
    group: Optional[str] = None  # 小组
    created_at: datetime  # 创建时间
    updated_at: datetime  # 更新时间
    created_by: User  # 创建者
    updated_by: User  # 更新者
    correlation: Optional[str] = None  # 关联

#简单设置一下，方便测试。实际应该来自数据库
def load_users() -> List[User]:
    return [
        User(id="f07e4e23-dc27-4011-bf07-cd8f9c12baf9", name="黄奕楠"),
        User(id="30c4e426-f7d4-4b22-ae59-5f1a09b10a5f", name="张果"),
    ]

# 以JSON作为源数据导入
def load_from_json(json_file: str, users: List[User]) -> List[Topic]:
    topics = []
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            # 类型转换，确保不出错
            item['id'] = uuid.UUID(item['id'])
            item['owner'] = uuid.UUID(item['owner']) if isinstance(item['owner'], str) else item['owner']
            item['reviewer'] = uuid.UUID(item['reviewer']) if isinstance(item['reviewer'], str) else item['reviewer']
            item['created_by'] = uuid.UUID(item['created_by']) if isinstance(item['created_by'], str) else item['created_by']
            item['updated_by'] = uuid.UUID(item['updated_by']) if isinstance(item['updated_by'], str) else item['updated_by']
            item['created_at'] = datetime.strptime(item['created_at'], '%Y-%m-%d %H:%M:%S')
            item['updated_at'] = datetime.strptime(item['updated_at'], '%Y-%m-%d %H:%M:%S')

            # 查找对应的 User 对象（通过 UUID），并替换为 User 实例
            item['owner'] = next(user for user in users if user.id == item['owner'])
            item['reviewer'] = next(user for user in users if user.id == item['reviewer'])
            item['created_by'] = next(user for user in users if user.id == item['created_by'])
            item['updated_by'] = next(user for user in users if user.id == item['updated_by'])

            # task 列表中的任务
            if 'task' in item:
                for task in item['task']:
                    task['owner'] = next(user for user in users if user.id == uuid.UUID(task['owner']))
                    task['reviewer'] = next(user for user in users if user.id == uuid.UUID(task['reviewer']))

            # 创建 Topic 对象并添加到列表
            topic = Topic(**item)
            topics.append(topic)
        return topics

def main():
    users=load_users()

    topics = load_from_json('data.json',users)

    for topic in topics:
        print(topic)

if __name__ == "__main__":
    main()

