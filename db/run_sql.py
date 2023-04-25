import psycopg2
import psycopg2.extras as ext


def run_sql(sql, values = None):
    conn = None 
    results = []
    try:
        conn = psycopg2.connect(dbname='music_library')
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("HEY WE MESSED UP:", error)
    finally:
        if conn is not None:
            conn.close()

    # return some data
    #in Python form
    return results