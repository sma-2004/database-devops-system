import os
import datetime

BACKUP_DIR = "backups"
os.makedirs(BACKUP_DIR, exist_ok=True)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# PostgreSQL backup
def backup_postgres():
    filename = f"{BACKUP_DIR}/pg_backup_{timestamp}.sql"
    cmd = f"pg_dump -U postgres -h localhost mydb > {filename}"
    os.system(cmd)
    print(f"PostgreSQL backup saved: {filename}")

# MySQL backup
def backup_mysql():
    filename = f"{BACKUP_DIR}/mysql_backup_{timestamp}.sql"
    cmd = f"mysqldump -u root -p password mydb > {filename}"
    os.system(cmd)
    print(f"MySQL backup saved: {filename}")

if __name__ == "__main__":
    backup_postgres()
    backup_mysql()