import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Example data (replace with your dataset)
st.title("Glucose Analysis Dashboard")


filename = 'Final_Dataset.csv'
df1 = pd.read_csv(filename)

col1, col2,col3,col4,col5 = st.columns(5)

with col1:
    fig1, ax1 = plt.subplots(figsize=(16, 14))
    
    # Distribution plot
    sns.histplot(df1['Glucose(mg/dl)'], bins=30, kde=True, color='teal', ax=ax1)
    ax1.axvline(180, color='red', linestyle='--', label='Hyperglycemia Threshold')
    ax1.axvline(70, color='orange', linestyle='--', label='Hypoglycemia Threshold')
    ax1.set_title('Distribution of Glucose Levels')
    ax1.set_xlabel('Glucose (mg/dL)')
    ax1.set_ylabel('Frequency')
    st.pyplot(fig1)

with col2:
   

    fig2, ax2 = plt.subplots(figsize=(16, 14))

    avg_glucose_by_gender = df1.groupby('Gender')['Glucose(mg/dl)'].mean()

    # Create a bar chart.
    avg_glucose_by_gender.plot(kind='bar', color=['skyblue', 'salmon'],ax=ax2)

    # Add titles and labels.
    ax2.set_title('Average Glucose Level by Gender')
    ax2.set_xlabel('Gender')
    ax2.set_ylabel('Average Glucose (mg/dl)')    
    st.pyplot(fig2)
with col3:
    fig3, ax3 = plt.subplots(figsize=(16, 14))

    sns.scatterplot(x='Carb_Intake(grams)', y='Glucose(mg/dl)', data=df1,ax=ax3)
    ax3.set_title("Carbohydrate Intake vs Glucose Levels")
    ax3.set_xlabel("Carbohydrate Intake (grams)")
    ax3.set_ylabel("Glucose (mg/dl)")
    st.pyplot(fig3)

with col4:
    Corr_variables = ['Calories','Carb_Intake(grams)','Steps','Glucose(mg/dl)']
    corr_relation = df1[Corr_variables].corr()
    fig4, ax4 = plt.subplots(figsize=(16, 14))
    sns.heatmap(corr_relation, annot=True, cmap='coolwarm', fmt='.2f', cbar=True, linewidths=0.5,ax=ax4)
    ax3.set_title('Correlation Matrix Between Calories, Carb Intake, Steps, and Glucose Levels')
    st.pyplot(fig4)

    

with col5:
    fig5, ax5 = plt.subplots(figsize=(16, 14))
    unique_patients = df1.drop_duplicates(subset=['Patient_id'])

    # Create a histogram of the '%_with_sleep_disturbances' column.
    ax5.hist(unique_patients['%_with_sleep_disturbances'], bins=5, edgecolor='black')

    # Add titles and labels.
    ax5.set_title('Distribution of Sleep Disturbances Percentage')
    ax5.set_xlabel('Percentage of Sleep Disturbances')
    ax5.set_ylabel('Number of Patients')
    st.pyplot(fig5)
    # Save the plot.
    

#with col6:
    #df1.rename(columns={'bolus_volume_delivered': 'bolus_volume'}, inplace=True)

    # Distribution plot
    #fig6, ax6 = plt.subplots(figsize=(16, 14))
    #sns.histplot(df1['Bolus_volume_delivered(units)'], bins=30, kde=True, color='skyblue' , ax=ax6)
    #ax6.set_title('Distribution of Bolus Insulin Volume')
    #ax6.set_xlabel('Bolus Volume Delivered (units)')
    # ax6.set_ylabel('Frequency')
    #st.pyplot(fig6)