#%%
# !pip install openpyxl
import pandas as pd

lst01 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTU',
         'JNJ', 'PFE', 'MRK', 'ABBV', 'TMO',
         'JPM', 'BAC', 'C', 'GS', 'MS',
         'AMZN', 'TSLA', 'NKE', 'MCD', 'SBUX',
         'PG', 'KO', 'PEP', 'WMT', 'COST',
         'MMM', 'HON', 'GE', 'CAT', 'LMT',
         'XOM', 'CVX', 'SLB', 'COP', 'EOG',
         'NEE', 'DUK', 'SO', 'AEP', 'XEL',
         'GOOGL', 'FB', 'DIS', 'VZ', 'T',
         'AMT', 'SPG', 'CCI', 'PLD', 'WY']
df01 = pd.DataFrame(lst01)
df01.to_excel('df01.xlsx', index=False)
# %%
lst02 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'ORCL',
         'JNJ', 'PFE', 'UNH', 'ABBV', 'MDT',
         'AMZN', 'TSLA', 'NKE', 'HD', 'MCD',
         'PG', 'KO', 'PEP', 'COST', 'WMT',
         'JPM', 'BAC', 'WFC', 'C', 'GS',
         'MMM', 'GE', 'UPS', 'HON', 'CAT',
         'XOM', 'CVX', 'COP', 'SLB', 'EOG',
         'NEE', 'DUK', 'SO', 'AEP', 'XEL',
         'GOOGL', 'FB', 'VZ', 'T', 'CMCSA',
         'AMT', 'SPG', 'O', 'WELL', 'VTR']
df02 = pd.DataFrame(lst02)
df02.to_excel('df02.xlsx', index=False)
# %%
lst03 = ['AAPL', 'MSFT', 'NVDA', 'INTC', 'AMD', 'CSCO', 'ORCL', 'IBM', 'QCOM',
         'JNJ', 'PFE', 'UNH', 'ABBV', 'MRK',
         'JPM', 'BAC', 'WFC', 'C', 'GS',
         'AMZN', 'HD', 'MCD', 'NKE', 'SBUX',
         'PG', 'KO', 'PEP', 'WMT', 'COST',
         'GE', 'MMM', 'HON', 'CAT', 'UPS',
         'XOM', 'CVX', 'COP',
         'NEE', 'DUK', 'SO',
         'AMT', 'SPG', 'WELL',
         'GOOGL', 'FB']
df03 = pd.DataFrame(lst03)
df03.to_excel('df03.xlsx', index=False)
# %%
lst04 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTC', 'CRM', 'ORCL', 'ADBE', 'CSCO',
         'JNJ', 'PFE', 'UNH', 'ABBV', 'MRK', 'TMO',
         'JPM', 'BAC', 'WFC', 'C', 'GS', 'BLK',
         'AMZN', 'TSLA', 'HD', 'NKE', 'SBUX',
         'GE', 'MMM', 'BA', 'CAT', 'HON',
         'XOM', 'CVX', 'SLB',
         'NEE', 'D', 'SO',
         'PG', 'KO', 'PEP',
         'GOOGL', 'FB', 'VZ',
         'AMT', 'SPG']
df04 = pd.DataFrame(lst04)
df04.to_excel('df04.xlsx', index=False)
# %%
lst05 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTC', 'CSCO', 'ORCL', 'ADBE', 'QCOM',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV',
         'JPM', 'BAC', 'WFC', 'C', 'GS',
         'AMZN', 'TSLA', 'HD', 'MCD', 'NKE',
         'BA', 'MMM', 'HON', 'GE', 'CAT',
         'XOM', 'CVX', 'SLB',
         'PG', 'KO', 'PEP', 'WMT',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'T',
         'AMT', 'SPG', 'CCI']
df05 = pd.DataFrame(lst05)
df05.to_excel('df05.xlsx', index=False)
# %%
lst06 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTU',
         'JNJ', 'PFE', 'UNH', 'ABT', 'MRK',
         'AMZN', 'TSLA', 'HD', 'NKE', 'SBUX',
         'PG', 'KO', 'PEP', 'COST', 'WMT',
         'JPM', 'BAC', 'C', 'GS', 'MS',
         'MMM', 'HON', 'UNP', 'CAT', 'GE',
         'XOM', 'CVX', 'COP', 'PSX', 'SLB',
         'NEE', 'DUK', 'SO', 'AEP', 'XEL',
         'GOOGL', 'FB', 'VZ', 'CMCSA', 'T',
         'AMT', 'SPG', 'CCI', 'WELL', 'O']
