import pandas as pd
import matplotlib.pyplot as plt
from _jobopprotunity import JobOpportunity

# Sample job data
job_data = {
    'Job Title': ['Software Engineer', 'Data Analyst', 'Product Manager', 'DevOps Engineer'],
    'Salary (USD)': [90000, 75000, 110000, 95000],
    'Growth Potential (10 years)': [0.8, 1.2, 1.5, 1.0]
}

# Create a DataFrame from the job data
job_df = pd.DataFrame(job_data)


def compare_jobs():
    while True:
        print("Job Analysis Tool")
        print("1. List Jobs")
        print("2. Compare Salaries")
        print("3. Compare Growth Potential")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(job_df)
        elif choice == '2':
            # Compare salaries
            job_df.plot(x='Job Title', y='Salary (USD)', kind='bar', legend=False)
            plt.xlabel('Job Title')
            plt.ylabel('Salary (USD)')
            plt.title('Salary Comparison')
            plt.show()
        elif choice == '3':
            # Compare growth potential
            job_df.plot(x='Job Title', y='Growth Potential (10 years)', kind='bar', legend=False)
            plt.xlabel('Job Title')
            plt.ylabel('Growth Potential (10 years)')
            plt.title('Growth Potential Comparison')
            plt.show()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    compare_jobs()