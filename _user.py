class User:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.tracked_jobs = []  # List to store tracked job opportunities
        # Other user-related attributes

    def update_info(self):
        """Allow the user to update their contact information."""
        print("Update User Information:")
        new_name = input("Enter your new name (Leave empty to keep current): ")
        new_email = input("Enter your new email (Leave empty to keep current): ")
        new_phone = input("Enter your new phone number (Leave empty to keep current): ")

        if new_name:
            self.name = new_name
        if new_email:
            self.email = new_email
        if new_phone:
            self.phone = new_phone

        print("User information has been updated.")

    def track_job(self, job):
        """Add a job opportunity to the user's list of tracked jobs."""
        self.tracked_jobs.append(job)
        print(f"{job.title} at {job.company} has been added to your tracked jobs.")

    def untrack_job(self, job_title):
        """Remove a job from the user's list of tracked jobs based on its title."""
        for job in self.tracked_jobs:
            if job.title == job_title:
                self.tracked_jobs.remove(job)
                print(f"{job.title} at {job.company} has been removed from your tracked jobs.")
                return
        print(f"No job with the title '{job_title}' found in your tracked jobs.")

    def display_tracked_jobs(self):
        """Display the list of job opportunities that the user is tracking."""
        if not self.tracked_jobs:
            print("You are not tracking any jobs yet.")
        else:
            print("Your tracked jobs:")
            for index, job in enumerate(self.tracked_jobs, start=1):
                print(f"{index}. {job.title} at {job.company} ({job.location}) - Status: {job.status}")