df06 = pd.DataFrame(lst06)
df06.to_excel('df06.xlsx', index=False)
# %%
lst07 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTU', 'QCOM', 'CRM', 'ORCL', 'ADP',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'AMGN', 'GILD', 'SYK',
         'JPM', 'BAC', 'WFC', 'C', 'GS', 'AXP',
         'AMZN', 'HD', 'NKE', 'TJX', 'GM',
         'PG', 'KO', 'PEP', 'COST',
         'MMM', 'GE', 'HON', 'UPS',
         'XOM', 'CVX', 'COP',
         'NEE', 'D', 'SO',
         'GOOGL', 'FB', 'T']
df07 = pd.DataFrame(lst07)
df07.to_excel('df07.xlsx', index=False)
# %%
lst08 = ['AAPL', 'MSFT', 'NVDA', 'INTC', 'AMD', 'CRM', 'ORCL', 'ADP', 'PAYX',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'TMO', 'AMGN', 'BDX',
         'JPM', 'BAC', 'C', 'GS', 'AXP', 'SCHW',
         'AMZN', 'HD', 'NKE', 'LOW', 'TGT',
         'PG', 'KO', 'PEP', 'WMT',
         'MMM', 'GE', 'UPS', 'CAT',
         'XOM', 'CVX', 'SLB',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'VZ']
df08 = pd.DataFrame(lst08)
df08.to_excel('df08.xlsx', index=False)
# %%
lst09 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTU', 'QCOM', 'ADP', 'ORCL', 'CSCO',
         'JNJ', 'PFE', 'UNH', 'ABT', 'MRK', 'AMGN', 'GILD', 'BDX',
         'JPM', 'BAC', 'C', 'GS', 'AXP', 'MS',
         'AMZN', 'HD', 'MCD', 'NKE', 'TGT',
         'PG', 'KO', 'WMT', 'COST',
         'MMM', 'HON', 'CAT', 'GE',
         'XOM', 'CVX', 'COP',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'VZ']
df09 = pd.DataFrame(lst09)
df09.to_excel('df09.xlsx', index=False)
# %%
lst10 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTU', 'CRM', 'ADBE', 'ORCL', 'CSCO',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'AMGN', 'GILD', 'TMO',
         'JPM', 'BAC', 'C', 'GS', 'MS', 'AXP',
         'AMZN', 'HD', 'MCD', 'NKE', 'LOW',
         'PG', 'KO', 'PEP', 'WMT',
         'MMM', 'HON', 'GE', 'CAT',
         'XOM', 'CVX', 'SLB',
         'NEE', 'D', 'SO',
         'GOOGL', 'FB', 'VZ']
df10 = pd.DataFrame(lst10)
df10.to_excel('df10.xlsx', index=False)

# %%
lst11 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTU', 'CRM', 'ORCL', 'ADP', 'CSCO',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'AMGN', 'GILD', 'BDX',
         'JPM', 'BAC', 'C', 'GS', 'AXP', 'MS',
         'AMZN', 'HD', 'NKE', 'TGT', 'LOW',
         'PG', 'KO', 'PEP', 'WMT',
         'MMM', 'HON', 'CAT', 'GE',
         'XOM', 'CVX', 'SLB',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'VZ']
df11 = pd.DataFrame(lst11)
df11.to_excel('df11.xlsx', index=False)

# %%
lst12 = ['AAPL', 'MSFT', 'NVDA', 'INTC', 'AMD', 'CRM', 'ORCL', 'ADP', 'SQ',
         'JNJ', 'PFE', 'UNH', 'ABBV', 'MRK', 'TMO', 'AMGN', 'SYK',
         'JPM', 'BAC', 'C', 'GS', 'AXP', 'SCHW',
         'AMZN', 'HD', 'NKE', 'GM', 'TGT',
         'PG', 'KO', 'PEP', 'COST',
         'GE', 'MMM', 'HON', 'CAT',
         'XOM', 'CVX', 'SLB',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'VZ']
