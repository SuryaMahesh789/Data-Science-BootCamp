import csv
import random

fields = ["Country", "State", "University Name", "Type of University", "Tie Up with University", "School",
          "Technologies/Courses Offered", "Course Types", "Unplaced %", "Corporate Tie Up", "Job Offering", "Internship",
          "Marketing Strategy", "Costing", "Hackathons", "Services Offered", "Scholarships", "Tier", "Ranking"]

countries = ["Australia", "UAE", "Saudi Arabia", "Kuwait", "Egypt", "Lebanon", "Syria", "Iraq", "Palestine", "Qatar", "Bahrain", "Oman", "Jordan"]

# Mapping of states to universities for each country
universities_by_country_state = {
    "Australia": {
        "Australian Capital Territory": ["Australian National University (ANU)", "University of Canberra"],
        "New South Wales": ["University of Sydney", "University of New South Wales (UNSW Sydney)", "University of Newcastle",
                            "University of Wollongong", "Macquarie University", "University of Technology Sydney (UTS)",
                            "Charles Sturt University", "Southern Cross University", "University of Divinity"],
        "Victoria": ["University of Melbourne", "Monash University", "RMIT University", "Deakin University", "La Trobe University", 
                     "Victoria University"],
        "Queensland": ["University of Queensland (UQ)", "Queensland University of Technology (QUT)", "Griffith University",
                       "Bond University", "Central Queensland University", "University of the Sunshine Coast"],
        "Western Australia": ["University of Western Australia (UWA)", "Curtin University", "Edith Cowan University (ECU)"],
        "South Australia": ["University of Adelaide", "University of South Australia (UniSA)", "Flinders University"],
        "Tasmania": ["University of Tasmania"],
        "Northern Territory": ["Charles Darwin University"],
        "Multi-State": ["Australian Catholic University (ACU)"]
    },
    "UAE": {
        "Dubai": ["American University in Dubai (AUD)", "University of Dubai", "Mohammed bin Rashid University of Medicine and Health Sciences",
                  "Dubai Institute of Design and Innovation (DIDI)", "University of the Arts London - Dubai", "British University in Dubai",
                  "Dubai Medical College", "Heriot-Watt University - Dubai"],
        "Abu Dhabi": ["Khalifa University", "Zayed University", "Abu Dhabi University"],
        "Sharjah": ["American University of Sharjah (AUS)", "University of Sharjah", "Skyline University College"],
        "Ajman": ["Gulf Medical University", "Gulf University"],
        "Ras Al Khaimah": ["American University of Ras Al Khaimah"],
        "Fujairah": ["University of Fujairah"]
    },
    "Saudi Arabia": {
        "Riyadh": ["King Saud University", "Prince Sultan University", "King Saud bin Abdulaziz University for Health Sciences",
                   "Al-Yamamah University", "Saudi Electronic University", "Al-Faisal University", "King Saud University College of Engineering",
                   "King Saud University College of Medicine", "King Saud University College of Business Administration"],
        "Jeddah": ["King Abdulaziz University", "Dar Al-Hekma University", "University of Business and Technology",
                   "King Abdulaziz University for Health Sciences"],
        "Dhahran": ["King Fahd University of Petroleum and Minerals"],
        "Abha": ["King Khalid University"],
        "Dammam": ["Imam Abdulrahman Bin Faisal University", "University of Dammam", "Prince Mohammad Bin Fahd University"],
        "Tabuk": ["University of Tabuk"],
        "Hail": ["University of Hail"],
        "Jazan": ["University of Jazan"],
        "Jubail": ["Jubail University College"],
        "Buraydah": ["Qassim University"]
    },
    "Kuwait": {
        "Kuwait City": ["Kuwait University", "American University of Kuwait", "University of the Middle East",
                        "Gulf University for Science and Technology", "Kuwait Institute for Scientific Research",
                        "Kuwait College of Science and Technology", "Kuwait College of Business Administration",
                        "Kuwait College of Medicine", "Kuwait College of Engineering", "Kuwait College of Art and Design"]
    },
    "Egypt": {
        "Giza": ["Cairo University"],
        "Cairo": ["American University in Cairo (AUC)", "Ain Shams University", "Helwan University"],
        "Alexandria": ["Alexandria University"],
        "Zagazig": ["University of Zagazig"],
        "Mansoura": ["University of Mansoura"],
        "Assiut": ["University of Assiut"],
        "Minya": ["University of Minya"],
        "Ismailia": ["Suez Canal University"],
        "South Valley": ["South Valley University"]
    },
    "Lebanon": {
        "Beirut": ["American University of Beirut (AUB)", "Lebanese University", "University of Saint Joseph (USJ)", 
                   "Lebanese American University (LAU)", "Saint George University", "Holy Spirit University of Kaslik (USEK)",
                   "Beirut Arab University", "International College", "Lebanese International University", 
                   "American University of Science and Technology", "Institut des Sciences Politiques et Relations Internationales (ISPRI)", 
                   "Université Libanaise de Sciences Appliquées (ULSA)", "Institut Superieur de Gestion (ISG)", 
                   "Institut National de Gestion", "Institut des Beaux-Arts", "Université Saint-Esprit de Kaslik", 
                   "Université de la Méditerranée", "Université des Sciences et Technologies du Liban (USTL)", 
                   "Université des Arts de Beyrouth", "Université des Langues et Sciences Sociales", 
                   "Université de Technologie et de Sciences Appliquées", "Université des Sciences et Technologies de Tripoli", 
                   "Université de Gestion de Tripoli", "Université de Damas", "Université de Science de Baabda", 
                   "Université de l'Institut de Management de la Méditerranée", "Université de Recherche Appliquée", 
                   "Université des Sciences de la Vie", "Université des Sciences de l'Ingénieur", 
                   "Université des Sciences de l'Information", "Université des Sciences de la Communication", 
                   "Université des Sciences de la Technologie", "Université des Sciences de l'Éducation", 
                   "Université des Sciences de la Santé", "Université des Sciences de l'Environnement", 
                   "Université des Sciences de l'Agriculture"],
        "Zouk Mosbeh": ["Notre Dame University (NDU)"],
        "Balamand": ["University of Balamand"],
        "Tripoli": ["Al Manar University of Tripoli", "Université des Sciences et Technologies de Tripoli", 
                    "Université de Gestion de Tripoli"],
        "Kaslik": ["Université Saint-Esprit de Kaslik"]
    },
    "Syria": {
        "Damascus": ["Damascus University"],
        "Aleppo": ["Aleppo University"],
        "Latakia": ["Tishreen University"],
        "Homs": ["University of Homs", "University of Al-Baath"],
        "Daraa": ["University of Daraa"],
        "Tartous": ["University of Tartous"],
        "Idlib": ["University of Idlib"],
        "Lattakia": ["University of Lattakia"],
        "Suwayda": ["University of Suwayda"],
        "Deir ez-Zor": ["University of Deir ez-Zor"],
        "Raqqa": ["University of Raqqa"],
        "Hasakah": ["University of Hasakah"],
        "Qamishli": ["University of Qamishli"],
        "Maarrat al-Nu'man": ["University of Maarrat al-Nu'man"],
        "Palmyra": ["University of Palmyra"],
        "Sheikh Said": ["University of Sheikh Said"],
        "Al-Munir": ["University of Al-Munir"],
        "Al-Salihiyah": ["University of Al-Salihiyah"],
        "Al-Ashrafiyah": ["University of Al-Ashrafiyah"],
        "Al-Jabal": ["University of Al-Jabal"],
        "Al-Raqqa": ["University of Al-Raqqa"],
        "Al-Mahfouz": ["University of Al-Mahfouz"],
        "Al-Quneitra": ["University of Al-Quneitra"],
        "Al-Nabek": ["University of Al-Nabek"],
        "Al-Tal": ["University of Al-Tal"],
        "Al-Zabadani": ["University of Al-Zabadani"],
        "Al-Maad": ["University of Al-Maad"],
        "Al-Safira": ["University of Al-Safira"],
        "Al-Bukamal": ["University of Al-Bukamal"],
        "Al-Khishta": ["University of Al-Khishta"]
    },
    "Iraq": {
        "Baghdad": ["University of Baghdad"],
        "Mosul": ["University of Mosul"],
        "Basra": ["University of Basra"],
        "Erbil": ["University of Erbil"],
        "Sulaimani": ["Sulaimani University"],
        "Duhok": ["University of Duhok"],
        "Kufa": ["University of Kufa"],
        "Nassiriya": ["University of Nassiriya"],
        "Babylon": ["University of Babylon"],
        "Amara": ["University of Amara"],
        "Anbar": ["University of Anbar"],
        "Kirkuk": ["University of Kirkuk"],
        "Najaf": ["University of Najaf"],
        "Qadissiyah": ["University of Qadissiyah"],
        "Samawah": ["University of Samawah"],
        "Tikrit": ["University of Tikrit"],
        "Thi-Qar": ["University of Thi-Qar"],
        "Wasit": ["University of Wasit"],
        "Sulaymaniyah": ["Sulaymaniyah University"]
    },
    "Palestine": {
        "Gaza": ["Islamic University of Gaza", "Al-Azhar University - Gaza"],
        "Ramallah": ["Birzeit University"],
        "Nablus": ["An-Najah National University"],
        "Hebron": ["Hebron University"],
        "Jericho": ["Al-Quds University"],
        "Bethlehem": ["Bethlehem University"],
        "Jenin": ["Arab American University"],
        "Tulkarm": ["Palestine Technical University - Kadoorie"]
    },
    "Qatar": {
        "Doha": ["Qatar University", "Carnegie Mellon University in Qatar", "Weill Cornell Medicine - Qatar",
                 "Texas A&M University at Qatar", "Georgetown University in Qatar", "Northwestern University in Qatar",
                 "Virginia Commonwealth University in Qatar", "College of the North Atlantic - Qatar", "University of Calgary in Qatar",
                 "Hamad Bin Khalifa University"]
    },
    "Bahrain": {
        "Manama": ["University of Bahrain", "Ahlia University", "Arabian Gulf University", "Royal University for Women",
                   "Bahrain Polytechnic", "Applied Science University - Bahrain", "Gulf University", "University College of Bahrain",
                   "Bahrain Institute of Banking and Finance (BIBF)", "Royal College of Surgeons in Ireland - Bahrain",
                   "American University of Bahrain (AUBH)", "Arab Open University - Bahrain"]
    },
    "Oman": {
        "Muscat": ["Sultan Qaboos University", "Oman Medical College", "Middle East College", "Majan University College",
                   "German University of Technology in Oman", "Oman College of Management & Technology"],
        "Salalah": ["Dhofar University", "Salalah College of Applied Sciences"],
        "Nizwa": ["University of Nizwa"],
        "Sohar": ["Sohar University"],
        "Sur": ["Sur University College"],
        "Barka": ["Al Buraimi University College"],
        "Ibra": ["Ibra College of Technology"]
    },
    "Jordan": {
        "Amman": ["University of Jordan", "Princess Sumaya University for Technology", "German-Jordanian University",
                  "Al-Zaytoonah University of Jordan", "Philadelphia University - Jordan", "Al Ahliyya Amman University",
                  "Middle East University - Jordan", "Applied Science Private University", "Jordan University of Science and Technology"],
        "Irbid": ["Yarmouk University"],
        "Aqaba": ["Aqaba University of Technology"],
        "Zarqa": ["Hashemite University", "Al-Zarqa Private University"],
        "Madaba": ["American University of Madaba"],
        "Ajloun": ["Ajloun National University"],
        "Mafraq": ["Al al-Bayt University"],
        "Karak": ["Mutah University"]
    }
}

