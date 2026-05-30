import plotly.express as px
import plotly.data as pldata

# TASK 3:
df = pldata.wind(return_type="pandas")
print("First 10 lines:\n ", df.head(10))
print("Last 10 lines:\n ", df.tail(10))

print(df.info())

# clean strength column
df_cleaned = df.copy()

df_cleaned["strength"] = df_cleaned["strength"].str.replace("+", "", regex=False)

def convert(x):
    if "-" in x:
        a, b = x.split("-")
        return (float(a) + float(b)) / 2
    else:
        return float(x)
    
df_cleaned["strength"] = df_cleaned["strength"].apply(convert)

print(df_cleaned)

# plot
fig = px.scatter(df_cleaned, x="frequency", y="strength", color="direction")
fig.write_html("wind.html", auto_open=True)

