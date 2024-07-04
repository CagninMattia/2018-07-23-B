from database.DB_connect import DBConnect
from model.stato import Stato


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_vertici():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from state s 
                         """

        cursor.execute(query)

        for row in cursor:
            result.append(Stato(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_archi(anno, xg):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select n.state1 A, n.state2 B, count(*) as peso
                    from neighbor n, (select s.* from sighting s where YEAR(`datetime`) = %s) as s1, 
                    (select s.* from sighting s where YEAR(`datetime`) = %s) as s2
                    where n.state1 = s1.state and n.state2 = s2.state and datediff(s1.datetime, s2.datetime) < %s and n.state1 < n.state2 
                    group by A, B
                    """

        cursor.execute(query, (anno, anno, xg))

        for row in cursor:
            result.append([row["A"], row["B"], row["peso"]])

        cursor.close()
        conn.close()
        return result

