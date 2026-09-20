
RAW_PATH = "SuperKart_project/data/SuperKart.csv"
df = pd.read_csv(RAW_PATH)

df.drop(columns=["Product_Id"], inplace=True)
df.drop(columns=["Store_Id"], inplace=True)
#removing identity column