df12 = pd.DataFrame(lst12)
df12.to_excel('df12.xlsx', index=False)
# %%
lst13 = ['AAPL', 'MSFT', 'NVDA', 'INTC', 'AMD', 'CRM', 'ORCL', 'ADP', 'SQ',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'AMGN', 'GILD', 'SYK',
         'JPM', 'BAC', 'C', 'GS', 'AXP', 'SCHW',
         'AMZN', 'HD', 'NKE', 'GM', 'TGT',
         'PG', 'KO', 'PEP', 'COST',
         'MMM', 'HON', 'CAT', 'GE',
         'XOM', 'CVX', 'SLB',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'VZ']
df13 = pd.DataFrame(lst13)
df13.to_excel('df13.xlsx', index=False)
# %%
lst14 = ['AAPL', 'MSFT', 'NVDA', 'INTC', 'AMD', 'CRM', 'ORCL', 'ADP', 'SQ',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'AMGN', 'GILD', 'SYK',
         'JPM', 'BAC', 'C', 'GS', 'AXP', 'SCHW',
         'AMZN', 'HD', 'NKE', 'GM', 'TGT',
         'PG', 'KO', 'PEP', 'COST',
         'MMM', 'HON', 'CAT', 'GE',
         'XOM', 'CVX', 'SLB',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'VZ']
df14 = pd.DataFrame(lst14)
df14.to_excel('df14.xlsx', index=False)
# %%
lst15 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTU', 'CRM', 'ORCL', 'ADP', 'CSCO',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'AMGN', 'GILD', 'BDX',
         'JPM', 'BAC', 'C', 'GS', 'AXP', 'MS',
         'AMZN', 'HD', 'NKE', 'GM', 'TGT',
         'PG', 'KO', 'PEP', 'WMT',
         'MMM', 'HON', 'CAT', 'GE',
         'XOM', 'CVX', 'SLB',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'VZ']
df15 = pd.DataFrame(lst15)
df15.to_excel('df15.xlsx', index=False)
# %%
lst16 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTC', 'CRM', 'ORCL', 'ADP', 'CSCO',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'AMGN', 'GILD', 'BDX',
         'JPM', 'BAC', 'C', 'GS', 'AXP', 'MS',
         'AMZN', 'HD', 'NKE', 'GM', 'TGT',
         'PG', 'KO', 'PEP', 'WMT',
         'MMM', 'HON', 'CAT', 'GE',
         'XOM', 'CVX', 'SLB',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'VZ']
df16 = pd.DataFrame(lst16)
df16.to_excel('df16.xlsx', index=False)
# %%
lst18 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTC', 'CRM', 'ORCL', 'ADP', 'CSCO',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'AMGN', 'GILD', 'BDX',
         'JPM', 'BAC', 'C', 'GS', 'AXP', 'MS',
         'AMZN', 'HD', 'NKE', 'GM', 'TGT',
         'PG', 'KO', 'PEP', 'WMT',
         'MMM', 'HON', 'CAT', 'GE',
         'XOM', 'CVX', 'SLB',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'VZ']
df18 = pd.DataFrame(lst18)
df18.to_excel('df18.xlsx', index=False)
# %%
lst19 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTU',
         'JNJ', 'PFE', 'MRK', 'ABT', 'TMO',
         'PG', 'KO', 'PEP', 'NKE', 'EL',
         'JPM', 'BAC', 'GS', 'MS', 'AXP',
         'XOM', 'CVX', 'COP', 'PSX', 'EOG',
         'MMM', 'GE', 'HON', 'CAT', 'DE',
         'GOOGL', 'FB', 'NFLX', 'T', 'VZ',
         'AMZN', 'TSLA', 'MCD', 'HD', 'LVMUY',
         'DUK', 'SO', 'SPG', 'AMT', 'PLD']
df19 = pd.DataFrame(lst19)
df19.to_excel('df19.xlsx', index=False)
# %%
lst20 = ['AAPL', 'MSFT', 'NVDA', 'ADBE', 'CRM',
         'JNJ', 'PFE', 'MRK', 'ABBV', 'AMGN',
         'AMZN', 'TSLA', 'HD', 'NKE', 'LOW',
         'JPM', 'BAC', 'BRK.B', 'V', 'MA',
         'GOOGL', 'FB', 'CMCSA', 'VZ', 'T',
         'BA', 'HON', 'MMM', 'CAT', 'UNP',
         'PG', 'KO', 'PEP', 'WMT', 'COST',
         'XOM', 'CVX', 'SLB', 'COP', 'EOG',
         'NEE', 'DUK', 'SO', 'D', 'EXC',
         'AMT', 'SPG', 'PLD', 'CCI', 'EQIX']
