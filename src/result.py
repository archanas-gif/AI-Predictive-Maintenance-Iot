import os
from sklearn.metrics import classification_report, accuracy_score

def save_results(y_test, y_pred):
    # Create outputs folder if not exists
    os.makedirs("outputs", exist_ok=True)

    # Generate report
    report = classification_report(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)

    # Print results
    print("\nReport:\n", report)
    print("Accuracy:", accuracy)

    # Save to file
    with open("outputs/results.txt", "w") as f:
        f.write("Classification Report:\n")
        f.write(report)
        f.write("\nAccuracy: " + str(accuracy))

    print("\n✅ Results saved in outputs/results.txt")