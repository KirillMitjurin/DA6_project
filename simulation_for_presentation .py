import joblib
import sklearn
clf = joblib.load('blackjack_model.joblib')

def predict_action(ply2cardsum, card1, card2, dealer_card, clf, feature_names):
    """
    Predict the action (take card, double, or split) based on player's hand sum and dealer's visible card.

    Args:
    - ply2cardsum (int): Sum of the player's first two cards.
    - dealer_card (int): The dealer's visible card.
    - clf (RandomForestClassifier): The trained Random Forest model.
    - feature_names (list): List of feature names used during training.

    Returns:
    - int: Predicted action (0 or 1).
    """
    # Create a DataFrame for input with default values for all features
    input_data = pd.DataFrame(columns=feature_names)
    input_data.loc[0] = 0  # Initialize all features to 0

    # Set the relevant features
    input_data['ply2cardsum'] = ply2cardsum
    input_data['dealcard1'] = dealer_card
    input_data['card1'] = card1
    input_data['card2'] = card2

    # Ensure all features are present in the correct order
    input_data = input_data[feature_names]

    # Predict the action (take card, double, or split)
    prediction = clf.predict(input_data)[0]
    return prediction


print(clf.predict(15))



