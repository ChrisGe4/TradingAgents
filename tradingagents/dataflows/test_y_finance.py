import yfinance as yf

ticker_obj = yf.Ticker('AAPL')
# historical_data = ticker_obj.history(period="1y")  # data for the last year
# data = ticker_obj.info
# print("\nInfo:")
# print(data)
# data = ticker_obj.actions
# print("\nActions:")
# print(data)
# data = ticker_obj.analyst_price_targets
# print("\nAnalyst Price Targets:")
# print(data)
# data = ticker_obj.cash_flow
# print("\nCash_Flow:")
# print(data)
# data = ticker_obj.cashflow
# print("\nCash Flow:")
# print(data)
# data = ticker_obj.balance_sheet
# print("\nBalance Sheet:")
# print(data)
# data = ticker_obj.balancesheet
# print("\nBalance Sheet:")
# print(data)
# data = ticker_obj.earnings_history
# print("\nEarnings History:")
# print(data)
# data = ticker_obj.eps_trend
# print("\nEPS Trend:")
# print(data)
# data = ticker_obj.financials
# print("\nFinancials:")
# print(data)
data = ticker_obj.get_income_stmt(pretty=True, freq='quarterly')
print("\nIncome Statement:")
print(data)
data = ticker_obj.get_balance_sheet(pretty=True, freq='quarterly')
print("\nBalance Sheet:")
print(data)
data = ticker_obj.get_cashflow(pretty=True, freq='quarterly')
print("\nCash Flow:")
print(data)
data = ticker_obj.get_info()
print("\nInfo:")
print(data)

data = ticker_obj.get_eps_trend()
print("\nEPS Trend:")
print(data)
data = ticker_obj.get_dividends()
print("\nDividends:")
print(data)
data = ticker_obj.get_earnings_history()
print("\nEarnings History:")
print(data)

data = ticker_obj.get_recommendations()
print("\nRecommendations:")
print(data)
data = ticker_obj.get_upgrades_downgrades()
print("\nUpgrades/Downgrades:")
print(data)
data = ticker_obj.get_sec_filings()
print("\nSEC Filings:")
print(data)
data = ticker_obj.get_analyst_price_targets()
print("\nAnalyst Price Targets:")
print(data)
data = ticker_obj.get_growth_estimates()
print("\nGrowth Estimates:")
print(data)
data = ticker_obj.quarterly_cashflow
print("\nQuarterly Cash Flow:")
print(data)
data = ticker_obj.get_insider_purchases()
print("\nInsider Purchases:")
print(data)
data = ticker_obj.get_insider_transactions()
print("\nInsider Sales:")
print(data)

