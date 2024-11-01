from conn import conn_op, conn_cl
import time

def insert_face(name, cam_n):
    fecha = time.strftime("%Y-%m-%d %H:%M:%S")
    my_con = conn_op()
    my_cursor = my_con.cursor()
    sql = "INSERT INTO registro (name, fecha, cam_n) VALUES(%s, %s, %s)"
    vals = (name, fecha, cam_n)
    my_cursor.execute(sql, vals)
    my_con.commit()
    my_con.close()