df20 = pd.DataFrame(lst20)
df20.to_excel('df20.xlsx', index=False)
# %%
lst21 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTC', 'CRM', 'ORCL', 'ADP', 'CSCO',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'AMGN', 'GILD', 'BDX',
         'JPM', 'BAC', 'C', 'GS', 'AXP', 'MS',
         'AMZN', 'HD', 'NKE', 'GM', 'TGT',
         'PG', 'KO', 'PEP', 'WMT',
         'MMM', 'HON', 'CAT', 'GE',
         'XOM', 'CVX', 'SLB',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'VZ']
df21 = pd.DataFrame(lst21)
df21.to_excel('df21.xlsx', index=False)
# %%
lst22 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTC', 'CRM', 'ORCL', 'ADP', 'CSCO',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'AMGN', 'GILD', 'BDX',
         'JPM', 'BAC', 'C', 'GS', 'AXP', 'MS',
         'AMZN', 'HD', 'NKE', 'GM', 'TGT',
         'PG', 'KO', 'PEP', 'WMT',
         'MMM', 'HON', 'CAT', 'GE',
         'XOM', 'CVX', 'SLB',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'VZ']
df22 = pd.DataFrame(lst22)
df22.to_excel('df22.xlsx', index=False)
# %%
lst23 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTC', 'CRM', 'ORCL', 'ADP', 'CSCO',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'AMGN', 'GILD', 'BDX',
         'JPM', 'BAC', 'C', 'GS', 'AXP', 'MS',
         'AMZN', 'HD', 'NKE', 'GM', 'TGT',
         'PG', 'KO', 'PEP', 'WMT',
         'MMM', 'HON', 'CAT', 'GE',
         'XOM', 'CVX', 'SLB',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'VZ']
df23 = pd.DataFrame(lst23)
df23.to_excel('df23.xlsx', index=False)
# %%
lst24 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTC', 'CRM', 'ORCL', 'ADP', 'CSCO',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'AMGN', 'GILD', 'BDX',
         'JPM', 'BAC', 'C', 'GS', 'AXP', 'MS',
         'AMZN', 'HD', 'NKE', 'GM', 'TGT',
         'PG', 'KO', 'PEP', 'WMT',
         'MMM', 'HON', 'CAT', 'GE',
         'XOM', 'CVX', 'SLB',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'VZ']
df24 = pd.DataFrame(lst24)
df24.to_excel('df24.xlsx', index=False)
# %%
lst25 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTC', 'CRM', 'ORCL', 'ADP', 'CSCO',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'AMGN', 'GILD', 'BDX',
         'JPM', 'BAC', 'C', 'GS', 'AXP', 'MS',
         'AMZN', 'HD', 'NKE', 'GM', 'TGT',
         'PG', 'KO', 'PEP', 'WMT',
         'MMM', 'HON', 'CAT', 'GE',
         'XOM', 'CVX', 'SLB',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'VZ']
df25 = pd.DataFrame(lst25)
df25.to_excel('df25.xlsx', index=False)
# %%
lst26 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTC', 'CRM', 'ORCL', 'ADP', 'CSCO',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'AMGN', 'GILD', 'BDX',
         'JPM', 'BAC', 'C', 'GS', 'AXP', 'MS',
         'AMZN', 'HD', 'NKE', 'GM', 'TGT',
         'PG', 'KO', 'PEP', 'WMT',
         'MMM', 'HON', 'CAT', 'GE',
         'XOM', 'CVX', 'SLB',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'VZ']
df26 = pd.DataFrame(lst26)
df26.to_excel('df26.xlsx', index=False)
# %%
lst27 = ['AAPL', 'MSFT', 'NVDA', 'AMD', 'INTC', 'CRM', 'ORCL', 'ADP', 'CSCO',
         'JNJ', 'PFE', 'UNH', 'MRK', 'ABBV', 'AMGN', 'GILD', 'BDX',
         'JPM', 'BAC', 'C', 'GS', 'AXP', 'MS',
         'AMZN', 'HD', 'NKE', 'GM', 'TGT',
         'PG', 'KO', 'PEP', 'WMT',
         'MMM', 'HON', 'CAT', 'GE',
         'XOM', 'CVX', 'SLB',
         'NEE', 'DUK', 'SO',
         'GOOGL', 'FB', 'VZ']
