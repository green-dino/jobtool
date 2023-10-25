class JobOpportunity:
    def __init__(self, title, company, location, growth_forecast, entry_level_salary, entry_level_training, job_duties, disability_restrictions, career_match):
        self.title = title
        self.company = company
        self.location = location
        self.status = "Not applied"  # Initial status
        self.growth_forecast = growth_forecast
        self.entry_level_salary = entry_level_salary
        self.entry_level_training = entry_level_training
        self.job_duties = job_duties
        self.disability_restrictions = disability_restrictions
        self.career_match = career_match

    def update_status(self, new_status):
        # Update the application status (e.g., "Applied," "Interview Scheduled," etc.)
        self.status = new_status

    def display_details(self):
        print(f"Job Title: {self.title}")
        print(f"Company: {self.company}")
        print(f"Location: {self.location}")
        print(f"Application Status: {self.status}")
        print(f"Growth Forecast: {self.growth_forecast}")
        print(f"Entry-level Salary: {self.entry_level_salary}")
        print(f"Entry-level Training Required: {self.entry_level_training}")
        print(f"Job Duties: {self.job_duties}")
        print(f"Disability Restrictions: {self.disability_restrictions}")
        print(f"Career Match: {self.career_match}")
