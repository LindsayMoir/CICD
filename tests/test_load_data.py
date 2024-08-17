# tests/test_load_data.py
def test_load_data(iris_data):
    # The iris_data fixture provides the data
    data = iris_data

    # Filter the data for 'Iris-setosa'
    setosa_data = data[data['species'] == 'Iris-setosa']

    # Assert that the 'sepal length' for 'Iris-setosa' is between 4 and 6
    assert setosa_data['sepal length'].between(4, 6).all(), (
        "Sepal length for 'Iris-setosa' is not in the expected range (4 to 6)"
    )
