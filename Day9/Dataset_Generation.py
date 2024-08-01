import csv
import random

fields = ["Country", "State", "University Name", "Type of University", "Tie Up with University", "School",
          "Technologies/Courses Offered", "Course Types", "Unplaced %", "Corporate Tie Up", "Job Offering", "Internship",
          "Marketing Strategy", "Costing", "Hackathons", "Services Offered", "Scholarships", "Tier", "Ranking"]

countries = ["Australia", "UAE", "Saudi Arabia", "Kuwait", "Egypt", "Iran", "Turkey"]
australian_states = ["New South Wales", "Victoria", "Queensland", "Western Australia", "South Australia", "Tasmania", "Northern Territory", "Australian Capital Territory"]
middle_east_states = ["Dubai", "Abu Dhabi", "Sharjah", "Riyadh", "Jeddah", "Mecca", "Kuwait City", "Cairo", "Giza", "Alexandria", "Tehran", "Isfahan", "Mashhad", "Istanbul", "Ankara", "Izmir"]
australian_universities = ["University of Sydney", "University of Melbourne", "Queensland University of Technology", "University of Western Australia", "University of Adelaide", "University of Technology Sydney", "Monash University", "Griffith University", "Macquarie University", "Curtin University"]
middle_east_universities = ["American University of Dubai", "King Saud University", "Kuwait University", "Cairo University", "University of Tehran", "Istanbul University"]
types_of_universities = ["Public", "Private"]
schools = ["Engineering", "Business", "Degree","Diploma", "IT",  "Education"]
technologies = ["Computer Science", "Data Science", "Information Systems", "AI", "Cyber Security", "IoT", "Machine Learning","Cloud Computing", "Robotics", "Big Data", "Analytics", "Software Engineering", "Networking", "Information Security", "Web Development", "Augmented Reality", "Virtual Reality", "Blockchain", "Quantum Computing"]
course_types = ["Bachelor", "Master", "Diploma", "Certificate", "PhD"]
marketing_strategies = ["Online Campaign", "Social Media Ads", "Print Media", "Email Marketing", "SEO", "Influencer Marketing", "PPC Ads", "TV Ads", "Content Marketing", "Radio Ads"]
costing_levels = ["High", "Medium", "Low"]
services_offered = ["Career Counseling", "Workshops", "Job Fairs", "Mentorship Programs", "Internship Programs", "Career Guidance", "Job Placement Services", "Seminars", "Webinars", "Hackathons", "Coding Bootcamps"]
tiers = ["Tier 1", "Tier 2"]

def generate_random_record(id):
    country = random.choice(countries)
    state = random.choice(australian_states if country == "Australia" else middle_east_states)
    university = random.choice(australian_universities if country == "Australia" else middle_east_universities)
    type_university = random.choice(types_of_universities)
    tie_up_university = random.choice(["Yes", "No"])
    school = random.choice(schools)
    technology = random.sample(technologies, random.randint(2, 5))
    course_type = random.sample(course_types, random.randint(1, 3))
    unplaced_percentage = random.randint(10, 30)
    corporate_tie_up = random.choice(["Yes", "No"])
    job_offering = random.choice(["Yes", "No"])
    internship = random.choice(["Yes", "No"])
    marketing_strategy = random.choice(marketing_strategies)
    costing = random.choice(costing_levels)
    hackathons = random.choice(["Yes", "No"])
    service = random.sample(services_offered, random.randint(1, 3))
    scholarship = random.choice(["Yes", "No"])
    tier = random.choice(tiers)
    ranking = random.randint(1, 100)
    
    return [
        country, state, university, type_university, tie_up_university, school,
        ", ".join(technology), ", ".join(course_type), f"{unplaced_percentage}%",
        corporate_tie_up, job_offering, internship, marketing_strategy, costing,
        hackathons, ", ".join(service), scholarship, tier, ranking
    ]

num_records = 1000000

with open('educational_institutions.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for i in range(num_records):
        csvwriter.writerow(generate_random_record(i))

print("CSV file generated successfully.")