# Function to generate a random university name for each state
def get_university(country, state):
    if country in universities_by_country_state and state in universities_by_country_state[country]:
        return random.choice(universities_by_country_state[country][state])
    return "Unknown University"

# Random data for each university
data = []

for country, states in universities_by_country_state.items():
    for state, universities in states.items():
        for university in universities:
            row = [
                country,
                state,
                university,
                "Public" if random.random() > 0.5 else "Private",
                random.choice(["Yes", "No"]),
                random.choice(["Engineering", "Business", "Arts", "Science"]),
                random.choice(["AI", "ML", "Data Science", "Cyber Security", "IoT"]),
                random.choice(["Full-time", "Part-time", "Online"]),
                round(random.uniform(5.0, 20.0), 2),  # Unplaced %
                random.choice(["Yes", "No"]),
                random.choice(["Yes", "No"]),
                random.choice(["Yes", "No"]),
                random.choice(["Digital", "Traditional", "Both"]),
                f"${random.randint(10000, 50000)}",
                random.choice(["Yes", "No"]),
                random.choice(["Consulting", "Training", "Both"]),
                random.choice(["Yes", "No"]),
                random.choice(["Tier 1", "Tier 2", "Tier 3"]),
                random.randint(1, 1000)
            ]
            data.append(row)

# Write to CSV file
filename = "Educational_Universities_data.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(data)

print(f"Data written to {filename} successfully.")
