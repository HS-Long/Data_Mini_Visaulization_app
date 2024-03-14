import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page config
st.set_page_config(page_title='Data Visualizer',
                   layout='centered',
                   page_icon='📈')  # Change the icon here

# Title
st.title('📈  Data Visualizer')

# Allow user to upload a CSV file
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

# If a file is uploaded
if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    col1, col2 = st.columns(2)

    columns = df.columns.tolist()

    with col1:
        st.write("")
        st.write(df.head())

    with col2:
        # Allow the user to select columns for plotting
        x_feature = st.selectbox('Select the X-feature', options=columns + ["None"])
        y_feature = st.selectbox('Select the Y-feature', options=columns + ["None"])

        plot_list = ['Line Plot', 'Bar Chart', 'Scatter Plot', 'Distribution Plot', 'Count Plot', 'Pair Plot', 'Heatmap Correlation']
        # Allow the user to select the type of plot
        plot_type = st.selectbox('Select the type of plot', options=plot_list)

        # Customize plot style
        plot_style = st.selectbox('Select plot style', options=['dark', 'white', 'darkgrid', 'whitegrid', 'ticks'])

    # Generate the plot based on user selection
    if st.button('Generate Plot'):
        # Set the style
        sns.set_style(plot_style)

        fig, ax = plt.subplots(figsize=(6, 4))

        if plot_type == 'Line Plot':
            sns.lineplot(x=df[x_feature], y=df[y_feature], ax=ax)
        elif plot_type == 'Bar Chart':
            sns.barplot(x=df[x_feature], y=df[y_feature], ax=ax)
            plt.xticks(rotation=45)
        elif plot_type == 'Scatter Plot':
            sns.scatterplot(x=df[x_feature], y=df[y_feature], ax=ax)
        elif plot_type == 'Distribution Plot':
            sns.histplot(df[x_feature], kde=True, ax=ax)
            plt.xticks(rotation=45)
        elif plot_type == 'Count Plot':
            sns.countplot(x=df[x_feature], ax=ax)
            plt.xticks(rotation=45)
        elif plot_type == 'Pair Plot':
            pairplot = sns.pairplot(df, vars=[x_feature, y_feature])
            st.pyplot(pairplot.fig)

        elif plot_type == 'Heatmap Correlation':
            plt.figure(figsize=(10, 8))
            heatmap = sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
            st.pyplot(heatmap.figure)

        # Adjust label sizes
        ax.tick_params(axis='x', labelsize=10)  # Adjust x-axis label size
        ax.tick_params(axis='y', labelsize=10)  # Adjust y-axis label size

        # Adjust title and axis labels with a smaller font size
        plt.title(f'{plot_type} of {y_feature} vs {x_feature}', fontsize=12)
        plt.xlabel(x_feature, fontsize=10)
        plt.ylabel(y_feature, fontsize=10)

        # Show the results
        st.pyplot(fig)

# Credit
st.text("Visualization tool by Seaklong HENG")
