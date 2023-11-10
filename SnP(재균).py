#로컬 파일 읽기
import pandas as pd

ownership = '/Users/jaekyunpark/Library/CloudStorage/OneDrive-경희대학교/JaekyunPark/S&P data/ownership.parquet'
professional = '/Users/jaekyunpark/Library/CloudStorage/OneDrive-경희대학교/JaekyunPark/S&P data/professional.parquet'
keydev = '/Users/jaekyunpark/Library/CloudStorage/OneDrive-경희대학교/JaekyunPark/S&P data/keydev.parquet'
exchangerate = '/Users/jaekyunpark/Library/CloudStorage/OneDrive-경희대학교/JaekyunPark/S&P data/exchangerate.parquet'
estimates = '/Users/jaekyunpark/Library/CloudStorage/OneDrive-경희대학교/JaekyunPark/S&P data/estimates.parquet'
company = '/Users/jaekyunpark/Library/CloudStorage/OneDrive-경희대학교/JaekyunPark/S&P data/company.parquet'
transcript = '/Users/jaekyunpark/Library/CloudStorage/OneDrive-경희대학교/JaekyunPark/S&P data/transcript.parquet'
financial = '/Users/jaekyunpark/Library/CloudStorage/OneDrive-경희대학교/JaekyunPark/S&P data/financials.parquet'
market = '/Users/jaekyunpark/Library/CloudStorage/OneDrive-경희대학교/JaekyunPark/S&P data/market.parquet'



#pd.read_parquet(ownership)
#pd.read_parquet(professional)
#pd.read_parquet(keydev)
#pd.read_parquet(exchangerate)
#pd.read_parquet(estimates)
pd.read_parquet(company)
#pd.read_parquet(transcript)
#pd.read_parquet(market)


# 현재 sql에 있는 테이블 목록을 보여줌
from sqlalchemy import create_engine

user = 'felab'
password = 'rlawkdgh'
host = '192.168.0.2'
port = 3306
database = 'db'

# 데이터베이스 엔진을 생성합니다.
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

# 엔진을 사용하여 데이터베이스 내의 모든 테이블 이름을 조회합니다.
table_list = engine.table_names()

# 테이블 리스트를 출력합니다.
print(table_list)




# sql에서 테이블을 읽어와서 pandas로 읽기
import pymysql
from sqlalchemy import create_engine
import pandas as pd

user = 'felab'
password = 'rlawkdgh'
host = '192.168.0.2'  # 포트 번호를 여기에 포함하지 않습니다.
port = 3306  # 포트 번호를 별도의 변수로 설정합니다.
database = 'db'
table_name = 'company' #읽고 싶은 데이터셋.

# SQLAlchemy 엔진 생성 시 호스트와 포트를 정확하게 지정합니다.
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

# pymysql 연결 시에도 마찬가지로 호스트와 포트를 정확하게 지정합니다.
connection = pymysql.connect(host=host, port=port, user=user, password=password, database=database)

query = f"SELECT simpleIndustryDescription FROM {table_name}" # 원하는 쿼리. SQL 지식 필요함
df = pd.read_sql(query, engine)
df



# company.parquet에서 tickerSymbol과 simpleIndustryDescription만 뽑아내기
import pandas as pd

company_path = '/Users/jaekyunpark/Library/CloudStorage/OneDrive-경희대학교/JaekyunPark/S&P data/company.parquet'
company_df = pd.read_parquet(company_path)

#비상장사 제거
filtered_company_df = company_df[company_df['tickerSymbol'].notnull()]

selected_columns = filtered_company_df[['tickerSymbol', 'simpleIndustryDescription']]

print(selected_columns)


# 산업군 수 파악
unique_industry_count = filtered_company_df['simpleIndustryDescription'].nunique()

print(unique_industry_count)



#산업군 종류 파악
unique_industries = filtered_company_df['simpleIndustryDescription'].unique()

print(unique_industries)



#산업군별 회사 수 시각화

import matplotlib.pyplot as plt

industry_counts = filtered_company_df['simpleIndustryDescription'].value_counts()

# Plotting
plt.figure(figsize=(10, 8))  
industry_counts.plot(kind='bar')
plt.title('Number of Companies per Industry Group')
plt.xlabel('Industry Group')
plt.ylabel('Number of Companies')
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()
