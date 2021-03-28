import sys

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("restaurant.csv", index_col=0)

#############################################################
# Funtion to perform Data Visualization on Restaurant Dataset
#############################################################


def visualization():
    """
    Data Visualization Menu
    """
    print("\n")
    print("////////////////////////////////")
    print("------Data Visualization-------")
    print("////////////////////////////////")
    print("1. Rating-Count Chart")
    print("2. Rating vs Type of Restaurant chart")
    print("3. Online order availability bar chart")
    print("4. Table Booking option availability chart")
    print("5. Rating vs Average Cost Graph")
    print("6. Back to Main Menu")
    ch = input("Enter your choice:")
    if ch == '1':
        print("1. Bar Chart")
        print("2. Line Chart")
        i = input("Enter your choice: ")
        if i == '1':
            df["rate"].value_counts().plot.bar()
        elif i == '2':
            df["rate"].value_counts().sort_index().plot()
        else:
            print("Enter a valid choice!!")
        plt.title('Rating - Count', fontsize=15, fontweight='bold')
        plt.ylabel('No. of restaurants', fontsize=10, fontweight='bold')
        plt.xlabel('Rating', fontsize=10, fontweight='bold')
        plt.xticks(fontsize=10, fontweight='bold')
        plt.yticks(fontsize=10, fontweight='bold')
        plt.show()
    elif ch == '2':
        type_plt = pd.crosstab(df['rate'], df['listed_in(type)'])
        print("1. Bar Chart")
        print("2. Line Chart")
        i = input("Enter your choice: ")
        if i == '1':
            type_plt.plot(kind='bar', stacked=True)
        elif i == '2':
            type_plt.plot(stacked=True)
        else:
            print("Enter a valid choice!!")
        plt.title('Type - Rating', fontsize=15, fontweight='bold')
        plt.ylabel('Type', fontsize=10, fontweight='bold')
        plt.xlabel('Rating', fontsize=10, fontweight='bold')
        plt.xticks(fontsize=10, fontweight='bold')
        plt.yticks(fontsize=10, fontweight='bold')
        plt.show()
    elif ch == '3':
        print("1. Bar Chart")
        print("2. Line Chart")
        i = input("Enter your choice: ")
        if i == '1':
            df["online_order"].value_counts().plot.bar()
        elif i == '2':
            df["online_order"].value_counts().sort_index().plot()
        else:
            print("Enter a valid choice!!")
        plt.title('Online Order Availability', fontsize=15, fontweight='bold')
        plt.ylabel('No. of restaurants', fontsize=10, fontweight='bold')
        plt.xlabel('Online order facility available', fontsize=10, fontweight='bold')
        plt.xticks(fontsize=10, fontweight='bold')
        plt.yticks(fontsize=10, fontweight='bold')
        plt.show()
    elif ch == '4':
        print("1. Bar Chart")
        print("2. Line Chart")
        i = input("Enter your choice: ")
        if i == '1':
            df["book_table"].value_counts().plot.bar()
        elif i == '2':
            df["book_table"].value_counts().sort_index().plot()
        else:
            print("Enter a valid choice!!")
        plt.title('Booking Table Availability', fontsize=15, fontweight='bold')
        plt.ylabel('No. of restaurants', fontsize=10, fontweight='bold')
        plt.xlabel('Booking Table facility available', fontsize=10, fontweight='bold')
        plt.xticks(fontsize=10, fontweight='bold')
        plt.yticks(fontsize=10, fontweight='bold')
        plt.show()
    elif ch == '5':
        df_rating = df[['rate', 'approx_cost(for two people)']]
        print("1. Bar Chart")
        print("2. Line Chart")
        i = input("Enter your choice: ")
        if i == '1':
            df_rating.groupby("rate").mean().plot(kind="bar")
        elif i == '2':
            df_rating.groupby("rate").mean().plot()
        else:
            print("Enter a valid choice!!")
        plt.title('Rating vs Expense', fontsize=15, fontweight='bold')
        plt.ylabel('Cost for two people', fontsize=10, fontweight='bold')
        plt.xlabel('Rating', fontsize=10, fontweight='bold')
        plt.xticks(fontsize=10, fontweight='bold')
        plt.yticks(fontsize=10, fontweight='bold')
        plt.show()
    elif ch == '6':
        print("Returning to main menu....")
        return
    else:
        print("Enter a valid choice!!")


#############################################################
# Funtion to perform Data Analysis on Restaurant Dataset
#############################################################


def analysis():
    """
    Data Analysis Menu
    """
    print("\n")
    print("////////////////////////////////")
    print("---------Data Analysis---------")
    print("////////////////////////////////")
    print("1. Top record")
    print("2. Bottom record")
    print("3. Statistics of Dataframe")
    print("4. Information about Dataframe")
    print("5. DataFrame Correlation Matrix")
    print("6. Back to Main Menu")
    ch = input("Enter your choice:")
    if ch == '1':
        n = int(input("Enter number of records to display"))
        print(df.head(n))
    elif ch == '2':
        n = int(input("Enter number of records to display"))
        print(df.tail(n))
    elif ch == '3':
        print(df.describe())
    elif ch == '4':
        print(df.info())
    elif ch == '5':
        print(df.corr())
    elif ch == '6':
        print("Returning to main menu....")
        return
    else:
        print("Enter a valid choice!!")


########################################################
# Perform grouping and view different parts of dataframe
########################################################


def view():
    """
    View Different parts of DataFrame
    """
    print("\n")
    print("////////////////////////////////")
    print("---------View DataFrame---------")
    print("////////////////////////////////")
    print("1. Display whole dataframe")
    print("2. View Top Restaurant Chains with highest ratings")
    print("3. View Top Restaurant Chains with highest no. of outlets")
    print("4. View Top Restaurant Chains with highest no. of votes")
    print("5. View Top Expensive Restaurant Chains")
    print("6. Back to Main Menu")
    ch = input("Enter your choice:")
    if ch == '1':
        print(df)
    elif ch == '2':
        n = int(input("Enter no. of records to display"))
        print(df.groupby('name')['rate'].mean().sort_values(ascending=False).head(n))
    elif ch == '3':
        n = int(input("Enter no. of records to display"))
        index = df['name'].value_counts().head(n).index
        values = df['name'].value_counts().head(n).values
        print(pd.DataFrame({'Restaurant': index, 'No. of outlets': values}))
    elif ch == '4':
        n = int(input("Enter no. of records to display"))
        print(
            df.groupby('name')[['votes', 'rate']]
            .max()
            .sort_values(ascending=False, by='votes')
            .head(n)
        )
    elif ch == '5':
        n = int(input("Enter no. of records to display"))
        print(
            df.groupby('name')[['rate', 'approx_cost(for two people)']]
            .mean()
            .sort_values(by='approx_cost(for two people)', ascending=False)
            .head(n)
        )
    elif ch == '6':
        print("Returning to main menu....")
        return
    else:
        print("Enter a valid choice!!")


#########################
# Main Menu Infinite Loop
#########################

while True:
    print("\n\n")
    print("*******************************")
    print("Restaurant Data Analysis System")
    print("*******************************")
    print("1. Data Visualization")
    print("2. Data Analysis")
    print("3. View Dataset")
    print("4. Exit")
    choice = input("Enter your choice:")
    print("*******************************")

    if choice == '1':
        visualization()
    elif choice == '2':
        analysis()
    elif choice == '3':
        view()
    elif choice == '4':
        print("Thank You!! Exiting....")
        sys.exit()
    else:
        print("Enter a valid Choice!!")
