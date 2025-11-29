from sqlmodel import SQLModel, create_engine, Session
import os

# 取得專案根目錄（mediteasy 資料夾）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sqlite_file_name = os.path.join(BASE_DIR, "med-it-easy.db")
sqlite_url = f"sqlite:///{sqlite_file_name}"

# 輸出資料庫路徑（用於除錯）
print(f"[資料庫] 資料庫檔案路徑: {sqlite_file_name}")
print(f"[資料庫] 資料庫檔案存在: {os.path.exists(sqlite_file_name)}")

engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session