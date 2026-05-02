import os

def restore_postgres(file):
    cmd = f"psql -U postgres -d mydb < {file}"
    os.system(cmd)
    print("PostgreSQL restored")

def restore_mysql(file):
    cmd = f"mysql -u root -p password mydb < {file}"
    os.system(cmd)
    print("MySQL restored")

if __name__ == "__main__":
    file = input("Enter backup file path: ")
    db = input("Enter db type (pg/mysql): ")

    if db == "pg":
        restore_postgres(file)
    else:
        restore_mysql(file)