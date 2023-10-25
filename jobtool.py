from _searchapp import JobSearchApp
from _user import User
from _jobopprotunity import JobOpportunity
import pandas as pd

class JobSearchApp:
    def __init__(self):
        self.user = None
        self.jobs = []
        self.job_df = pd.DataFrame(columns=['Title', 'Company', 'Location', 'Growth Forecast', 'Entry-level Salary'])

    def start(self):
        print("Welcome to the Job Search App!")
        self.user = self.create_user()
        while True:
            choice = input("What would you like to do? (1 - Add Job, 2 - Display Jobs, 3 - Open Job, 4 - Compare Jobs, 5 - Update User Info, 6 - Quit): ")
            if choice == '1':
                self.add_job()
            elif choice == '2':
                self.display_jobs()
            elif choice == '3':
                self.open_job()
            elif choice == '4':
                self.compare_jobs()
            elif choice == '5':
                self.update_user_info()
            elif choice == '6':
                print("Thank you for using the Job Search App. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def create_user(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        return User(name, email, phone)

    def add_job(self):
        job = self.create_job()
        self.jobs.append(job)
        self.user.track_job(job)
        #self.job_df = self.job_df.append({'Title': job.title, 'Company': job.company, 'Location': job.location, 'Growth Forecast': job.growth_forecast, 'Entry-level Salary': job.entry_level_salary}, ignore_index=True)
        print("Job added successfully!")

    def create_job(self):
        title = input("Enter the job title: ")
        company = input("Enter the company name: ")
        location = input("Enter the job location: ")
        growth_forecast = input("Enter the expected job growth over the next 5-10 years: ")
        entry_level_salary = input("Enter the entry-level salary and whether it meets your financial needs: ")
        entry_level_training = input("Enter the entry-level training required for this occupation: ")
        job_duties = input("Enter the duties of the job: ")
        disability_restrictions = input("Enter your disability restrictions/limitations and whether working in this field would exacerbate them: ")
        career_match = input("Explain why this career is a good match for you considering your interests, aptitudes, experience, and abilities: ")
        return JobOpportunity(title, company, location, growth_forecast, entry_level_salary, entry_level_training, job_duties, disability_restrictions, career_match)

    def compare_jobs(self):
        if not self.jobs:
            print("You have no tracked jobs to compare.")
        else:
            print("Job Comparison Results:")
            print(self.job_df)

    def display_jobs(self):
        if not self.jobs:
            print("You are not tracking any jobs yet.")
        else:
            print("Your tracked jobs:")
            for index, job in enumerate(self.jobs, start=1):
                print(f"{index}. {job.title} at {job.company} ({job.location}) - Status: {job.status}")

    def open_job(self):
        if not self.jobs:
            print("You have no tracked jobs to open.")
        else:
            self.display_jobs()
            job_number = input("Enter the number of the job you want to open: ")
            if job_number.isdigit() and 1 <= int(job_number) <= len(self.jobs):
                job = self.jobs[int(job_number) - 1]
                print("Opening job details:")
                job.display_details()
            else:
                print("Invalid job number. Please enter a valid job number.")

    def update_user_info(self):
        self.user.update_info()
        
if __name__ == "__main__":
    app = JobSearchApp()
    app.start()
