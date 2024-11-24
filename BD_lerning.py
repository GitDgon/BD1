import psycopg2
conn = psycopg2.connect(dbname='BD1', user='users1',
                        password='', host='localhost')
cursor = conn.cursor()