import uuid
from pydantic import BaseModel
from typing import Optional
'''2024年12月13日 协作云B组 刘畅'''


class Table(BaseModel):
    id: uuid.UUID
    topic: str  # 标题
    description: Optional[str] = None  # 描述
    work_document: Optional[str] = None  # 工作文档
    responsible_man: str  # 负责人
    re_check_man: str  # 复核人
    responsible_department: str  # 负责部门
    task: Optional[str] = None  # 任务
    plan: Optional[str] = None  # 计划
    discussion: Optional[str] = None  # 研讨
    thesis: Optional[str] = None  # 议题
    group: Optional[str] = None  # 小组
    create_time: str  # 创建时间
    last_edit_time: str  # 最后编辑时间
    create_man: str  # 创建人
    last_edit_man: str  # 最后编辑人
    correlation: Optional[str] = None  # 关联


def main():

    row_1 = Table(
        id=uuid.uuid4(),
        topic='组建项目部议事机构',
        description=None,
        work_document=None,
        responsible_man='黄奕楠',
        re_check_man='张果',
        responsible_department='数据云-办公室',
        task='梳理协作秘书岗位职责',
        plan=None,
        discussion=None,
        thesis='组建数据云项目部议事机构,建立创赛绩效制度',
        group=None,
        create_time='2024年12月6日',
        last_edit_time='2024年12月8日',
        create_man='张果',
        last_edit_man='张果',
        correlation=None
    )
    row_2 = Table(
        id=uuid.uuid4(),
        topic='研发数据云客户端数据集页面',
        description=None,
        work_document=None,
        responsible_man='薛菲',
        re_check_man='张果',
        responsible_department='数据云-产品研发部',
        task=None,
        plan='数据云客户端',
        discussion=None,
        thesis=None,
        group=None,
        create_time='2024年12月6日',
        last_edit_time='2024年12月8日',
        create_man='张果',
        last_edit_man='张果',
        correlation=None
    )
    row_3 = Table(
        id=uuid.uuid4(),
        topic='梳理联盟管理制度',
        description=None,
        work_document='量潮创新联盟手册-初稿',
        responsible_man='莫志超',
        re_check_man='张果',
        responsible_department='数据云-产品运营部',
        task=None,
        plan=None,
        discussion=None,
        thesis=None,
        group=None,
        create_time='2024年12月8日',
        last_edit_time='2024年12月8日',
        create_man='莫志超',
        last_edit_man='张果',
        correlation=None
    )
    row_4 = Table(
        id=uuid.uuid4(),
        topic='梳理团队协作制度',
        description=None,
        work_document='量潮团队协作手册-初稿',
        responsible_man='邱艺佳',
        re_check_man='莫志超',
        responsible_department='数据云-产品运营部',
        task=None,
        plan=None,
        discussion=None,
        thesis=None,
        group=None,
        create_time='2024年12月8日',
        last_edit_time='2024年12月8日',
        create_man='莫志超',
        last_edit_man='张果',
        correlation=None
    )
    row_5 = Table(
        id=uuid.uuid4(),
        topic='梳理数据工程最佳实践',
        description=None,
        work_document='量潮数据工程手册-初稿',
        responsible_man='张嘉轩',
        re_check_man='莫志超',
        responsible_department='数据云-产品运营部',
        task=None,
        plan=None,
        discussion=None,
        thesis=None,
        group=None,
        create_time='2024年12月8日',
        last_edit_time='2024年12月8日',
        create_man='莫志超',
        last_edit_man='张果',
        correlation=None
    )
    row_6 = Table(
        id=uuid.uuid4(),
        topic='梳理项目管理制度',
        description=None,
        work_document='量潮项目管理手册',
        responsible_man='宋昇瑞',
        re_check_man='莫志超',
        responsible_department='数据云-产品运营部',
        task=None,
        plan=None,
        discussion=None,
        thesis=None,
        group=None,
        create_time='2024年12月8日',
        last_edit_time='2024年12月8日',
        create_man='莫志超',
        last_edit_man='张果',
        correlation=None
    )
    row_7 = Table(
        id=uuid.uuid4(),
        topic='建设项目部教学机制',
        description=None,
        work_document=None,
        responsible_man='张奕冉',
        re_check_man='张果',
        responsible_department='数据云-办公室',
        task='实现商品价格计算Python程序',
        plan='创赛教学管理',
        discussion=None,
        thesis=None,
        group=None,
        create_time='2024年12月8日',
        last_edit_time='2024年12月8日',
        create_man='张果',
        last_edit_man='张果',
        correlation=None
    )
    row_8 = Table(
        id=uuid.uuid4(),
        topic='浙理工实训申请入职',
        description=None,
        work_document=None,
        responsible_man='张果',
        re_check_man='薛菲',
        responsible_department='协作云-办公室',
        task=None,
        plan=None,
        discussion=None,
        thesis=None,
        group='浙理工实训入职小组',
        create_time='2024年12月10日',
        last_edit_time='2024年12月10日',
        create_man='薛菲',
        last_edit_man='薛菲',
        correlation=None
    )
    row_9 = Table(
        id=uuid.uuid4(),
        topic='金融科技比赛选题',
        description=None,
        work_document=None,
        responsible_man='黄奕楠',
        re_check_man='谢梓鹏',
        responsible_department='数据云-商业计划部',
        task=None,
        plan=None,
        discussion=None,
        thesis=None,
        group='金融科技选题小组',
        create_time='2024年12月10日',
        last_edit_time='2024年12月11日',
        create_man='薛菲',
        last_edit_man='谢梓鹏',
        correlation='金融科技比赛选题'
    )
    row_10 = Table(
        id=uuid.uuid4(),
        topic='西交招募渠道',
        description=None,
        work_document=None,
        responsible_man='张果',
        re_check_man='薛菲',
        responsible_department='协作云-办公室',
        task=None,
        plan=None,
        discussion=None,
        thesis=None,
        group=None,
        create_time='2024年12月11日',
        last_edit_time='2024年12月11日',
        create_man='张果',
        last_edit_man='张果',
        correlation='建立稳定的西交招募渠道'
    )


if __name__ == "__main__":
    main()