{'address1': 'One Apple Park Way', 'city': 'Cupertino', 'state': 'CA',
 'zip': '95014', 'country': 'United States', 'phone': '(408) 996-1010',
 'website': 'https://www.apple.com', 'industry': 'Consumer Electronics',
 'industryKey': 'consumer-electronics', 'industryDisp': 'Consumer Electronics',
 'sector': 'Technology', 'sectorKey': 'technology', 'sectorDisp': 'Technology',
 'longBusinessSummary': 'Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. The company offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, a line of multi-purpose tablets; and wearables, home, and accessories comprising AirPods, Apple Vision Pro, Apple TV, Apple Watch, Beats products, and HomePod, as well as Apple branded and third-party accessories. It also provides AppleCare support and cloud services; and operates various platforms, including the App Store that allow customers to discover and download applications and digital content, such as books, music, video, games, and podcasts, as well as advertising services include third-party licensing arrangements and its own advertising platforms. In addition, the company offers various subscription-based services, such as Apple Arcade, a game subscription service; Apple Fitness+, a personalized fitness service; Apple Music, which offers users a curated listening experience with on-demand radio stations; Apple News+, a subscription news and magazine service; Apple TV, which offers exclusive original content and live sports; Apple Card, a co-branded credit card; and Apple Pay, a cashless payment service, as well as licenses its intellectual property. The company serves consumers, and small and mid-sized businesses; and the education, enterprise, and government markets. It distributes third-party applications for its products through the App Store. The company also sells its products through its retail and online stores, and direct sales force; and third-party cellular network carriers and resellers. The company was formerly known as Apple Computer, Inc. and changed its name to Apple Inc. in January 2007. Apple Inc. was founded in 1976 and is headquartered in Cupertino, California.',
 'fullTimeEmployees': 166000, 'companyOfficers': [
    {'maxAge': 1, 'name': 'Mr. Timothy D. Cook', 'age': 64,
     'title': 'CEO & Director', 'yearBorn': 1961, 'fiscalYear': 2025,
     'totalPay': 16759518, 'exercisedValue': 0, 'unexercisedValue': 0},
    {'maxAge': 1, 'name': 'Mr. Kevan  Parekh', 'age': 53,
     'title': 'Senior VP & CFO', 'yearBorn': 1972, 'fiscalYear': 2025,
     'totalPay': 4034174, 'exercisedValue': 0, 'unexercisedValue': 0},
    {'maxAge': 1, 'name': 'Mr. Sabih  Khan', 'age': 58,
     'title': 'Senior VP & Chief Operating Officer', 'yearBorn': 1967,
     'fiscalYear': 2025, 'totalPay': 5021905, 'exercisedValue': 0,
     'unexercisedValue': 0},
    {'maxAge': 1, 'name': 'Ms. Katherine L. Adams', 'age': 61,
     'title': 'Senior VP, General Counsel & Secretary', 'yearBorn': 1964,
     'fiscalYear': 2025, 'totalPay': 5022482, 'exercisedValue': 0,
     'unexercisedValue': 0},
    {'maxAge': 1, 'name': "Ms. Deirdre  O'Brien", 'age': 58,
     'title': 'Senior Vice President of Retail & People', 'yearBorn': 1967,
     'fiscalYear': 2025, 'totalPay': 5037867, 'exercisedValue': 0,
     'unexercisedValue': 0},
    {'maxAge': 1, 'name': 'Mr. Ben  Borders', 'age': 44,
     'title': 'Principal Accounting Officer', 'yearBorn': 1981,
     'fiscalYear': 2025, 'exercisedValue': 0, 'unexercisedValue': 0},
    {'maxAge': 1, 'name': 'Suhasini  Chandramouli',
     'title': 'Director of Investor Relations', 'fiscalYear': 2025,
     'exercisedValue': 0, 'unexercisedValue': 0},
    {'maxAge': 1, 'name': 'Ms. Kristin Huguet Quayle',
     'title': 'Vice President of Worldwide Communications', 'fiscalYear': 2025,
     'exercisedValue': 0, 'unexercisedValue': 0},
    {'maxAge': 1, 'name': 'Mr. Greg  Joswiak',
     'title': 'Senior Vice President of Worldwide Marketing',
     'fiscalYear': 2025, 'exercisedValue': 0, 'unexercisedValue': 0},
    {'maxAge': 1, 'name': 'Mr. Adrian  Perica', 'age': 51,
     'title': 'Vice President of Corporate Development', 'yearBorn': 1974,
     'fiscalYear': 2025, 'exercisedValue': 0, 'unexercisedValue': 0}],
 'auditRisk': 7, 'boardRisk': 1, 'compensationRisk': 3,
 'shareHolderRightsRisk': 1, 'overallRisk': 1,
 'governanceEpochDate': 1768176000, 'compensationAsOfEpochDate': 1767139200,
 'irWebsite': 'http://investor.apple.com/', 'executiveTeam': [],
 'maxAge': 86400, 'priceHint': 2, 'previousClose': 247.65, 'open': 249.2,
 'dayLow': 248.385, 'dayHigh': 250.7799, 'regularMarketPreviousClose': 247.65,
 'regularMarketOpen': 249.2, 'regularMarketDayLow': 248.385,
 'regularMarketDayHigh': 250.7799, 'dividendRate': 1.04, 'dividendYield': 0.42,
 'exDividendDate': 1762732800, 'payoutRatio': 0.1367,
 'fiveYearAvgDividendYield': 0.52, 'beta': 1.093, 'trailingPE': 33.584835,
 'forwardPE': 27.365784, 'volume': 17390279, 'regularMarketVolume': 17390279,
 'averageVolume': 46204940, 'averageVolume10days': 51598510,
 'averageDailyVolume10Day': 51598510, 'bid': 249.12, 'ask': 251.97,
 'bidSize': 3, 'askSize': 4, 'marketCap': 3697146855424,
 'fiftyTwoWeekLow': 169.21, 'fiftyTwoWeekHigh': 288.62, 'allTimeHigh': 288.62,
 'allTimeLow': 0.049107, 'priceToSalesTrailing12Months': 8.883934,
 'fiftyDayAverage': 270.5986, 'twoHundredDayAverage': 234.3916,
 'trailingAnnualDividendRate': 1.02, 'trailingAnnualDividendYield': 0.004118716,
 'currency': 'USD', 'tradeable': False, 'enterpriseValue': 3717043847168,
 'profitMargins': 0.26915002, 'floatShares': 14750346619,
 'sharesOutstanding': 14697926000, 'sharesShort': 112732788,
 'sharesShortPriorMonth': 129458559, 'sharesShortPreviousMonthDate': 1764288000,
 'dateShortInterest': 1767139200, 'sharesPercentSharesOut': 0.0076,
 'heldPercentInsiders': 0.017029999, 'heldPercentInstitutions': 0.6482,
 'shortRatio': 2.68, 'shortPercentOfFloat': 0.0076,
 'impliedSharesOutstanding': 14776353000, 'bookValue': 4.991,
 'priceToBook': 50.131634, 'lastFiscalYearEnd': 1758931200,
 'nextFiscalYearEnd': 1790467200, 'mostRecentQuarter': 1758931200,
 'earningsQuarterlyGrowth': 0.864, 'netIncomeToCommon': 112010002432,
 'trailingEps': 7.45, 'forwardEps': 9.14306, 'lastSplitFactor': '4:1',
 'lastSplitDate': 1598832000, 'enterpriseToRevenue': 8.932,
 'enterpriseToEbitda': 25.679, '52WeekChange': 0.10726106,
 'SandP52WeekChange': 0.123704195, 'lastDividendValue': 0.26,
 'lastDividendDate': 1762732800, 'quoteType': 'EQUITY', 'currentPrice': 250.207,
 'targetHighPrice': 350.0, 'targetLowPrice': 205.0,
 'targetMeanPrice': 287.21902, 'targetMedianPrice': 300.0,
 'recommendationMean': 2.0, 'recommendationKey': 'buy',
 'numberOfAnalystOpinions': 41, 'totalCash': 54697000960,
 'totalCashPerShare': 3.702, 'ebitda': 144748003328, 'totalDebt': 112377004032,
 'quickRatio': 0.771, 'currentRatio': 0.893, 'totalRevenue': 416161005568,
 'debtToEquity': 152.411, 'revenuePerShare': 27.84, 'returnOnAssets': 0.22964,
 'returnOnEquity': 1.7142199, 'grossProfits': 195201007616,
 'freeCashflow': 78862254080, 'operatingCashflow': 111482003456,
 'earningsGrowth': 0.912, 'revenueGrowth': 0.079, 'grossMargins': 0.46905,
 'ebitdaMargins': 0.34782, 'operatingMargins': 0.31647,
 'financialCurrency': 'USD', 'symbol': 'AAPL', 'language': 'en-US',
 'region': 'US', 'typeDisp': 'Equity',
 'quoteSourceName': 'Nasdaq Real Time Price', 'triggerable': True,
 'customPriceAlertConfidence': 'HIGH', 'shortName': 'Apple Inc.',
 'longName': 'Apple Inc.', 'corporateActions': [],
 'regularMarketTime': 1769104049, 'exchange': 'NMS',
 'messageBoardId': 'finmb_24937', 'exchangeTimezoneName': 'America/New_York',
 'exchangeTimezoneShortName': 'EST', 'gmtOffSetMilliseconds': -18000000,
 'market': 'us_market', 'esgPopulated': False,
 'regularMarketChangePercent': 1.0325084, 'regularMarketPrice': 250.207,
 'averageDailyVolume3Month': 46204940, 'fiftyTwoWeekLowChange': 80.996994,
 'fiftyTwoWeekLowChangePercent': 0.47867733,
 'fiftyTwoWeekRange': '169.21 - 288.62', 'fiftyTwoWeekHighChange': -38.412994,
 'fiftyTwoWeekHighChangePercent': -0.13309194,
 'fiftyTwoWeekChangePercent': 10.726107, 'dividendDate': 1762992000,
 'earningsTimestamp': 1769720400, 'earningsTimestampStart': 1769720400,
 'earningsTimestampEnd': 1769720400, 'earningsCallTimestampStart': 1769724000,
 'earningsCallTimestampEnd': 1769724000, 'isEarningsDateEstimate': False,
 'epsTrailingTwelveMonths': 7.45, 'epsForward': 9.14306,
 'epsCurrentYear': 8.24255, 'priceEpsCurrentYear': 30.355534,
 'fiftyDayAverageChange': -20.391602,
 'fiftyDayAverageChangePercent': -0.07535738,
 'twoHundredDayAverageChange': 15.815399,
 'twoHundredDayAverageChangePercent': 0.06747425, 'sourceInterval': 15,
 'exchangeDataDelayedBy': 0, 'averageAnalystRating': '2.0 - Buy',
 'cryptoTradeable': False, 'hasPrePostMarketData': True,
 'firstTradeDateMilliseconds': 345479400000, 'regularMarketChange': 2.5570068,
 'regularMarketDayRange': '248.385 - 250.7799', 'fullExchangeName': 'NasdaqGS',
 'marketState': 'REGULAR', 'displayName': 'Apple', 'trailingPegRatio': 2.5062}

# e = f"**EBITDA**: ${data.get('EBITDA', 'N/A')}\n"

# print(e)
