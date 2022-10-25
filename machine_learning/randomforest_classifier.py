
# Random Forest Classifier Example
from matplotlib import pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split


def main():

    """
    Random Forest Classifier Example using sklearn function.
    Breast Cancer dataset from Wisconsin is used to demonstrate algorithm.
    """

    # Load Breast Cancer dataset
    breastcancer = load_breast_cancer()

    # Split dataset into train and test data
    x = breastcancer["data"]  # features
    y = breastcancer["target"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3)

    # Random Forest Classifier
    rand_for = RandomForestClassifier(random_state=42, n_estimators=200)
    rand_for.fit(x_train, y_train)

    # Display Confusion Matrix of Classifier
    plot_confusion_matrix(
        rand_for,
        x_test,
        y_test,
        display_labels=breastcancer["target_names"],
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - IRIS Dataset")
    plt.show()


if __name__ == "__main__":
    main()