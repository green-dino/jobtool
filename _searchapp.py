class JobSearchApp:
    def __init__(self):
        self.user = None
        self.jobs = []

    def start(self):
        # Initialize user, gather user information, and provide options to the user
        pass

    def add_job(self, job):
        # Add a job to the list of jobs the user is tracking
        pass

    def display_jobs(self):
        # Display a list of jobs the user is tracking
        pass

    def conduct_research(self, job):
        # Conduct research on a specific job opportunity
        pass

    def remove_job(self, job_title):
        """Remove a job from the list of tracked jobs based on its title."""
        for job in self.jobs:
            if job.title == job_title:
                self.jobs.remove(job)
                print(f"{job.title} at {job.company} has been removed from your tracked jobs.")
                return
        print(f"No job with the title '{job_title}' found in your tracked jobs.")
