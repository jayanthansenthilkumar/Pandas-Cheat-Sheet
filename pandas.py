import streamlit as st
import pandas as pd
from pathlib import Path
import base64
#Main Function
st.set_page_config(
    page_title='Pandas-Cheat-Sheet',
    page_icon='logo.png',
    layout="wide",
    initial_sidebar_state="expanded",
)
#Image function Start
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
#Image function End
#Sidebar Start
def cs_sidebar():
    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=300 height=120>](https://numpy.org/doc/stable/user/whatisnumpy.html)'''.format(img_to_bytes("site.png")), unsafe_allow_html=True)
    st.sidebar.title('Pandas cheat sheet')
    st.sidebar.markdown('''<small>Developed by <b>Jayanthan Senthilkumar<b></small>''', unsafe_allow_html=True)
    st.sidebar.markdown('__Install and import__')
    st.sidebar.code('$ pip install pandas')
    st.sidebar.code('''
# Import convention
>>> import pandas as pd
''')
#Sidebar End
def cs_body():
    st.title("Pandas - Data Science Package")
    print()
    a,b, = st.columns(2)
#A Session Starts
#Pandas Introduction
    a.title("Pandas-Introduction")
    a.markdown("Pandas is a Python library used for data manipulation and analysis."
         " It provides data structures and functions for efficiently handling structured data, "
         "such as tabular data, making it essential for tasks like data cleaning, exploration, and analysis in data science and analytics workflows.\n\n\n\n\n\n")
    libraries = ['NumPy', 'pandas', 'Matplotlib', 'scikit-learn', 'Seaborn']
    usage_percentages = [80, 85, 70, 75, 60]
    a.header('Usage of Data Science Libraries')
    #a.bar_chart({library: percentage for library, percentage in zip(libraries, usage_percentages)})
    a.markdown("---")
# Pandas Introduction End
#Read Write Starts
    a.title("Reading and Writing Data")
# Section for CSV operations
    a.subheader("Read and Write CSV File")
    a.code("pd.read_csv('file.csv')")
    a.write("Read data from a CSV file into a DataFrame.")
# Section for Excel operations
    a.subheader("Read and Write Excel File")
    a.code("pd.read_excel('file.xlsx')")
    a.write("Read data from an Excel file into a DataFrame.")
# Section for JSON operations
    a.subheader("Read and Write JSON File")
    a.code("pd.read_json('file.json')")
    a.write("Read data from a JSON file into a DataFrame.")
# Section for DataFrame to file operations
    a.subheader("DataFrame to CSV, Excel, JSON File")
    a.code("df.to_csv('output.csv', index=False)")
    a.code("df.to_excel('output.xlsx', index=False)")
    a.code("df.to_json('output.json', orient='records')")
    a.write("Convert DataFrame into CSV, Excel, or JSON file.")
    a.markdown("---")
#Read write Ends
#Indexing and Selection Starts
    a.title("Indexing and Selection")
    a.subheader("Selecting columns")
    a.code("df.column_name")
    a.latex("Or")
    a.code("df['colunmn_name']")
    a.subheader("Selecting rows")
    a.code("df.loc['row_label']")
    a.write("label-based indexing ")
    a.code("df.iloc['row_label']")
    a.write("integer-based indexing")
    a.subheader("Filtering rows")
    a.code("df[df['column'] > value]")
    a.write("Boolean indexing")
    a.markdown("---")
#Indexing and Selection Ends
#Data MANIPULATION sTARTS
    a.title("Data Manipulation")
    a.code("df.groupby('column_name')")
    a.write(" Group DataFrame by one or more columns")
    a.code("pd.merge(df1, df2)")
    a.write("Merge two DataFrames based on a common column")
    a.write("Concatenate DataFrames along rows or columns")
    a.code("df.join(df2)")
    a.write("Join DataFrames based on index or columns")
    a.code("df.pivot_table(values='value_column', index='index_column', columns='column_to_pivot', aggfunc='mean')")
    a.write(" Create a pivot table from DataFrame")
    a.code("df.agg()")
    a.latex("Or")
    a.code("df.aggregate()")
    a.write("Apply aggregation functions to grouped data")
    a.markdown("---")
#Data Manipulation Ends
#Time Starts
    a.title("Time Series Analysis")
    a.code("pd.to_datetime(df['column'])")
    a.write("Convert datetime columns")
    a.code("df.resample()")
    a.write("Resample time series data")
    a.code("df.tz_localize()")
    a.latex("Or")
    a.code("df.tz_convert()")
    a.write("Time zone conversion")
    a.markdown("---")
#Time Ends
#Performance Starts
    a.title("Performance Optimization")
    a.code("df.memory_usage()")
    a.write("Display memory usage of each column in the DataFrame")
    a.code("df.query()")
    a.markdown("---")
#Performance Ends
#B Session Starts
    b.title("Importing Pandas & IDE's")
    b.code("import pandas as pd")
    b.write("Import the pandas library.\n\n\n")
#Compiler Starts
    b.subheader("IDE'S for Pandas Compiling ")
    b.write("* Google Colaboratory")
    b.write("* Anaconda Navigator")
    b.write("* Visual Studio Code")
    b.write("* PyCharm")
    b.write("* Spyder")
    b.markdown("---")
#Complier Ends
#Exploring Data Starts
    b.title("Exploring Data")
    b.code("df.head(5)")
    b.write("Display the first five rows of the DataFrame\n")
    b.code("df.tail(5)")
    b.write("Display the last five rows of the DataFrame\n")
    b.code("df.sample(5)")
    b.write("Display the random five rows of the DataFrame\n")
    b.code("df.info()")
    b.write("Display information about the DataFrame, including data types and memory usage")
    b.code("df.dtypes")
    b.write("Display the datatype of the DataFrame")
    b.code("df.describe()")
    b.write("Generate descriptive statistics of numerical columns")
    b.markdown("---")
#Exploring Data Ends
#Data Cleaning Starts
    b.title("Data Cleaning or Handling Missing Data")
    b.code("df.dropna()")
    b.write("Drop rows with missing values\n")
    b.code("df.fillna()")
    b.write("Fill missing values with specified values")
    b.code("df.isnull()")
    b.latex("Or")
    b.code("df.notnull()")
    b.write("Check for missing values and return boolean masks")
    b.code("df.drop_duplicates()")
    b.write("Drop duplicate rows")
    b.markdown("---")
#Data Cleaning Ends
#Data Aggrigation Starts
    b.title("Data Aggregation")
    code="""df.mean()
df.median()
df.sum()"""
    b.code(code)
    b.write("Calculate mean, median, and sum of columns")
    b.code("df.groupby().agg()")
    b.write("Apply custom aggregation functions")
    b.markdown("---")
#Data Aggrigation Ends
#Categorical Data Handling Starts
    b.title("Categorical Data Handling")
    b.code("df.astype()")
    b.write("Convert data types of columns, including converting to categorical type")
    b.code("pd.Categorical()")
    b.write(" Create categorical data from arrays or Series")
    b.code("pd.get_dummies(df['column_name'])")
    b.write("Convert categorical variable into dummy/indicator variables (one-hot encoding)")
    b.markdown("---")
#Categorical Data Handling Ends
#Advanced Starts
    b.title("Advanced Topics")
    b.code("df.apply()")
    b.write("Or")
    b.code("df.applymap()")
    b.write("Apply functions element-wise or row/column-wise")
    b.code("df.pipe()")
    b.write("Apply a sequence of operations to DataFrame")
    b.code("df.melt()")
    b.write("Convert wide format to long format (tidy data)")
    b.markdown("---")
    b.markdown("Explore more Pandas functionalities in the [official documentation](https://pandas.pydata.org/docs/).")
#Advanced Ends
cs_sidebar()
cs_body()