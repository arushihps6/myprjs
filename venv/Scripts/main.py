from db import create_connection, close_connection

def execute_query(connection, query, params):
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Query executed successfully")
    except Exception as e:
        print(f"The error '{e}' occurred")

def fetch_query(connection, query, params):
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"The error '{e}' occurred")
        return None

def main():
    connection = create_connection()
    
    if connection is None:
        return

    # Example query to fetch data from the 'empl' table where ename is 'BINA'
    fetch_empl_query = "SELECT * FROM empl WHERE ename = %s"
    empl_records = fetch_query(connection, fetch_empl_query, ('BINA',))

    if empl_records:
        for record in empl_records:
            print(record)
    
    close_connection(connection)

if __name__ == "__main__":
    main()
