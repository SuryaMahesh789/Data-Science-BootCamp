import csv
import random

fields = ["Country", "State", "University Name", "Type of University", "Tie Up with University", "School",
          "Technologies/Courses Offered", "Course Types", "Unplaced %", "Corporate Tie Up", "Job Offering", "Internship",
          "Marketing Strategy", "Costing", "Hackathons", "Services Offered", "Scholarships", "Tier", "Ranking"]


countries = [
    "Australia", "UAE", "Saudi Arabia", "Kuwait", "Egypt", "Lebanon", "Syria", "Iraq", 
    "Palestine", "Qatar", "Bahrain", "Oman", "Jordan",
    "Afghanistan", "Armenia", "Azerbaijan", "Bangladesh", "Bhutan", "Brunei", "Cambodia", 
    "China", "Cyprus", "Georgia", "Indonesia", "Iran", "Israel", "Japan", "Kazakhstan", 
    "Kyrgyzstan", "Laos", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", 
    "North Korea", "Pakistan", "Philippines", "Singapore", "South Korea", "Sri Lanka", 
    "Taiwan", "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", 
    "Uzbekistan", "Vietnam", "Yemen"]


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

    "Armenia": {
        "Yerevan": [
            "Yerevan State University", 
            "National Polytechnic University of Armenia", 
            "Armenian State Pedagogical University", 
            "Yerevan State Medical University", 
            "Armenian State University of Economics", 
            "Yerevan State University of Architecture and Construction", 
            "Yerevan Brusov State University of Languages and Social Sciences", 
            "Yerevan Komitas State Conservatory", 
            "Armenian National Agrarian University", 
            "American University of Armenia", 
            "French University in Armenia", 
            "Russian-Armenian (Slavonic) University", 
            "Eurasia International University", 
            "European University", 
            "Haybusak University of Yerevan", 
            "Yerevan Gladzor University", 
            "International Scientific-Educational Center of NAS RA", 
            "Saint Teresa Medical University", 
            "Yerevan University of Management and Information Technologies", 
            "University of Traditional Medicine", 
            "Anania Shirakatsi University", 
            "Armenian State Institute of Physical Culture", 
            "Ararat University", 
            "King Danylo University", 
            "Yerevan Institute of Humanities", 
            "Yerevan International Linguistic and Regional Studies University"
        ],
        "Gavar": ["Gavar State University"],
        "Gyumri": [
            "Gyumri State Pedagogical Institute", 
            "Shirak State University"
        ],
        "Vanadzor": [
            "Vanadzor State University", 
            "Mkhitar Gosh Armenian-Russian International University"
        ],
        "Stepanakert": [
            "Artsakh State University", 
            "Mesrop Mashtots University"
        ]
    },

    "Azerbaijan": {
        "Baku": [
            "Baku State University", 
            "Azerbaijan State Oil and Industry University", 
            "Azerbaijan Technical University", 
            "Azerbaijan University of Architecture and Construction", 
            "Azerbaijan State Pedagogical University", 
            "Azerbaijan Medical University", 
            "Azerbaijan University of Languages", 
            "Khazar University", 
            "Baku Engineering University", 
            "Azerbaijan State University of Economics", 
            "Azerbaijan State University of Culture and Arts", 
            "ADA University", 
            "Qafqaz University", 
            "Western University", 
            "Baku Business University", 
            "Azerbaijan University of Architecture and Construction", 
            "Khazar University", 
            "Istanbul University (Azerbaijan Branch)", 
            "Azerbaijan University of Tourism and Management", 
            "Baku Higher Oil School", 
            "Caspian University", 
            "Azerbaijan State University of Economics (Private Branch)", 
            "East University", 
            "Baku International University", 
            "Azerbaijan State Institute of Physical Culture and Sports (Private Branch)"
        ],
        "Sumgayit": ["Sumgayit State University"],
        "Ganja": [
            "Ganja State University", 
            "Ganja State University (Private Branch)"
        ],
        "Lankaran": ["Lankaran State University"],
        "Nakhchivan": ["Nakhchivan State University"]
    },


    "Bahrain": {
        "Sakhir": ["University of Bahrain"],
        "Manama": [
            "Arab Open University - Bahrain Branch", 
            "Bahrain University", 
            "Ahlia University", 
            "University College of Bahrain", 
            "University of Kalamoon", 
            "College of Health Sciences", 
            "Bahrain Institute of Banking and Finance", 
            "Gulf University", 
            "Dhofar University - Bahrain Branch", 
            "Ibn Khaldun University", 
            "Bahrain Polytechnic"
        ],
        "Riffa": [
            "Royal University for Women", 
            "American University of Bahrain"
        ]
    },

    "Bangladesh": {
        "Dhaka": [
            "University of Dhaka", 
            "Bangladesh University of Engineering and Technology (BUET)", 
            "Bangladesh University of Textiles (BUTEX)", 
            "North South University", 
            "BRAC University", 
            "United International University", 
            "East West University", 
            "Daffodil International University", 
            "Ahsanullah University of Science and Technology", 
            "Green University of Bangladesh", 
            "American International University-Bangladesh (AIUB)", 
            "University of Liberal Arts Bangladesh (ULAB)", 
            "Monash University Malaysia - Dhaka Campus", 
            "Uttara University", 
            "World University of Bangladesh", 
            "International University of Business Agriculture and Technology (IUBAT)", 
            "Bangladesh University", 
            "Central Women's University"
        ],
        "Savar": ["Jahangirnagar University"],
        "Rajshahi": [
            "University of Rajshahi", 
            "Rajshahi University of Engineering and Technology (RUET)"
        ],
        "Chittagong": [
            "University of Chittagong", 
            "Southern University Bangladesh", 
            "University of Science and Technology Chittagong (USTC)", 
            "BGC Trust University Bangladesh"
        ],
        "Khulna": ["Khulna University"],
        "Sylhet": [
            "Sylhet Agricultural University", 
            "Shahjalal University of Science and Technology (SUST)", 
            "Sylhet International University"
        ],
        "Dinajpur": ["Hajee Mohammad Danesh Science and Technology University"],
        "Patuakhali": ["Patuakhali Science and Technology University"],
        "Comilla": ["Comilla University"],
        "Moulvibazar": ["Jatiyo Kabi Kazi Nazrul Islam University"],
        "Gazipur": [
            "National University", 
            "Bangladesh Open University"
        ],
        "Barisal": ["Barisal University"],
        "Rangpur": ["Begum Rokeya University"],
        "Tangail": ["Mawlana Bhashani Science and Technology University"],
        "Kishoreganj": ["Jatiyo Sanskrit University"],
        "Mymensingh": ["Bangladesh Agricultural University"],
        "Chandpur": ["Chandpur Government College"],
        "Bogura": ["Pundra University of Science & Technology"]
    },

    "Bhutan": {
        "Thimphu": [
            "Royal University of Bhutan (RUB)",
            "Royal Thimphu College (RTC)",
            "Palden Drukpa College",
            "Khesar Gyalpo University of Medical Sciences of Bhutan"
        ],
        "Phuentsholing": ["College of Science and Technology (CST)"],
        "Lobesa": ["College of Natural Resources (CNR)"],
        "Kanglung": ["Sherubtse College"],
        "Dewathang": ["Jigme Namgyel Engineering College (JNEC)"]
    },

    "Brunei": {
        "Bandar Seri Begawan": [
            "Universiti Brunei Darussalam (UBD)",
            "Universiti Teknologi Brunei (UTB)",
            "Politeknik Brunei (PB)",
            "Institut Pendidikan Teknikal Brunei (IPTB)",
            "Brunei University of Technology",
            "Brunei International School"
        ]
    },

    "Cambodia": {
        "Phnom Penh": [
            "Royal University of Phnom Penh",
            "Royal University of Law and Economics",
            "Royal University of Agriculture",
            "University of Health Sciences",
            "Institute of Technology of Cambodia",
            "National University of Management",
            "Paññāsāstra University of Cambodia",
            "Norton University",
            "Western University",
            "Limkokwing University of Creative Technology",
            "Cambodian Mekong University",
            "University of Cambodia",
            "Asia Euro University",
            "Zaman University",
            "International University"
        ],
        "Battambang": ["Build Bright University"]
    },

    "Yemen": {
        "Sana'a": [
            "University of Sana'a",
            "Saba University",
            "Yemen University",
            "University of Science and Technology (UST)",
            "Al-Eman University",
            "Al-Rahma University",
            "Al-Hekma University",
            "Ibn Sina University",
            "Al-Nasser University",
            "Sana'a International University"
        ],
        "Aden": ["Aden University"],
        "Taiz": ["Taiz University", "Al-Zahra University", "Al-Saeed University"],
        "Ibb": ["Ibb University"],
        "Al Hudaydah": ["Hodeidah University"],
        "Al Bayda": ["Al-Baydha University"],
        "Dhamar": ["Dhamar University"],
        "Hadhramaut": ["Hadhramout University"],
        "Al Mukalla": ["Al-Mukalla University"]
    },


    "Vietnam": {
        "Hanoi": [
            "Hanoi University of Science and Technology",
            "Hanoi University",
            "University of Hanoi",
            "University of Education, Hanoi",
            "Thuy Loi University",
            "Military Medical University",
            "National Economics University",
            "Vietnam National University, Hanoi",
            "FPT University"
        ],
        "Da Nang": [
            "University of Danang",
            "American University in Vietnam",
            "Central International University"
        ],
        "Ho Chi Minh City": [
            "Ho Chi Minh City University of Technology",
            "Nong Lam University",
            "Hochiminh City University of Pedagogy",
            "Vietnam National University, Ho Chi Minh City",
            "University of Agriculture and Forestry",
            "University of International Business and Economics",
            "Hong Bang International University",
            "Van Lang University",
            "Hoa Sen University",
            "Troy University Vietnam",
            "RMIT University Vietnam",
            "University of Finance and Marketing"
        ],
        "Hue": ["Hue University"],
        "Can Tho": ["Can Tho University"],
        "Vinh": ["Vinh University"],
        "Nam Dinh": ["Nam Dinh University of Nursing"]
    },

    "China": {
        "Beijing": [
            "Peking University",
            "Tsinghua University",
            "Beijing Normal University",
            "Beijing University of International Business and Economics"
        ],
        "Shanghai": [
            "Fudan University",
            "Shanghai Jiao Tong University",
            "Tongji University",
            "East China Normal University",
            "Shanghai International Studies University (SISU)"
        ],
        "Zhejiang": [
            "Zhejiang University",
            "Wenzhou-Kean University",
            "Ningbo University of Technology"
        ],
        "Jiangsu": ["Xi'an Jiaotong-Liverpool University"],
        "Anhui": ["University of Science and Technology of China"],
        "Hubei": [
            "Wuhan University",
            "Huazhong University of Science and Technology"
        ],
        "Guangdong": [
            "Sun Yat-sen University",
            "United International College (Beijing Normal University-Hong Kong Baptist University)",
            "Shenzhen University (certain departments and colleges)"
        ],
        "Sichuan": ["Sichuan University"],
        "Shaanxi": ["Xi'an Jiaotong University"],
        "Shandong": ["Shandong University"],
        "Tianjin": ["Nankai University"],
        "Heilongjiang": ["Harbin Institute of Technology"],
        "Fujian": ["Xiamen University"],
        "Hunan": ["Central South University"],
        "Hangzhou": ["Hangzhou Dianzi University (certain departments)"],
        "Beijing": ["Beijing University of International Business and Economics (Private/Public)"]
    },

    "Uzbekistan": {
        "Tashkent": [
            "Tashkent State Technical University",
            "Tashkent State University of Economics",
            "Tashkent University of Information Technologies",
            "National University of Uzbekistan",
            "Uzbekistan State World Languages University",
            "Tashkent Medical Academy",
            "Uzbek State Institute of Arts and Culture",
            "Urgench State University",
            "Tashkent Institute of Irrigation and Agricultural Mechanization Engineers",
            "Institute of Nuclear Physics",
            "Uzbekistan State University of Law",
            "Westminster International University in Tashkent",
            "Inha University in Tashkent",
            "Tashkent International University of Technology",
            "Tashkent Institute of Finance",
            "Uzbekistan-Japan Center for Human Development",
            "Korean University of International Studies"
        ],
        "Samarkand": ["Samarkand State University"],
        "Bukhara": ["Bukhara State University"],
        "Andijan": ["Andijan State University"],
        "Fergana": ["Fergana State University"],
        "Namangan": ["Namangan State University"],
        "Karshi": ["Karshi State University"]
    },


    "Cyprus": {
        "Nicosia": [
            "University of Cyprus",
            "Open University of Cyprus",
            "European University Cyprus",
            "University of Nicosia",
            "Frederick University"
        ],
        "Limassol": ["Cyprus University of Technology", "Frederick University"],
        "Paphos": ["Neapolis University Pafos"],
        "Larnaca": ["UCLan Cyprus (University of Central Lancashire)"]
    },

    "United Arab Emirates": {
        "Al Ain": [
            "United Arab Emirates University (UAEU)",
            "Al Ain University of Science and Technology"
        ],
        "Sharjah": [
            "American University of Sharjah (AUS)",
            "University of Sharjah"
        ],
        "Abu Dhabi": [
            "Zayed University",
            "Abu Dhabi University (ADU)",
            "Paris-Sorbonne University Abu Dhabi",
            "NYU Abu Dhabi"
        ],
        "Dubai": [
            "Dubai Islamic University",
            "American University in Dubai (AUD)",
            "British University in Dubai (BUiD)",
            "Dubai University of Technology",
            "Canadian University Dubai (CUD)",
            "University of Wollongong in Dubai (UOWD)",
            "Middlesex University Dubai",
            "Heriot-Watt University Dubai"
        ]
    },

    "Georgia": {
        "Tbilisi": [
            "Ivane Javakhishvili Tbilisi State University",
            "Georgian Technical University",
            "Ilia State University",
            "Tbilisi State Medical University",
            "Sokhumi State University",
            "Shota Rustaveli Theatre and Film Georgian State University",
            "Georgian American University",
            "Free University of Tbilisi",
            "International Black Sea University",
            "Grigol Robakidze University",
            "Georgian Institute of Public Affairs (GIPA)",
            "European University",
            "David Tvildiani Medical University",
            "University of Georgia (UG)",
            "New Vision University"
        ],
        "Batumi": ["Batumi Shota Rustaveli State University"],
        "Kutaisi": [
            "Akaki Tsereteli State University",
            "Kutaisi University"
        ],
        "Tbilisi": ["Georgian State University of Physical Education and Sport"]
    },

    "Turkmenistan": {
        "Ashgabat": [
            "Turkmenistan State University",
            "Turkmen State Institute of Economics and Management",
            "Turkmen Agricultural University",
            "Turkmen State Institute of Architecture and Construction",
            "Turkmen State Institute of Physical Culture and Sport",
            "Turkmen State Medical University",
            "Turkmen State University of World Languages",
            "Turkmen State Institute of Technology",
            "International Turkmen University"
        ],
        "Various locations": ["State Pedagogical Institute"],
        "Ashgabat": ["Turkmen State Institute of Business and Management"]
    },


    "Indonesia": {
        "Depok": [
            "University of Indonesia (Universitas Indonesia)",
            "Gunadarma University"
        ],
        "Yogyakarta": ["Gadjah Mada University (Universitas Gadjah Mada)"],
        "Bandung": [
            "Bandung Institute of Technology (Institut Teknologi Bandung)",
            "Padjadjaran University (Universitas Padjadjaran)",
            "Telkom University",
            "Maranatha Christian University (Universitas Kristen Maranatha)"
        ],
        "Bogor": ["Bogor Agricultural University (Institut Pertanian Bogor)"],
        "Surabaya": [
            "Airlangga University (Universitas Airlangga)",
            "Sepuluh Nopember Institute of Technology (Institut Teknologi Sepuluh Nopember)",
            "Petra Christian University (Universitas Kristen Petra)"
        ],
        "Semarang": ["Diponegoro University (Universitas Diponegoro)"],
        "Makassar": ["Hasanuddin University (Universitas Hasanuddin)"],
        "Malang": ["Brawijaya University (Universitas Brawijaya)"],
        "Padang": ["Andalas University (Universitas Andalas)"],
        "Palembang": ["Sriwijaya University (Universitas Sriwijaya)"],
        "Jakarta": [
            "Binus University (Bina Nusantara University)",
            "Atma Jaya Catholic University of Indonesia (Universitas Katolik Indonesia Atma Jaya)",
            "Trisakti University (Universitas Trisakti)"
        ],
        "Tangerang": [
            "Pelita Harapan University (Universitas Pelita Harapan)",
            "Swiss German University"
        ],
        "Bekasi": ["President University"],
        "Yogyakarta": ["Universitas Islam Indonesia"]
    },

    "Turkey": {
        "Ankara": [
            "Ankara University",
            "Middle East Technical University (METU)",
            "Hacettepe University",
            "Gazi University",
            "Bilkent University",
            "Kırıkkale University",
            "Çukurova University"
        ],
        "Istanbul": [
            "Boğaziçi University",
            "Istanbul University",
            "Istanbul Technical University (ITU)",
            "Yeditepe University",
            "Sabancı University",
            "Koç University",
            "Istanbul Bilgi University",
            "Istanbul Sehir University",
            "Istanbul University - Cerrahpaşa",
            "Bahçeşehir University",
            "Üsküdar University",
            "Acıbadem University",
            "İstanbul Kültür University",
            "Maltepe University",
            "Beykoz University",
            "Nişantaşı University",
            "Doğuş University",
            "Kadir Has University",
            "Altınbaş University",
            "American University of Turkey"
        ],
        "Izmir": [
            "University of Izmir",
            "Ege University",
            "Dokuz Eylül University"
        ],
        "Konya": ["Selçuk University"],
        "Sakarya": ["Sakarya University"],
        "Kocaeli": ["Kocaeli University"],
        "Trabzon": ["Karadeniz Technical University"],
        "Mardin": ["Mardin Artuklu University"],
        "Kütahya": ["Kütahya Dumlupınar University"],
        "Aksaray": ["Aksaray University"],
        "Kocaeli": ["Kocaeli University"]
    },

    "Iran": {
        "Tehran": [
            "University of Tehran",
            "Sharif University of Technology",
            "Amirkabir University of Technology (Tehran Polytechnic)",
            "Iran University of Science and Technology",
            "Shahid Beheshti University",
            "Tarbiat Modares University",
            "K. N. Toosi University of Technology",
            "Allameh Tabataba'i University",
            "University of Science and Culture"
        ],
        "Mashhad": ["Ferdowsi University of Mashhad"],
        "Isfahan": ["Isfahan University of Technology", "University of Isfahan"],
        "Tabriz": ["University of Tabriz", "Tabriz Islamic Art University"],
        "Yazd": ["Yazd University"],
        "Zahedan": ["University of Sistan and Baluchestan"],
        "Hamedan": ["Bu-Ali Sina University"],
        "Rasht": ["University of Guilan"],
        "Karaj": ["Kharazmi University"],
        "Babolsar": ["University of Mazandaran"],
        "Semnan": ["Semnan University"],
        "Tehran": [
            "Islamic Azad University",
            "Alzahra University",
            "Imam Sadiq University",
            "Shahid Rajaee Teacher Training University",
            "University of Medical Sciences",
            "Tehran University of Medical Sciences",
            "Shahid Beheshti University of Medical Sciences"
        ]
    },

    "Iraq": {
        "Baghdad": [
            "University of Baghdad",
            "Al-Mustansiriya University",
            "University of Technology, Iraq",
            "American University of Iraq, Baghdad",
            "Al-Nahrain University",
            "Baghdad College of Economic Sciences University",
            "Al-Turath University College",
            "Al-Rafidain University College",
            "Al-Ma'mun University College",
            "Al-Mansour University College"
        ],
        "Basrah": ["University of Basrah"],
        "Mosul": ["University of Mosul", "Al-Hadba University College"],
        "Najaf": ["University of Kufa"],
        "Karbala": ["University of Karbala"],
        "Baqubah": ["University of Diyala"],
        "Ramadi": ["University of Anbar"],
        "Hillah": ["University of Babylon"],
        "Kirkuk": ["University of Kirkuk"],
        "Tikrit": ["University of Tikrit"],
        "Sulaymaniyah": [
            "University of Sulaimani",
            "American University of Iraq, Sulaimani",
            "Komar University of Science and Technology",
            "University of Human Development"
        ],
        "Duhok": [
            "University of Duhok",
            "Cihan University"
        ],
        "Al Diwaniyah": ["University of Al-Qadisiyah"],
        "Nasiriyah": ["University of Thi-Qar"],
        "Amarah": ["University of Misan"],
        "Kut": ["University of Wasit"],
        "Samarra": ["University of Samarra"],
        "Fallujah": ["University of Fallujah"],
        "Erbil": [
            "Cihan University",
            "SABIS® University",
            "Lebanese French University",
            "Catholic University in Erbil",
            "University of Kurdistan Hewlêr"
        ]
    },

    "Israel": {
        "Jerusalem": [
            "Hebrew University of Jerusalem",
            "The Jerusalem College of Technology",
            "Hadassah Academic College"
        ],
        "Tel Aviv": [
            "Tel Aviv University",
            "The Israel College of Applied Science"
        ],
        "Haifa": ["Technion – Israel Institute of Technology", "University of Haifa"],
        "Be'er Sheva": ["Ben-Gurion University of the Negev"],
        "Ramat Gan": ["Bar-Ilan University", "Shenkar College of Engineering and Design"],
        "Ra'anana": ["Open University of Israel"],
        "Ariel": ["Ariel University"],
        "Herzliya": [
            "Interdisciplinary Center (IDC) Herzliya",
            "Efi Arazi School of Computer Science, IDC Herzliya"
        ],
        "Rishon LeZion": ["The College of Management Academic Studies"],
        "Kinneret": ["Kinneret Academic College"]
    },


    "Timor-Leste": {
        "Dili": [
            "Universidade Nacional de Timor-Leste (UNTL)",
            "Universidade de La Salle"
        ]
    },
    "Thailand": {
        "Bangkok": [
            "Chulalongkorn University",
            "Kasetsart University",
            "Thammasat University",
            "Srinakharinwirot University",
            "Assumption University (ABAC)",
            "Bangkok University",
            "Dhurakij Pundit University",
            "Mahanakorn University of Technology",
            "Siam University",
            "Stamford International University",
            "University of the Thai Chamber of Commerce (UTCC)"
        ],
        "Nakhon Pathom": ["Mahidol University", "Christian University of Thailand"],
        "Chiang Mai": ["Chiang Mai University"],
        "Khon Kaen": ["Khon Kaen University"],
        "Hat Yai": ["Prince of Songkla University"],
        "Chonburi": ["Burapha University"],
        "Chiang Rai": ["Mae Fah Luang University"],
        "Phitsanulok": ["Naresuan University"],
        "Pathum Thani": ["Asian Institute of Technology (AIT)", "Rangsit University"],
        "Songkhla": ["Songkhla Rajabhat University"],
        "Chachoengsao": ["Eastern Asia University"],
        "Hua Hin": ["Webster University Thailand"],
        "Various locations": [
            "Rajabhat University",
            "Rajamangala University of Technology"
        ]
    },


    "Japan": {
        "Tokyo": [
            "University of Tokyo (Tokyo Daigaku)",
            "Hitotsubashi University",
            "Tokyo Institute of Technology (Tokyo Kogyo Daigaku)",
            "Tokyo University of Foreign Studies",
            "Nihon University",
            "Keio University",
            "Waseda University",
            "Sophia University",
            "Tokyo University of the Arts",
            "Aoyama Gakuin University",
            "Chuo University",
            "Tokyo University of Science",
            "Showa Pharmaceutical University",
            "Juntendo University",
            "Musashi University",
            "Nihon University",
            "International Christian University",
            "Shibaura Institute of Technology"
        ],
        "Kyoto": [
            "Kyoto University",
            "Ritsumeikan University",
            "Doshisha University"
        ],
        "Osaka": [
            "Osaka University",
            "Osaka University of Economics",
            "Kinki University"
        ],
        "Sendai": ["Tohoku University"],
        "Nagoya": ["Nagoya University"],
        "Fukuoka": ["Kyushu University"],
        "Sapporo": ["Hokkaido University"],
        "Kobe": ["Kobe University"],
        "Okayama": ["Okayama University"],
        "Shizuoka": ["Shizuoka University"],
        "Chiba": ["Chiba University"],
        "Yokohama": ["Yokohama National University"],
        "Gifu": ["Gifu University"],
        "Matsuyama": ["Ehime University"],
        "Nagasaki": ["Nagasaki University"],
        "Tama": ["Tama Art University"]
    },
    "Jordan": {
        "Amman": [
            "University of Jordan",
            "University of Petra",
            "Princess Sumaya University for Technology",
            "The University of Applied Sciences",
            "Amman Arab University",
            "Abdullah II Design and Development Bureau University",
            "Al-Zaytoonah University of Jordan",
            "Arab Open University",
            "International University for Science and Technology",
            "Al-Isra University",
            "University of Modern Sciences",
            "Amman University for Technology"
        ],
        "Irbid": [
            "Jordan University of Science and Technology",
            "Yarmouk University"
        ],
        "Zarqa": ["Hashemite University"],
        "Karak": ["Mutah University"],
        "Salt": ["Al-Balqa Applied University"],
        "Ma'an": [
            "University of Ma'an",
            "Al-Hussein Bin Talal University"
        ]
    },


    "Tajikistan": {
        "Dushanbe": [
            "Tajik National University",
            "Tajik Technical University",
            "Tajik State University of Law",
            "Tajik State University of Commerce",
            "Dushanbe Medical University",
            "Agricultural University of Tajikistan",
            "Institute of Pedagogy and Psychology",
            "University of Central Asia",
            "Tajik Institute of Entrepreneurship and Service",
            "International University of Central Asia"
        ],
        "Khorog": [
            "Khorog State University",
            "Pamir State University"
        ],
        "Khujand": ["Khujand State University"]
    },
    "Taiwan": {
        "Taipei": [
            "National Taiwan University (NTU)",
            "National Yang Ming Chiao Tung University (NYCU)",
            "National Taipei University (NTPU)",
            "National Taiwan University of Science and Technology (NTUST)",
            "National Taiwan Normal University (NTNU)",
            "Soochow University",
            "Ming Chuan University"
        ],
        "Tainan": [
            "National Cheng Kung University (NCKU)",
            "Chang Jung Christian University"
        ],
        "Hsinchu": ["National Tsing Hua University (NTHU)"],
        "Taoyuan": [
            "National Central University (NCU)",
            "Chung Yuan Christian University (CYCU)"
        ],
        "Kaohsiung": [
            "National Sun Yat-sen University (NSYSU)",
            "Shu-Te University",
            "National Kaohsiung University of Science and Technology (NKUST)"
        ],
        "Taichung": [
            "National Chung Hsing University (NCHU)",
            "Asia University"
        ],
        "Hualien": ["National Dong Hwa University (NDHU)"],
        "Pingtung": ["National Pingtung University (NPTU)"],
        "Tamsui": [
            "Tamkang University",
            "Aletheia University"
        ]
    },


    "Kazakhstan": {
        "Almaty": [
            "Al-Farabi Kazakh National University",
            "Kazakh National Technical University (KazNTU)",
            "Kazakh-British Technical University",
            "Kazakh National Medical University",
            "Kazakh American University",
            "KIMEP University",
            "International University of Almaty",
            "Almaty Management University",
            "Kazakh Humanitarian Law University",
            "International School of Medicine"
        ],
        "Nur-Sultan": [
            "L.N. Gumilyov Eurasian National University",
            "Nazarbayev University",
            "Astana International University"
        ],
        "Petropavl": ["North Kazakhstan State University"],
        "Uralsk": ["West Kazakhstan Innovative Technological University"],
        "Shymkent": ["South Kazakhstan State Pedagogical University"],
        "Aktobe": ["Aktobe Regional State University"],
        "Pavlodar": ["Pavlodar State University"],
        "Karaganda": ["Karaganda State Technical University"],
        "Taraz": ["Taraz Regional University"],
        "Semey": ["Semey Medical University", "Shakarim University"],
        "Kokshetau": ["University of Kokshetau"],
        "Taldykorgan": ["Zhetysu State University"],
        "Atyrau": ["Atyrau University of Oil and Gas"]
    },
    "Kuwait": {
        "Kuwait City": [
            "Kuwait University",
            "The Public Authority for Applied Education and Training (PAAET)",
            "Kuwait International University",
            "University of Sharjah (Kuwait Campus)",
            "Arab Open University",
            "Alhadi University College",
            "New Kuwait University College",
            "College of Basic Education"
        ],
        "Egaila": ["American University of the Middle East"],
        "Mubarak Al-Abdullah": ["Australian College of Kuwait"],
        "Hawally": ["Gulf University for Science and Technology"]
    },
    "Syria": {
        "Damascus": [
            "University of Damascus",
            "American University of Science and Technology (AUST)",
            "Syrian Private University (SPU)",
            "Arab International University (AIU)",
            "Al-Maaref University",
            "Sham Private University"
        ],
        "Aleppo": ["University of Aleppo"],
        "Latakia": ["Tishreen University"],
        "Homs": ["University of Homs", "Al-Baath University"],
        "Daraa": ["University of Daraa"],
        "Qamishli": ["University of Qamishli"],
        "Deir ez-Zor": ["University of Deir ez-Zor"],
        "Hasaka": ["University of Hasaka"]
    },
    "South Korea": {
        "Seoul": [
            "Seoul National University",
            "Konkuk University",
            "Kyung Hee University",
            "Sungkyunkwan University",
            "Hanyang University",
            "Yonsei University",
            "Ewha Womans University",
            "Sogang University",
            "Sejong University",
            "Sookmyung Women's University",
            "Namseoul University",
            "Myongji University",
            "Seoul Women's University",
            "Korea University",
            "University of Seoul",
            "Dongguk University"
        ],
        "Daejeon": [
            "Korea Advanced Institute of Science and Technology (KAIST)",
            "Chungnam National University"
        ],
        "Pohang": ["Pohang University of Science and Technology (POSTECH)"],
        "Ulsan": ["University of Ulsan"],
        "Jinju": ["Gyeongsang National University"],
        "Jeju": ["Jeju National University"],
        "Cheongju": ["Chungbuk National University"],
        "Incheon": ["Incheon National University"],
        "Gangneung and Wonju": ["Gangneung-Wonju National University"],
        "Chuncheon": ["Kangwon National University"],
        "Seongnam": ["Seongnam University"],
        "Asan": ["Hoseo University"]
    },
    "Singapore": {
        "Singapore": [
            "National University of Singapore (NUS)",
            "Nanyang Technological University (NTU)",
            "Singapore Management University (SMU)",
            "Singapore University of Technology and Design (SUTD)",
            "Singapore University of Social Sciences (SUSS)",
            "Singapore Institute of Technology (SIT)",
            "Singapore Institute of Management (SIM)",
            "Singapore University of Business and Technology (SUBT)",
            "Singapore University of the Arts (SUA)",
            "Shatec Institutes",
            "Raffles University"
        ]
    },


    "Kyrgyzstan": {
        "Bishkek": [
            "Kyrgyz National University",
            "Kyrgyz State Technical University",
            "Kyrgyz State Medical Academy",
            "Kyrgyz-Russian Slavic University",
            "Kyrgyz State University of Construction, Transport, and Architecture",
            "American University of Central Asia",
            "International University of Kyrgyzstan",
            "Kyrgyz-Turkish Manas University",
            "University of Central Asia",
            "Kyrgyz Economic University",
            "Bishkek Humanities University",
            "Slavonic University",
            "Istanbul University of Kyrgyzstan",
            "Kyrgyz National University of Arts"
        ],
        "Osh": ["Osh State University"],
        "Karakol": ["Issyk-Kul State University"],
        "Batken": ["Batken State University"],
        "Naryn": ["Naryn State University"],
        "Talas": ["Talas State University"]
    },
    "Saudi Arabia": {
        "Riyadh": [
            "King Saud University (KSU)",
            "King Saud bin Abdulaziz University for Health Sciences (KSAU-HS)",
            "Prince Sultan University (PSU)",
            "Al-Yamamah University",
            "Al-Faisal University",
            "American International University (AIU)",
            "Arab Open University",
            "Saudi Electronic University (SEU)"
        ],
        "Jeddah": [
            "King Abdulaziz University (KAU)",
            "University of Jeddah",
            "Dar Al-Hekma University",
            "Effat University"
        ],
        "Dhahran": ["King Fahd University of Petroleum and Minerals (KFUPM)"],
        "Abha": ["King Khalid University (KKU)"],
        "Dammam": ["Imam Abdulrahman Bin Faisal University (IAU)"],
        "Manama": ["Kingdom University"],
        "Tabuk": ["Tabuk University"],
        "Buraydah": ["Qassim University"],
        "Jazan": ["Jazan University"],
        "Hail": ["Hail University"],
        "Najran": ["Najran University"],
        "Al Khobar": ["Prince Mohammad Bin Fahd University (PMU)"],
        "Sakakah": ["Al-Jouf University"],
        "Arar": ["Northern Borders University"],
        "Bisha": ["University of Bisha"]
    },


    "Laos": {
        "Vientiane": [
            "National University of Laos",
            "Lao National Institute of Public Health",
            "University of Health Sciences",
            "RATANAK University",
            "Vientiane College",
            "University of Laos",
            "Khon Kaen University International College",
            "Lao-American College",
            "Asia-Pacific International University",
            "Lao University of Commerce"
        ],
        "Pakse": ["Champasak University"],
        "Savannakhet": ["Savannakhet University"],
        "Luang Prabang": ["Luang Prabang University"],
        "Khong District, Champasak": ["Don Sahong University"]
    },
    "Qatar": {
        "Doha": [
            "Qatar University (QU)",
            "College of the North Atlantic - Qatar (CNA-Q)",
            "Doha Institute for Graduate Studies (DI)",
            "Qatar University of Science and Technology",
            "University of Calgary in Qatar (UCQ)",
            "Weill Cornell Medicine-Qatar (WCM-Q)",
            "Georgetown University in Qatar",
            "Northwestern University in Qatar"
        ]
    },


    "Lebanon": {
        "Beirut": [
            "Lebanese University (Université Libanaise)",
            "American University of Beirut (AUB)",
            "Lebanese American University (LAU)",
            "University of Saint Joseph (USJ)",
            "Beirut Arab University (BAU)",
            "Lebanese International University (LIU)",
            "International University of Beirut (IUB)",
            "Modern University for Business and Science (MUBS)"
        ],
        "Baabda": ["Université Antonine"],
        "Kaslik": [
            "Holy Spirit University of Kaslik (USEK)",
            "Université Saint-Esprit de Kaslik (USEK)"
        ],
        "Byblos": [
            "Lebanese American University (LAU)",
            "American University of Technology (AUT)"
        ],
        "Louaize": ["Notre Dame University - Louaize (NDU)"],
        "Tripoli": ["Al-Manar University of Technology"],
        "Balamand": ["University of Balamand"]
    },
    "Malaysia": {
        "Kuala Lumpur": [
            "University of Malaya (UM)",
            "Asia Pacific University (APU)",
            "Malaysia University of Science and Technology (MUST)",
            "Kuala Lumpur Metropolitan University (KLMU)",
            "UCSI University",
            "HELP University",
            "OUM (Open University Malaysia)"
        ],
        "Bangi": ["Universiti Kebangsaan Malaysia (UKM)"],
        "Serdang": ["Universiti Putra Malaysia (UPM)"],
        "Penang": ["Universiti Sains Malaysia (USM)"],
        "Skudai": ["Universiti Teknologi Malaysia (UTM)"],
        "Kuching": ["Universiti Malaysia Sarawak (UNIMAS)"],
        "Kota Kinabalu": ["Universiti Malaysia Sabah (UMS)"],
        "Kuala Terengganu": ["Universiti Sultan Zainal Abidin (UniSZA)"],
        "Perlis": ["Universiti Malaysia Perlis (UniMAP)"],
        "Putrajaya": ["Universiti Tenaga Nasional (UNITEN)"],
        "Sintok": ["Universiti Utara Malaysia (UUM)"],
        "Pekan": ["Universiti Malaysia Pahang (UMP)"],
        "Bandar Sunway": [
            "Monash University Malaysia",
            "Sunway University"
        ],
        "Semenyih": ["University of Nottingham Malaysia"],
        "Subang Jaya": ["Taylor's University"],
        "Nilai": ["INTI International University"],
        "Petaling Jaya": ["Heritage University"],
        "Kota Damansara": ["SEGi University"],
        "Cyberjaya": ["Limkokwing University of Creative Technology"]
    },
    "Philippines": {
        "Multiple campuses": [
            "University of the Philippines (UP) (including Diliman, Manila, Los Baños, Baguio, Cebu, Mindanao)"
        ],
        "Manila": [
            "Polytechnic University of the Philippines (PUP)",
            "Philippine Normal University (PNU)",
            "Technological University of the Philippines (TUP)",
            "Ateneo de Manila University (ADMU)",
            "De La Salle University (DLSU)",
            "University of Santo Tomas (UST)",
            "San Beda University",
            "University of the East (UE)",
            "Mapúa University",
            "Philippine Christian University (PCU)",
            "Centro Escolar University (CEU)",
            "La Consolacion College (LCC)",
            "Far Eastern University (FEU)"
        ],
        "Marawi City": ["Mindanao State University (MSU)"],
        "Legazpi City": ["Bicol University (BU)"],
        "Science City of Muñoz": ["Central Luzon State University (CLSU)"],
        "Tuguegarao City": ["Cagayan State University (CSU)"],
        "Cagayan de Oro": ["University of Science and Technology of Southern Philippines (USTSP)"],
        "Catarman": ["University of Eastern Philippines (UEP)"],
        "Sogod": ["Southern Leyte State University (SLSU)"],
        "Bontoc": ["Mountain Province State Polytechnic College (MPSPC)"],
        "Dumaguete City": [
            "Negros Oriental State University (NORSU)",
            "St. Paul University"
        ],
        "Puerto Princesa City": ["Palawan State University (PSU)"],
        "Quezon City": [
            "St. Paul University",
            "University of Perpetual Help System DALTA"
        ],
        "Bacolod City": ["University of Negros Occidental - Recoletos (UNO-R)"],
        "San Fernando City": ["University of the Assumption (UA)"],
        "Las Piñas City": ["University of Perpetual Help System DALTA"],
        "Caloocan City": ["La Consolacion College (LCC)"]
    },
    "Palestine": {
        "Birzeit": ["Birzeit University"],
        "East Jerusalem": ["Al-Quds University"],
        "Hebron": [
            "Hebron University",
            "Palestine Polytechnic University"
        ],
        "Nablus": ["An-Najah National University"],
        "Gaza City": [
            "The Islamic University of Gaza",
            "University of Palestine"
        ],
        "Jenin": ["Arab American University"],
        "Abu Dis": ["Al-Quds Bard College for Arts and Sciences"],
        "Multiple campuses": ["Al-Quds Open University (West Bank and Gaza Strip)"]
    },
    "Pakistan": {
        "Lahore": [
            "University of the Punjab",
            "Lahore University of Management Sciences (LUMS)",
            "University of Engineering and Technology (UET) Lahore",
            "American University of Pakistan",
            "Lahore College for Women University",
            "National College of Arts (NCA)",
            "University of Central Punjab",
            "Virtual University of Pakistan"
        ],
        "Karachi": [
            "University of Karachi",
            "Karachi Institute of Technology and Entrepreneurship",
            "Institute of Business Administration (IBA)",
            "Karachi University of Management Sciences",
            "Umar Bin Khattab University",
            "Ziauddin University"
        ],
        "Islamabad": [
            "National University of Sciences and Technology (NUST)",
            "Pakistan Institute of Engineering and Applied Sciences (PIEAS)",
            "University of Islamabad",
            "Quaid-i-Azam University",
            "Bahria University",
            "Comsats Institute of Information Technology"
        ],
        "Peshawar": [
            "University of Peshawar",
            "Abasyn University",
            "Peshawar University"
        ],
        "Gujranwala": ["University of the Punjab, Gujranwala Campus"],
        "Muzaffarabad": ["University of Azad Jammu and Kashmir"],
        "Quetta": ["University of Balochistan"],
        "Dera Ismail Khan": ["Gomal University"]
    },


    "Maldives": {
        "Malé": [
            "Maldives National University (MNU)",
            "University of the Maldives",
            "Maldives Islamic University",
            "The Maldives Institute of Technology (MIT)",
            "The Maldives National College of Higher Education (MNCH)",
            "International University of Maldives",
            "Amna International University"
        ]
    },
    "Mongolia": {
        "Ulaanbaatar": [
            "National University of Mongolia (NUM)",
            "Mongolian University of Science and Technology (MUST)",
            "Mongolian State University of Education",
            "Mongolian University of Life Sciences",
            "Mongolian University of Arts and Culture",
            "University of the Humanities",
            "National Medical University of Mongolia",
            "Mongolian National University of Education",
            "University of Ulaanbaatar",
            "Royal International University",
            "Huree University",
            "Institute of Finance and Economics",
            "Mongolia International University",
            "The Asia University",
            "International University of Mongolia",
            "Mongolian University of Science and Technology",
            "Sukhbaatar University"
        ]
    },


    "Oman": {
        "Muscat": [
            "Sultan Qaboos University",
            "Sultan Qaboos University College of Medicine and Health Sciences",
            "Muscat University",
            "The American University of Oman",
            "Oman College of Management and Technology"
        ],
        "Salalah": [
            "Dhofar University"
        ],
        "Nizwa": [
            "University of Nizwa"
        ],
        "Sohar": [
            "Oman Medical College",
            "Sohar University",
            "International Maritime College Oman"
        ],
        "Al Buraimi": [
            "Al Buraimi University College"
        ]
    },
    "Myanmar": {
        "Yangon": [
            "University of Yangon",
            "University of Medicine 1, Yangon",
            "University of Medicine 2, Yangon",
            "Dagon University",
            "Rangoon Institute of Technology",
            "University of Social Sciences",
            "University of Education",
            "University of Distance Education (Yangon)",
            "Myanmar Institute of Information Technology",
            "American International School of Myanmar",
            "International University of Myanmar",
            "University of Computer Studies, Yangon",
            "Asia Pacific International University",
            "Myanmar Aerospace Engineering University",
            "Myanmar International University"
        ],
        "Mandalay": [
            "Mandalay University",
            "University of Technology (Yatanarpon)",
            "University of Medicine 2, Mandalay",
            "Myanmar Institute of Information Technology",
            "University of Computer Studies, Mandalay",
            "University of Foreign Languages, Mandalay",
            "Mandalay University of Economics"
        ],
        "Yezin": [
            "University of Forestry",
            "University of Agriculture"
        ],
        "Monywa": [
            "Monywa University"
        ]
    },
    "North Korea": {
        "Pyongyang": [
            "Kim Il-sung University",
            "Kim Chaek University of Technology",
            "Pyongyang University of Science and Technology",
            "Pyongyang University of Foreign Studies",
            "University of Agriculture",
            "Kim Hyong-jik University of Education",
            "Koryo Medical University"
        ],
        "Wonsan": [
            "Kangwon National University"
        ],
        "Hamhung": [
            "Northeast Asia University",
            "Hamhung University of Chemical Industry"
        ]
    },
    "Nepal": {
        "Kathmandu": [
            "Tribhuvan University",
            "Nepal University of Science and Technology",
            "Central Department of Education",
            "Ace Institute of Management",
            "Birla Institute of Technology and Science (BITS)",
            "Global College International",
            "Universal College of Nepal",
            "The British College",
            "South Asian University (branch)",
            "Asian University for Women (branch)"
        ],
        "Pokhara": [
            "Pokhara University"
        ],
        "Surkhet": [
            "Mid-Western University"
        ],
        "Mahendranagar": [
            "Far Western University"
        ],
        "Chitwan": [
            "Agricultural and Forestry University"
        ],
        "Lalitpur": [
            "Nepal Engineering College"
        ]
    },


    "Nepal": {
        "Kathmandu": [
            "Tribhuvan University",
            "Bagmati University",
            "University of the Himalayas",
            "South Asian University",
            "Royal University of Bhutan",
            "Kathmandu Medical College",
            "Nepal Medical College",
            "Shree Harsha University",
            "Himalayan WhiteHouse International College",
            "The British College",
            "Islington College",
            "Ace Institute of Management",
            "Samriddhi College"
        ],
        "Pokhara": [
            "Pokhara University"
        ],
        "Lalitpur": [
            "Nepal Engineering College"
        ],
        "Dhulikhel": [
            "Kathmandu University"
        ],
        "Birendranagar": [
            "Mid-Western University "
        ],
        "Mahendranagar": [
            "Far Western University "
        ]
    }

}


import csv


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
                random.choice(["Social Media Advertising","Email Marketing","Search Engine Marketing (SEM)",
                               "Influencer Marketing","Community Engagement","Print Media","Radio and tv advertising",
                               "Direct Engagement","SEO"]),
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

with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(data)

print(f"Data written to {filename} successfully.")

