import json
from datetime import datetime

from upwork_analysis.scrape_data import JobsScraper


def scrape_upwork_jobs(search_query, output_file, pages=1, jobs_per_page=50):
    scraper = JobsScraper(
        search_query=search_query,
        jobs_per_page=jobs_per_page,
        start_page=1,
        pages_to_scrape=pages,
        save_path=output_file,
        retries=5,
        headless=True,
        workers=4,
        fast=False  # Changed to False to get more detailed information
    )
    return scraper.scrape_jobs()

def print_job_details(job):
    details = [
        ("Title", "title"),
        ("URL", "job_url"),  # Add this line
        ("Budget", "budget"),
        ("Hourly Range", "hourly_range"),
        ("Description", "description"),
        ("Skills", "skills"),
        ("Category", "category"),
        ("Country", "country"),
        ("Client Info", "client_info"),
        ("Posted Time", "posted_time"),
        ("Proposals", "proposals"),
        ("Client Payment Verified", "client_payment_verified"),
        ("Job Type", "job_type"),
        ("Duration", "duration"),
        ("Work Load", "workload"),
        ("Experience Level", "experience_level"),
        ("Client History", "client_history"),
        ("Client Reviews", "client_reviews"),
        ("Client Jobs Posted", "client_jobs_posted"),
        ("Client Past Hires", "client_past_hires"),
        ("Client Payment Verification", "client_payment_verification"),
        ("Job Success Score", "job_success_score"),
        ("Earnings", "earnings"),
        ("Location", "location"),
        ("Connects", "connects"),
        ("Question", "question")
    ]
    
    for label, key in details:
        value = job.get(key, "N/A")
        if isinstance(value, list):
            value = ", ".join(value)
        print(f"{label}: {value}")
    print("\n" + "="*50 + "\n")

def main():
    search_terms = [
        "WordPress"
    ]
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    for term in search_terms:
        output_file = f"upwork_jobs_{term.replace(' ', '_').lower()}_{timestamp}.json"
        print(f"Scraping jobs for: {term}")
        
        jobs = scrape_upwork_jobs(term, output_file, pages=1)
        
        print(f"Scraped {len(jobs)} jobs for '{term}'")
        print(f"Results saved to {output_file}")
        
        if jobs:
            print("\nDetails of the first job:")
            print_job_details(jobs[0])
        
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()