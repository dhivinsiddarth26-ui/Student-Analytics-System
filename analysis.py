import pandas as pd
import matplotlib.pyplot as plt
from db_connection import get_connection

def run_analysis():
    conn = get_connection()

    query = "SELECT id, name, age, city, course_id FROM students"
    df = pd.read_sql(query, conn)

    print(df)

    print("\nAverage Age:", df["age"].mean())

    print("\nStudents per City:")
    print(df["city"].value_counts())

    df["city"].value_counts().plot(kind="bar")
    plt.show()

    conn.close()