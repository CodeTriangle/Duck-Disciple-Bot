import sqlite3
from core.log import log
from config.config import SQLITE3_DB_NAME, DB_TABLE_REMINDERS_NAME


# Database definitions
def _table_exists(conn, table):
    cursor = conn.execute(f''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table}' ''')

    return cursor.fetchone()[0] == 1


def _create_table_reminders(db):
    table = DB_TABLE_REMINDERS_NAME
    conn = sqlite3.connect(db)

    if _table_exists(conn, table):
        conn.close()
        return

    conn.execute(
        f'''
        CREATE TABLE {table}
        (
            UserId      TEXT    NOT NULL,
            MessageId   INT     NOT NULL,
            ChannelId   INT     NOT NULL,
            CreatedAt   INT     NOT NULL,
            RemindAfter INT     NOT NULL,
            RemindMsg   TEXT,
            Active      INT     NOT NULL    DEFAULT 1
        )
        '''
    )

    conn.commit()
    conn.close()

    log.info(f'Created sqlite3 table {table} in {db}')

    return


# Repository Methods
def add_reminder(userId, messageId, channelId, createdAt, remindAfter, remindMsg):
    return _add_reminder(userId, messageId, channelId, createdAt, remindAfter, remindMsg,
                         SQLITE3_DB_NAME, DB_TABLE_REMINDERS_NAME)


def _add_reminder(userId, messageId, channelId, createdAt, remindAfter, remindMsg, db, table):
    conn = sqlite3.connect(db)
    cursor = conn.execute(
        f'''
        INSERT INTO {table}
        (UserId, MessageId, ChannelId, CreatedAt, RemindAfter, RemindMsg, Active)
        Values (:userId, :messageId, :channelId, :createdAt, :remindAfter, :remindMsg, 1)
        ''',
        [userId, messageId, channelId, createdAt, remindAfter, remindMsg]
    )

    conn.commit()
    conn.close()

    return cursor.lastrowid


def unset_reminder(rowId):
    return _unset_reminder(rowId, SQLITE3_DB_NAME, DB_TABLE_REMINDERS_NAME)


def _unset_reminder(rowId, db, table):
    conn = sqlite3.connect(db)
    cursor = conn.execute(
        f'''
        UPDATE {table}
        SET Active = 0
        WHERE ROWID = :rowId
        ''', [rowId]
    )

    conn.commit()
    conn.close()

    return cursor.rowcount > 0


def get_reminders(where=None):
    return _get_reminders(SQLITE3_DB_NAME, DB_TABLE_REMINDERS_NAME, where)


def _get_reminders(db, table, where=None):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row

    cursor = conn.execute(
        f'''
        SELECT RowId, UserId, MessageId, ChannelId, CreatedAt, RemindAfter, RemindMsg, Active
        FROM {table}
        {'' if not where else where}
        '''
    )

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


# Maintenence Methods
def set_tables():
    _create_table_reminders(SQLITE3_DB_NAME)
