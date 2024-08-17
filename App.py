import pandas as pd
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu

# Load routes data from CSV
list_K = []
df_k = pd.read_csv('df_k.csv')
for _, r in df_k.iterrows():
    list_K.append(r['Route_name'].strip())  # Remove leading and trailing whitespace

list_Ap = []
df_Ap = pd.read_csv('df_Ap.csv')
for _, r in df_Ap.iterrows():  # Corrected to iterate over df_A
    list_Ap.append(r['Route_name'].strip())  # Remove leading and trailing whitespace

list_As = []
df_As = pd.read_csv('df_As.csv')
for _, r in df_As.iterrows():  # Corrected to iterate over df_A
    list_As.append(r['Route_name'].strip())  # Remove leading and trailing whitespace

list_Ka = []
df_Ka = pd.read_csv('df_Ka.csv')
for _, r in df_Ka.iterrows():  # Corrected to iterate over df_A
    list_Ka.append(r['Route_name'].strip())  # Remove leading and trailing whitespace

list_H = []
df_H = pd.read_csv('df_H.csv')
for _, r in df_H.iterrows():  # Corrected to iterate over df_A
    list_H.append(r['Route_name'].strip())  # Remove leading and trailing whitespace

list_R = []
df_R = pd.read_csv('df_R.csv')
for _, r in df_R.iterrows():  # Corrected to iterate over df_A
    list_R.append(r['Route_name'].strip())  # Remove leading and trailing whitespace

list_S = []
df_S = pd.read_csv('df_S.csv')
for _, r in df_S.iterrows():  # Corrected to iterate over df_A
    list_S.append(r['Route_name'].strip())  # Remove leading and trailing whitespace

list_T = []
df_T = pd.read_csv('df_T.csv')
for _, r in df_T.iterrows():  # Corrected to iterate over df_A
    list_T.append(r['Route_name'].strip())  # Remove leading and trailing whitespace

list_U = []
df_U = pd.read_csv('df_U.csv')
for _, r in df_U.iterrows():  # Corrected to iterate over df_A
    list_U.append(r['Route_name'].strip())  # Remove leading and trailing whitespace

list_Wb = []
df_Wb = pd.read_csv('df_Wb.csv')
for _, r in df_Wb.iterrows():  # Corrected to iterate over df_A
    list_Wb.append(r['Route_name'].strip())  # Remove leading and trailing whitespace

# Set up the Streamlit page
slt.set_page_config(layout='wide')

# Option menu for navigation
web = option_menu(
    menu_title='Redbus',
    options=['Home', 'States and Routes'],
    icons=['house', 'info-circle'],
    orientation='horizontal'
)

# Home page content
if web == 'Home':
    slt.image(r"C:\Users\HP\OneDrive\Desktop\Data Science MDT23\Project\Redbus\bus-icon-solid-logo-illustration-with-red-color-free-vector.jpg", width=100)
    slt.title('Redbus Data Scraping with Selenium & Dynamic Filtering Using Streamlit')
    slt.subheader(':blue[Domain:] Transportation')
    slt.subheader(':blue[Objective:]')
    slt.markdown('''
                    This project aims to create an all-encompassing solution for collecting, analyzing, and visualizing data from online sources. 
                    By implementing web scraping, the system automates the extraction of detailed information from websites. 
                    Additionally, the project includes developing a user-friendly application interface that allows for seamless data filtering, analysis, and visualization of key metrics like schedules, prices, and availability. 
                    The primary objective is to boost efficiency and effectiveness across diverse industries by leveraging automation and data analytics.
                  ''')
    slt.subheader(':blue[Skills:]')
    slt.markdown('Selenium, Pandas, MySQL, Streamlit')
    slt.markdown('**Selenium:** A powerful tool for controlling web browsers through programs and performing browser automation.')
    slt.markdown('**Pandas:** A data manipulation and analysis library for Python that offers data structures and operations for manipulating numerical tables and time series.')
    slt.markdown('**MySQL:** An open-source relational database management system that uses Structured Query Language (SQL).')
    slt.markdown('**Streamlit:** A fast way to build and share data apps in Python.')

    slt.subheader(':blue[Developed By:] A. Saravana Raja')

# States and Routes page content
if web == 'States and Routes':
    S = slt.selectbox("List of states", ['Andhra Pradesh', 'Assam', 'Hariyana', 'Kadamba', 'Kerala', 'Rajasthan', 'South Bengal','Telangana', 'Uttar Pradesh', 'West Bengal'])

    # Choose the appropriate list based on the selected state
    if S == 'Kerala':
        route_list = list_K
    elif S == 'Andhra Pradesh':
        route_list = list_Ap
    elif S == 'Assam':
        route_list = list_As
    elif S == 'Telangana':
        route_list = list_T
    elif S == 'South Bengal':
        route_list = list_S
    elif S == 'Rajasthan':
        route_list = list_R
    elif S == 'West Bengal':
        route_list = list_Wb
    elif S == 'Hariyana':
        route_list = list_H
    elif S == 'Uttar Pradesh':
        route_list = list_U
    else:
        route_list = list_Ka  # Placeholder for states not yet implemented

    # Show the route selection box only if there are routes to display
    if route_list:
        selected_route = slt.selectbox('List of routes', route_list)

        select_fare = slt.radio('Choose bus fare range', ['100-499', '500-999','1000-1999', '2000 and above', 'All'])

        # Database connection and query
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Tango@0044.",
            database="REDBUS"
        )
        my_cursor = conn.cursor()

        # Construct the SQL query based on the selected fare range
        if select_fare == '100-499':
            query = '''
                SELECT * FROM bus_details
                WHERE price BETWEEN 100 AND 699 AND Route_name = %s
                ORDER BY price DESC
            '''
        elif select_fare == '500-999':
            query = '''
                SELECT * FROM bus_details
                WHERE price BETWEEN 500 AND 999 AND Route_name = %s
                ORDER BY price DESC
            '''
        elif select_fare == '1000-1999':
            query = '''
                SELECT * FROM bus_details
                WHERE price BETWEEN 1000 AND 1999 AND Route_name = %s
                ORDER BY price DESC
            '''
        elif select_fare == '2000 and above':
            query = '''
                SELECT * FROM bus_details
                WHERE price >= 2000 AND Route_name = %s
                ORDER BY price DESC
            '''
        else:
            query = '''
                        SELECT * 
                        FROM bus_details
                        WHERE   Route_name = %s
                        ORDER BY price DESC'''

        # Execute the query with parameter
        my_cursor.execute(query, (selected_route,))
        out = my_cursor.fetchall()

        # Convert query results to DataFrame and display
        df = pd.DataFrame(out, columns=['ID', 'Bus_name', 'Bus_types', 'Start_time', 'End_time', 'Total_duration',
                                        'Ratings', 'Price', 'Seats_available', 'Route_name', 'Route_link'])
        slt.write(df)

        # Close the database connection
        my_cursor.close()
        conn.close()

