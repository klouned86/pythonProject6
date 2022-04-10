import psycopg2


conn = psycopg2.connect(dbname='qa_ddl_24_9',
                        user='user_24_9',
                        password='123',
                        host='159.69.151.133',
                        port='5056')

cursor = conn.cursor()

# if conn:
#     print('connect is true')
#
#     select_query = 'select * from employees_9;'
#     select_query_2 = '''select * from employees_9;'''
#
#     ex_query = cursor.execute(select_query)
#     f_query = cursor.fetchall()
#     for i in f_query:
#
#         print('Number', i[0], 'Name', i[1])
#
#     conn.commit()
#     conn.close()

# if conn:
#     print('YES')
#     create_query = 'create table my_family('\
#                    'id serial primary key,'\
#                    'name varchar(30),'\
#                    'age int not null,'\
#                    'weight int not null,' \
#                    'salary int'\
#                    ')'
#     cursor.execute(create_query)
#
#     conn.commit()
#     conn.close()
'==============INSERT_INTO============================================================================='
for i in range(0, 10):
    if conn:
        print('YES')

        name = "'" + 'name_' + str(i) + "'"
        age = '3' + str(i)
        weight = str(85)
        salary = str(1000)

        q_values = name + ','\
                   + age + ','\
                   + weight + ','\
                   + salary
        print(q_values)

        create_insert = 'insert into public.my_family(name,'\
                        'age,'\
                        'weight,'\
                        'salary)'\
                        'values (' + name + ',' + age + ',' + weight + ',' + salary + ')'




        cursor.execute(create_insert)

        conn.commit()
conn.close()

'==================END==========================================================================='
