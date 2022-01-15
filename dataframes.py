import pandas
df=pandas.read_csv('Output.csv')

#for index, row in df.iterrows():
    #if df['Column5'].str.contains('/robots.txt').any():
        #print ("Robots is there")
        #print (row["Column5"])


ip_df = df[~df['Column5'].str.contains("/robots.txt")]
crawl_df = df[df['Column5'].str.contains("/robots.txt")]
ip_df['Column9'].to_csv('IP.csv', index=False,header=False)
crawl_df['Column9'].to_csv('Crawlers.csv', index=False,header=False)