df27 = pd.DataFrame(lst27)
df27.to_excel('df27.xlsx', index=False)
# %%
lst28 = [
    # Technology
    "AAPL", "MSFT", "NVDA", "AMD", "INTU",
    # Healthcare
    "JNJ", "PFE", "UNH", "ABBV", "TMO",
    # Finance
    "JPM", "BAC", "C", "GS", "MS",
    # Consumer Goods
    "PG", "KO", "PEP", "NKE", "EL",
    # Energy
    "XOM", "CVX", "SLB", "COP", "EOG",
    # Industrials
    "MMM", "GE", "HON", "CAT", "DE",
    # Utilities
    "NEE", "DUK", "SO", "AEP", "EXC",
    # Communication Services
    "GOOGL", "FB", "T", "VZ", "CMCSA",
    # Materials
    "LIN", "ECL", "SHW", "NEM", "APD",
    # Real Estate
    "AMT", "SPG", "CCI", "PLD", "WELL"]
df28 = pd.DataFrame(lst28)
df28.to_excel('df28.xlsx', index=False)
# %%
lst29 = [
    # Technology
    "AAPL", "MSFT", "NVDA", "AMD", "INTU",
    # Healthcare
    "JNJ", "PFE", "UNH", "ABBV", "TMO",
    # Financials
    "JPM", "BAC", "C", "GS", "MS",
    # Consumer Discretionary
    "AMZN", "TSLA", "NKE", "HD", "SBUX",
    # Consumer Staples
    "PG", "KO", "PEP", "WMT", "COST",
    # Industrials
    "GE", "MMM", "HON", "CAT", "DE",
    # Energy
    "XOM", "CVX", "SLB", "COP", "PSX",
    # Utilities
    "NEE", "DUK", "SO", "AEP", "EXC",
    # Communication Services
    "GOOGL", "FB", "VZ", "T", "CMCSA"
]
df29 = pd.DataFrame(lst29)
df29.to_excel('df29.xlsx', index=False)
# %%
lst30 = [
    # Technology
    "AAPL", "MSFT", "NVDA", "AMD", "CRM",
    # Healthcare
    "JNJ", "PFE", "UNH", "MRK", "ABBV",
    # Financials
    "JPM", "BAC", "GS", "C", "MS",
    # Consumer Discretionary
    "AMZN", "TSLA", "NKE", "MCD", "SBUX",
    # Consumer Staples
    "PG", "KO", "PEP", "WMT", "COST",
    # Industrials
    "BA", "MMM", "HON", "CAT", "DE",
    # Energy
    "XOM", "CVX", "SLB", "COP", "KMI",
    # Utilities
    "NEE", "DUK", "SO", "AEP", "EXC",
    # Communication Services
    "GOOGL", "FB", "DIS", "VZ", "CMCSA"
]
df30 = pd.DataFrame(lst30)
df30.to_excel('df30.xlsx', index=False)
# %%
lst31 = [
    # Technology
    "AAPL", "MSFT", "NVDA", "AMD", "INTC",
    # Healthcare
    "JNJ", "PFE", "UNH", "ABBV", "MRK",
    # Financials
    "JPM", "BAC", "C", "GS", "MS",
    # Consumer Discretionary
    "AMZN", "TSLA", "NKE", "MCD", "SBUX",
    # Consumer Staples
    "PG", "KO", "PEP", "WMT", "COST",
    # Industrials
    "BA", "MMM", "HON", "CAT", "GE",
    # Energy
    "XOM", "CVX", "SLB", "COP", "KMI",
    # Utilities
    "NEE", "DUK", "SO", "AEP", "EXC",
    # Communication Services
    "GOOGL", "FB", "DIS", "VZ", "CMCSA"
]
df31 = pd.DataFrame(lst31)
df31.to_excel('df31.xlsx', index=False)
# %%
# 티커 빈도수 확인
import pandas as pd

# Load the Excel file
file_path = './45개 자산 티커.xlsx'
data = pd.read_excel(file_path)

# Assuming each column in the file represents a different list of tickers
# We will concatenate all the columns into a single series and then count the frequency of each ticker
all_tickers = pd.concat([data[col] for col in data.columns]).dropna()
ticker_frequency = all_tickers.value_counts()

# Display the ticker frequencies
ticker_frequency.to_excel('./45stocks_freq_JY.xlsx')
# %%
