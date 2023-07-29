import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load and preprocess the dataset
dataset = pd.read_csv('plants_data.csv')  # Replace 'plants_data.csv' with the correct path to your dataset
# Preprocess the dataset as needed (e.g., handle missing values, encode categorical variables, etc.)

# Split the dataset into training and testing sets
X = dataset.drop('label', axis=1)  # 'label' is the column name for the target variable
y = dataset['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the machine learning model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Define the Streamlit app
def main():
    st.title('Soil Recommendation System')
    st.write('Enter the type of plants you want to grow and get recommendations on the attributes like Turbidity, Ph, Nitrogen level, Phosphorous level, Potassium level, Humidity and Rainfall which determine the health of the soil and the type of environment best suitable for your plants.')

    # Accept user input for the number of plants and their names
    num_plants = st.number_input("SELECT THE NUMBER OF PLANTS", min_value=1, value=1, step=1)
    plant_names = []
    selected_plant_attributes = {}

    for i in range(num_plants):
        plant_name = st.text_input(f"PLANT {i+1} NAME:")
        plant_names.append(plant_name)

        # Find the row for the selected plant
        if plant_name in dataset['label'].unique():
            plant_row = dataset[dataset['label'] == plant_name].iloc[0]
            selected_plant_attributes[plant_name] = plant_row.drop('label')
        else:
            st.warning(f"Plant '{plant_name}' is not a valid input here.")

    # ... rest of the code ...

    # Display the optimal attribute values
    st.header("Optimal Attribute Values for Selected Plants:")
    for attribute, value in optimal_attributes.items():
        st.write(f"{attribute}: {value}")

    # Check if attribute values vary among the selected plants and display conflicts
    if conflicting_values:
        st.header("Plants that cannot be grown together due to conflicting attribute values:")
        for attribute, values in conflicting_values.items():
            st.subheader(f"Attribute: {attribute}")
            conflicting_plants = [plant_name for plant_name in plant_names if selected_plant_attributes.get(plant_name, {}).get(attribute) in values]
            conflicting_plant_tables = {plant: plant_tables.get(plant) for plant in conflicting_plants}
            for plant, table in conflicting_plant_tables.items():
                if table is not None:
                    st.write(f"Plant: {plant}")
                    st.dataframe(table)


    # Team details
    st.markdown("<p>VIT-AP UNIVERSITY ECS PROJECT</p>", unsafe_allow_html=True)
    st.markdown("<p>TEAM DETAILS:</p>", unsafe_allow_html=True)
    st.markdown("<p>Habeeb Ur Rahman - 21BCE7005</p>", unsafe_allow_html=True)
    st.markdown("<p>Havish Ponnaganti - 21BCE8186</p>", unsafe_allow_html=True)
    st.markdown("<p>T. Jaswanth - 21BCE8600</p>", unsafe_allow_html=True)
    st.markdown("<p>Junaid Ahmed - 21BCE7925</p>", unsafe_allow_html=True)
    st.markdown("<p>B. Rahul Reddy - 21BCE7129</p>", unsafe_allow_html=True)
    st.markdown("<p>Y.B Koushik - 21BCE7807</p>", unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()

