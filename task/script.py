import json

import psycopg2
f = open("../media/data.json", 'r')
data = json.load(f)
for i in data:
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="root",
                                      host="localhost",
                                      port="5432",
                                      database="tvf")
        cursor = connection.cursor()
        postgres_insert_query = """INSERT INTO task_user_data (ID, first_name, last_name, company_name,
            age, city, state, zip, email, web) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """
        record_to_insert = (
            i["id"], str(i["first_name"]), str(i["last_name"]), str(i["company_name"]), i["age"], str(i["city"]), str(i["state"]), str(i["zip"]),
            str(i["email"]), str(i["web"]))
        print(record_to_insert)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into Category table", error)
