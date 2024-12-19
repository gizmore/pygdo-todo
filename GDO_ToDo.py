from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_String import GDT_String
from gdo.date.GDT_Created import GDT_Created
from gdo.date.GDT_Deleted import GDT_Deleted
from gdo.date.GDT_Timestamp import GDT_Timestamp
from gdo.ui.GDT_Title import GDT_Title


class GDO_ToDo(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('todo_id'),
            GDT_Title('todo_title').maxlen(48).not_null(),
            GDT_String('todo_entry').maxlen(256).not_null(),
            GDT_Created('todo_created'),
            GDT_Creator('todo_creator'),
            GDT_Deleted('todo_deleted'),
            GDT_Timestamp('todo_accomplished'),
        ]
