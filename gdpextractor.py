import pandas as pd
import matplotlib.pyplot as plt

def extract_gdp(url):
    # Read HTML tables from the provided URL
    tables = pd.read_html(url)
    
    # Typically, the GDP table is the first table on the Wikipedia page
    gdp_df = tables[3]
    
    # Display the extracted DataFrame
    print("Extracted GDP Table:")
    print(gdp_df.head())  # Display the first 5 rows for a quick check

    return gdp_df

def plot_gdp(gdp_df):
    # Select the top 10 countries by GDP
    top10_gdp = gdp_df.head(10)
    
    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.bar(top10_gdp['Country/Territory'], top10_gdp['GDP(US$million)'])
    plt.xlabel('Country')
    plt.ylabel('GDP (in million US$)')
    plt.title('Top 10 Countries by GDP')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    # URL of the Wikipedia page containing the GDP data
    url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
    
    # Extract the GDP data
    gdp_df = extract_gdp(url)
    
    # Further processing can be done here if needed
    # For example, saving the data to a CSV file
    gdp_df.to_csv('gdp_data.csv', index=False)
    print("GDP data has been saved to gdp_data.csv")
    
    # Plot the GDP data
    plot_gdp(gdp_df)

if __name__ == "__main__":
    main()
