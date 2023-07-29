import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load and preprocess the dataset
dataset = pd.read_csv('plant_attributes_data.csv')  # Replace 'plants_data.csv' with the correct path to your dataset
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
    st.markdown("<h1>VIT-AP UNIVERSITY ECS PROJECT</h1w>", unsafe_allow_html=True)
    st.title('Soil Recommendation System')
    st.write('Enter the type of plants you want to grow and get recommendations on the attributes like Turbidity, Ph, Nitrogen level, Phosphorous level, Potassium level, Humidity and Rainfall which determine the health of the soil and the type of environment best suitable for your plants.')

    # Get the list of unique plant names from the dataset
    plant_names = dataset['label'].unique()

    # Accept user input for the number of plants and their names
    num_plants = st.number_input("SELECT THE NUMBER OF PLANTS", min_value=1, value=1, step=1)

    selected_plant_attributes = {}
    for i in range(num_plants):
        plant_name = st.selectbox(f"PLANT {i+1} NAME:", plant_names)
        selected_plant_attributes[plant_name] = dataset[dataset['label'] == plant_name].drop('label', axis=1).iloc[0]

    # Generate recommendations for each plant
    recommendations = {}
    for plant_name, plant_attributes in selected_plant_attributes.items():
        plant_attributes_df = pd.DataFrame([plant_attributes])
        predicted_label = model.predict(plant_attributes_df)[0]
        plant_recommendations = dataset[dataset['label'] == predicted_label].drop('label', axis=1).iloc[0]
        recommendations[plant_name] = plant_recommendations

    # Display the recommendations
    st.header("Recommendations:")
    for plant_name, plant_recommendations in recommendations.items():
        st.subheader(f"For {plant_name}:")
        st.dataframe(plant_recommendations)

    # Find the optimal attribute values for all selected plants
    optimal_attributes = {}
    conflicting_values = {}
    plant_tables = {}

    for attribute in dataset.columns[1:]:
        attribute_values = []

        for plant_name in selected_plant_attributes:
            attribute_value = selected_plant_attributes[plant_name][attribute]
            attribute_values.append(attribute_value)

        if len(set(attribute_values)) == 1:
            optimal_value = attribute_values[0]
        else:
            optimal_value = "Varies"
            conflicting_values[attribute] = attribute_values

        optimal_attributes[attribute] = optimal_value

        for plant_name in selected_plant_attributes:
            plant_table = pd.DataFrame({attribute: attribute_values})
            if plant_name in plant_tables:
                plant_tables[plant_name][attribute] = attribute_values
            else:
                plant_tables[plant_name] = plant_table

    # Display the optimal attribute values
    st.header("Optimal Attribute Values for Selected Plants:")
    for attribute, value in optimal_attributes.items():
        st.write(f"{attribute}: {value}")

    # Check if attribute values vary among the selected plants and display conflicts
    if conflicting_values:
        st.header("Plants that cannot be grown together due to conflicting attribute values:")
        for attribute, values in conflicting_values.items():
            # st.subheader(f"Attribute: {attribute}")
            conflicting_plants = [plant_name for plant_name in selected_plant_attributes if selected_plant_attributes[plant_name][attribute] in values]
            conflicting_plant_tables = {plant: plant_tables[plant] for plant in conflicting_plants}
            for plant, table in conflicting_plant_tables.items():
                if table is not None:
                    st.subheader(f"Plant: {plant}")
                    st.dataframe(table)

# Run the app
if __name__ == "__main__":
    main()

# Team details
st.markdown("<h3>TEAM DETAILS:</h3>", unsafe_allow_html=True)
st.markdown("<p>Habeeb Ur Rahman - 21BCE7005</p>", unsafe_allow_html=True)
st.markdown("<p>Havish Ponnaganti - 21BCE8186</p>", unsafe_allow_html=True)
st.markdown("<p>T. Jaswanth - 21BCE8600</p>", unsafe_allow_html=True)
st.markdown("<p>Junaid Ahmed - 21BCE7925</p>", unsafe_allow_html=True)
st.markdown("<p>B. Rahul Reddy - 21BCE7129</p>", unsafe_allow_html=True)
st.markdown("<p>Y.B Koushik - 21BCE7807</p>", unsafe_allow_html=True)
