import pandas as pd															#Import Pandas libraru as pd variable
df=pd.read_csv(r'C:\Users\SShyam1\Desktop\Python Inputs\prices.csv')		#create a variable df(Dataframe): Read csv using pandas(pd.read_csv) & store the file as a dataframe in df
print(df)																	#view the df to understand its structure
x=input("What item's price do you want to know?: ")							#get user input of the item whose price needs to be displayed
results = df[df['Item'] == x]['Price']										#Considering the search made on Item, matches one of the values in Item, print it's appropriate Price
values=results.values														#Print as values using ".values" attribute
print("The price of " + x + " is " + str(values[0]))						#Print statement
