import csv
import random

fields = ["Country", "State", "University Name", "Type of University", "Tie Up with University", "School",
          "Technologies/Courses Offered", "Course Types", "Unplaced %", "Corporate Tie Up", "Job Offering", "Internship",
          "Marketing Strategy", "Costing", "Hackathons", "Services Offered", "Scholarships", "Tier", "Ranking"]

countries = ["Australia", "UAE", "Saudi Arabia", "Kuwait", "Egypt", "Iran", "Turkey"]

# Mapping of states to universities for each country
universities_by_country_state = {
    "Australia": {
        "New South Wales": ["University of Sydney", "University of New South Wales", "Macquarie University"],
        "Victoria": ["University of Melbourne", "Monash University", "RMIT University"],
        "Queensland": ["University of Queensland", "Queensland University of Technology", "Griffith University"],
        "Western Australia": ["University of Western Australia", "Curtin University", "Murdoch University"],
        "South Australia": ["University of Adelaide", "Flinders University", "University of South Australia"],
        "Tasmania": ["University of Tasmania"],
        "Northern Territory": ["Charles Darwin University"],
        "Australian Capital Territory": ["Australian National University", "University of Canberra"]
    },
    "UAE": {
        "Dubai": ["American University in Dubai", "University of Dubai", "Zayed University"],
        "Abu Dhabi": ["Khalifa University", "Abu Dhabi University", "United Arab Emirates University"],
        "Sharjah": ["University of Sharjah", "American University of Sharjah"]
    },
    "Saudi Arabia": {
        "Riyadh": ["King Saud University", "Princess Nourah Bint Abdulrahman University"],
        "Jeddah": ["King Abdulaziz University"],
        "Mecca": ["Umm Al-Qura University"]
    },
    "Kuwait": {
        "Kuwait City": ["Kuwait University", "American University of Kuwait"]
    },
    "Egypt": {
        "Cairo": ["Cairo University", "American University in Cairo"],
        "Giza": ["Ain Shams University"],
        "Alexandria": ["Alexandria University"]
    },
    "Iran": {
        "Tehran": ["University of Tehran", "Sharif University of Technology"],
        "Isfahan": ["Isfahan University of Technology"],
        "Mashhad": ["Ferdowsi University of Mashhad"]
    },
    "Turkey": {
        "Istanbul": ["Istanbul University", "Bogazici University"],
        "Ankara": ["Middle East Technical University", "Ankara University"],
        "Izmir": ["Ege University"]
    }
}

types_of_universities = ["Public", "Private"]
schools = ["Engineering", "Business", "Degree", "Diploma", "IT", "Education"]
technologies = ["Computer Science", "Data Science", "Information Systems", "AI", "Cyber Security", "IoT", "Machine Learning", "Cloud Computing", "Robotics", "Big Data", "Analytics", "Software Engineering", "Networking", "Information Security", "Web Development", "Augmented Reality", "Virtual Reality", "Blockchain", "Quantum Computing"]
course_types = ["Bachelor", "Master", "Diploma", "Certificate", "PhD"]
marketing_strategies = ["Online Campaign", "Social Media Ads", "Print Media", "Email Marketing", "SEO", "Influencer Marketing", "PPC Ads", "TV Ads", "Content Marketing", "Radio Ads"]
costing_levels = ["High", "Medium", "Low"]
services_offered = ["Career Counseling", "Workshops", "Job Fairs", "Mentorship Programs", "Internship Programs", "Career Guidance", "Job Placement Services", "Seminars", "Webinars", "Hackathons", "Coding Bootcamps"]
tiers = ["Tier 1", "Tier 2"]

def generate_random_record(id):
    country = random.choice(countries)
    state = random.choice(list(universities_by_country_state[country].keys()))
    university = random.choice(universities_by_country_state[country][state])
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

num_records = 100000

with open('Educational_Institutions.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for i in range(num_records):
        csvwriter.writerow(generate_random_record(i))

print("CSV file generated successfully.")
