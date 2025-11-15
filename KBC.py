import random
print("\n\t WELCOME TO \"KAUN BANEGA CROREPATI\"")
print("\nRules Of The Game:")
print("1. Multiple-Choice Questions (MCQs):\n   Each question has 4 options — A, B, C, and D.\n   The player must choose the correct one.\n")
print("2. Money Ladder:\n   With each correct answer, the player moves up the prize ladder.\n   [5,000 -> 10,000 -> 15,000 -> 20,000 -> 25,000 -> 50,000 -> 1,00,000 -> 2,00,000 -> 3,00,000 -> 5,00,000 -> 7,50,000 -> 12,50,000 -> 25,00,000 -> 50,00,000 -> 1 Crore -> 7 Crore.]\n")
print("3. Safe Levels:\n   If players cross certain levels, they guarantee that amount even if they get a later answer wrong_iter.\n   Common safe levels: ₹25,000; ₹500,000; ₹7 Crore.\n")
print("4. Lifelines:\n   4 lifelines are available:\n   50:50 → Removes two wrong_iter options.\n   Audience Poll → Shows percentage for each option.\n   Phone-a-Friend → Gives a hint.\n   Flip the Question → Replace the current question.\n")
print("5. Wrong Answer Ends the Game:\n   If a player answers incorrectly, the game ends and they win the last “safe amount”.\n")
print("6. Quit Option:\n   A player can quit anytime and take the current amount.\n")

# ------------------------------ Life-Lines -----------------------------

def fifty_fifty(question):
    correct_option = question[-1]
    option = [1,2,3,4]
    wrong_option = [opt for opt in option if opt != correct_option]
    remove_two = random.sample(wrong_option, 2)
    remaining_options = [opt for opt in option if opt not in remove_two]
    print("50-50 Lifeline Activated:")
    for opt in remaining_options:
        label = ['a','b','c','d'][opt-1]
        print(f"{label}. {question[opt]}")
    return remaining_options

def flip_the_question(current_question, flipped_question):
    if not flipped_question:
        print("\nNo more questions available to flip. Flip not possible.\n")
        return current_question, flipped_question
    new_question = random.choice(flipped_question)
    flipped_question.remove(new_question)
    print("\nFlip The Question Activated..!")
    return new_question, flipped_question

def phone_a_friend(question):
    correct_option = question[-1]
    option = [1,2,3,4]
    chance = random.randint(1,100)
    if(chance >= 70):
        friend_choice = correct_option
    else:
        wrong_choice = [opt for opt in option if opt != correct_option]
        friend_choice = random.choice(wrong_choice)
        label = ['a','b','c','d']
        print(f"Phone A Friend Activated..!\nYour Friend Thinks {label[friend_choice-1]} option is correct.\n")
    return friend_choice

def audience_poll(question):
    correct_option = question[-1]
    correct_percentage = random.randint(50,75)
    remaining = 100 - correct_percentage
    a = random.randint(0,remaining)
    b = random.randint(0, remaining - a)
    c = remaining - a - b
    wrong_percentage = [a,b,c]
    percentage = {}
    index = 0
    for opt in [1,2,3,4]:
        if(opt == correct_option):
            percentage[opt] = correct_percentage
        else:
            percentage[opt] = wrong_percentage[index]
            index += 1
    print("\nAudience Poll Activated..!")
    label = ['a','b','c','d']
    for opt in [1,2,3,4]:
        print(f"{label[opt-1]} -> {percentage[opt]}%")

# ------------------------------ Asking To Play -----------------------------

def play():
    while True:
        reply = input("Are You Ready To Play \"KAUN BANEGA CROREPATI\" ['yes' or 'no']: ").lower().strip()
        if (reply == 'yes'):
            return False
        elif (reply == 'no'):
            print("Exiting From The Game..!\n")
            exit()
        else:
            print("INVALID INPUT..!\n")

# ------------------------------ Questions -----------------------------

questions_list = [
["Which planet has the largest number of moons?", "Earth", "Jupiter", "Saturn", "Neptune", 3],
["Who wrote the epic 'Paradise Lost'?", "John Milton", "William Wordsworth", "Leo Tolstoy", "Mark Twain", 1],
["Which element has the highest melting point?", "Carbon", "Tungsten", "Osmium", "Platinum", 2],
["The Battle of Plassey was fought in which year?", "1757", "1857", "1657", "1707", 1],
["Which is the longest bone in the human body?", "Fibula", "Femur", "Tibia", "Humerus", 2],
["Which organelle is known as the powerhouse of the cell?", "Golgi Body", "Ribosome", "Mitochondria", "Lysosome", 3],
["Who painted the Mona Lisa?", "Pablo Picasso", "Leonardo da Vinci", "Rembrandt", "Van Gogh", 2],
["Which gas is used in the preparation of soda water?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Helium", 3],
["Which country is known as the Land of the Rising Sun?", "China", "South Korea", "Japan", "Thailand", 3],
["What is the SI unit of pressure?", "Kelvin", "Pascal", "Newton", "Joule", 2],
["Which metal is liquid at room temperature?", "Iron", "Mercury", "Sodium", "Potassium", 2],
["Who discovered Penicillin?", "Marie Curie", "Alexander Fleming", "Isaac Newton", "Einstein", 2],
["The Suez Canal connects the Mediterranean Sea to which sea?", "Red Sea", "Black Sea", "Arabian Sea", "Caspian Sea", 1],
["Where is the headquarters of UNESCO located?", "Rome", "Paris", "London", "Berlin", 2],
["Which desert is the largest in the world?", "Sahara", "Gobi", "Kalahari", "Arabian", 1],
["What is the currency of Switzerland?", "Euro", "Yen", "Pound", "Swiss Franc", 4],
["Which is the hardest natural substance?", "Diamond", "Quartz", "Topaz", "Corundum", 1],
["Who proposed the three laws of motion?", "Einstein", "Newton", "Galileo", "Planck", 2],
["Which is the smallest continent?", "Africa", "Europe", "Australia", "South America", 3],
["Which is the largest coral reef system?", "Belize Reef", "Red Sea Reef", "Great Barrier Reef", "Florida Reef", 3],
["What is the chemical name of table salt?", "Potassium Chloride", "Sodium Chloride", "Magnesium Sulphate", "Calcium Oxide", 2],
["Which instrument is used to measure earthquakes?", "Barometer", "Seismograph", "Altimeter", "Hydrometer", 2],
["Which Mughal ruler built the Red Fort?", "Akbar", "Jahangir", "Shah Jahan", "Aurangzeb", 3],
["Which river is the longest in the world?", "Amazon", "Nile", "Yangtze", "Mississippi", 2],
["Who discovered gravity?", "Galileo", "Newton", "Kepler", "Faraday", 2],
["Which vitamin is known as ascorbic acid?", "Vitamin B", "Vitamin C", "Vitamin D", "Vitamin K", 2],
["Which country invented paper?", "India", "China", "Egypt", "Greece", 2],
["What is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Perth", 3],
["Which blood group is known as the universal donor?", "AB+", "O+", "O-", "A-", 3],
["Which scientist proposed the theory of relativity?", "Tesla", "Einstein", "Planck", "Edison", 2],
["The Great Wall of China was built to protect against which group?", "Romans", "Mongols", "Persians", "Japanese", 2],
["Where is Mount Kilimanjaro located?", "Kenya", "Tanzania", "Uganda", "Ethiopia", 2],
["Which chemical element has symbol 'Au'?", "Silver", "Gold", "Copper", "Argon", 2],
["Which is the largest mammal?", "Blue Whale", "Elephant", "Hippopotamus", "Giraffe", 1],
["What is H2SO4 called?", "Nitric Acid", "Sulfuric Acid", "Hydrochloric Acid", "Phosphoric Acid", 2],
["Who was the first man to step on the Moon?", "Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Alan Shepard", 1],
["The process of converting milk into curd is called?", "Oxidation", "Fermentation", "Sublimation", "Evaporation", 2],
["Who wrote 'The Odyssey'?", "Homer", "Sophocles", "Virgil", "Plato", 1],
["Where is the Dead Sea located?", "China & Mongolia", "Israel & Jordan", "India & Pakistan", "Iran & Iraq", 2],
["What is the largest internal organ in the human body?", "Liver", "Kidney", "Heart", "Lungs", 1],
["Which disease is caused by a deficiency of iodine?", "Night blindness", "Goitre", "Rickets", "Scurvy", 2],
["Who invented the telephone?", "Graham Bell", "Edison", "Tesla", "Faraday", 1],
["What is the study of fossils called?", "Ecology", "Paleontology", "Geology", "Anthropology", 2],
["Which is the deepest point in the oceans?", "Tonga Trench", "Mariana Trench", "Java Trench", "Puerto Rico Trench", 2],
["Which language has the most native speakers?", "French", "Mandarin Chinese", "Spanish", "Hindi", 2],
["What is the capital of Egypt?", "Alexandria", "Cairo", "Giza", "Aswan", 2],
["What is the boiling point of water at sea level?", "50°C", "100°C", "150°C", "200°C", 2],
["Which continent has the most countries?", "Europe", "South America", "Africa", "Asia", 3],
["Which gas is essential for photosynthesis?", "Nitrogen", "Oxygen", "Hydrogen", "Carbon Dioxide", 4],
["Which is the world's fastest land animal?", "Lion", "Cheetah", "Tiger", "Greyhound", 2],
["Who was the first President of the United States?", "Lincoln", "Washington", "Jefferson", "Adams", 2],
["Which metal is most abundant in Earth's crust?", "Iron", "Aluminum", "Copper", "Zinc", 2],
["What is the largest ocean?", "Atlantic", "Indian", "Pacific", "Arctic", 3],
["Which organ purifies blood?", "Heart", "Liver", "Kidney", "Lungs", 3],
["Which country gifted the Statue of Liberty to the USA?", "Spain", "France", "Germany", "Italy", 2],
["Who discovered the electron?", "Rutherford", "Thomson", "Bohr", "Fermi", 2],
["Which animal is known as the Ship of the Desert?", "Horse", "Camel", "Elephant", "Yak", 2],
["What is the largest island in the world?", "Greenland", "Madagascar", "Borneo", "New Guinea", 1],
["How many chromosomes are in a human cell?", "23", "32", "46", "56", 3],
["What is the capital of Canada?", "Toronto", "Ottawa", "Vancouver", "Montreal", 2],
["Which blood vessels carry blood to the heart?", "Arteries", "Veins", "Capillaries", "Nerves", 2],
["Which is the smallest prime number?", "0", "1", "2", "3", 3],
["What is the chemical formula of methane?", "CH4", "CO2", "C2H6", "NH3", 1],
["Which revolution is associated with the production of milk?", "White Revolution", "Green Revolution", "Blue Revolution", "Golden Revolution", 1],
["Which country has the most volcanoes?", "Japan", "Indonesia", "USA", "Italy", 2],
["Which mountain range separates Europe and Asia?", "Alps", "Ural", "Andes", "Rockies", 2],
["Which is the lightest metal?", "Lithium", "Sodium", "Magnesium", "Aluminum", 1],
["Where is the Taj Mahal located?", "Delhi", "Agra", "Jaipur", "Varanasi", 2],
["What is the longest-running animated TV series?", "Pokemon", "Tom and Jerry", "The Simpsons", "Family Guy", 3],
["What is the powerhouse of the cell?", "Ribosome", "Nucleus", "Mitochondria", "Chloroplast", 3],
["Which gas forms about 78% of Earth's atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 2],
["How many players are there in a cricket team?", "9", "10", "11", "12", 3],
["Which is the nearest star to Earth?", "Polaris", "Alpha Centauri", "Sirius", "Sun", 4],
["What did Alfred Nobel invent?", "Telephone", "Dynamite", "Airplane", "Steam Engine", 2],
["Which continent is the driest?", "Asia", "Antarctica", "Africa", "Australia", 2],
["Which country is the largest producer of coffee?", "Colombia", "Vietnam", "Brazil", "Ethiopia", 3],
["Who was the first woman to win Nobel Prize?", "Marie Curie", "Mother Teresa", "Rosalind Franklin", "Ada Lovelace", 1],
["What is the study of earthquakes called?", "Seismology", "Geology", "Hydrology", "Meteorology", 1],
["Which fruit has its seeds on the outside?", "Mango", "Banana", "Strawberry", "Apple", 3],
["Which is the longest river in India?", "Yamuna", "Ganga", "Godavari", "Brahmaputra", 2],
["What is the capital of Italy?", "Venice", "Rome", "Milan", "Naples", 2],
["Which instrument measures atmospheric pressure?", "Thermometer", "Barometer", "Anemometer", "Hydrometer", 2],
["What is the study of birds called?", "Ecology", "Ornithology", "Zoology", "Botany", 2],
["What is the largest plateau in the world?", "Tibetan Plateau", "Deccan Plateau", "Colorado Plateau", "Andean Plateau", 1],
["Which gas is known as laughing gas?", "Nitrogen", "Nitrous Oxide", "Carbon Monoxide", "Hydrogen Sulfide", 2],
["Which is the hottest planet?", "Mercury", "Venus", "Mars", "Jupiter", 2],
["Which city is called the City of Canals?", "Venice", "Amsterdam", "Bangkok", "Bruges", 1],
["What is the unit of electric current?", "Volt", "Ampere", "Ohm", "Watt", 2],
["Which is the most spoken language in the world?", "English", "Spanish", "Mandarin Chinese", "Hindi", 3],
["Where is the Leaning Tower located?", "Paris", "Rome", "Berlin", "Pisa", 4],
["Which ancient university was located in Bihar, India?", "Taxila", "Nalanda", "Ujjain", "Vikramshila", 2],
["Which scientist is known for the uncertainty principle?", "Bohr", "Heisenberg", "Feynman", "Dirac", 2],
["What is the largest gland in the human body?", "Pancreas", "Liver", "Thyroid", "Adrenal", 2],
["Which Indian classical dance originates from Odisha?", "Kathak", "Bharatnatyam", "Odissi", "Kuchipudi", 3],
["Which country first used paper currency?", "India", "Egypt", "China", "Greece", 3],
["Who discovered the law of planetary motion?", "Copernicus", "Kepler", "Galileo", "Tycho Brahe", 2],
["Which animal has the highest blood pressure?", "Elephant", "Blue Whale", "Giraffe", "Hippo", 3],
["What is the main ore of aluminum?", "Magnetite", "Bauxite", "Galena", "Hematite", 2],
["Which part of the brain controls balance?", "Cerebrum", "Medulla", "Cerebellum", "Thalamus", 3],
["Who wrote the book 'The Prince'?", "Voltaire", "Machiavelli", "Kant", "Rousseau", 2]
]

# ------------------------------ Money Level, Options & Life-lines Used -----------------------------

levels = [5000, 10000, 15000, 20000, 25000, 50000, 100000, 200000, 300000, 500000, 750000, 1250000, 2500000, 5000000, 10000000, 70000000]
options = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
amount = 0
fifty_fifty_used = False
audience_poll_used = False
flip_the_question_used = False
phone_a_friend_used = False

# ------------------------------ GAME LOGIC -----------------------------

play()
random.shuffle(questions_list)
selected_questions = questions_list[:16]
flipped_questions = questions_list[16:]
for i, question in enumerate(selected_questions):
    question = selected_questions[i]
    current_remaining = [1,2,3,4]
    while True:
        print(f"\n{i+1} Question for Rs.{levels[i]}:\n{question[0]}")
        labels = ['a','b','c','d']
        for opt in current_remaining:
            print(f"{labels[opt-1]}. {question[opt]}")
        print("\n")
        answer = input("Enter The Correct Option [a/b/c/d], 'l' for liflines or 'quit': ").lower().strip()
        if(answer == "quit"):
            if(i == 0):
                print("You Have Won Rs.0")
            else:
                print(f"Congratulations You Have Won Rs.{levels[i-1]}")
            print("Thanks For Playing The Game..!\n")
            exit()
        if(answer == 'l'):
            print("\nLife-Lines:\n1. 50-50.\n2. Flip The Question.\n3. Audience Poll.\n4. Phone A Friend.\n5. Cancel.\n")
            choose = int(input("Choose Life-Line Number: "))
            match choose:
                case 1:
                    if(fifty_fifty_used == True):
                        print("You have already used '50-50' life-line\n")
                        continue
                    else:
                        current_remaining = fifty_fifty(question)
                        fifty_fifty_used = True
                    continue
                case 2:
                    if(flip_the_question_used == True):
                        print("You have already used 'Flip The Question' life-line\n")
                        continue
                    else:
                        question, flipped_questions = flip_the_question(question,flipped_questions)
                        flip_the_question_used = True
                        current_remaining = [1,2,3,4]
                        continue
                case 3:
                    if(audience_poll_used == True):
                        print("You Have Already Used 'Audience Poll' life-line\n")
                        continue
                    else:
                        audience_poll(question)
                        audience_poll_used = True
                        continue
                case 4:
                    if(phone_a_friend_used == True):
                        print("You Have already used 'Phone A Friend' life-line")
                    else:
                        phone_a_friend(question)
                        phone_a_friend_used = True
                        continue
                case 5:
                    print("Life-Line Menu Closed:\n")
                    continue
                case _:
                    print("INVALID INPUT..!")
        if answer not in options:
            print("INAVLID INPUT..! Please choose a, b, c, d or 'l' or 'quit'.\n")
            continue
        if answer in options:
            if(options[answer] == question[-1]):
                print(f"Your Answer is Right..., You Won Rs.{levels[i]}.\n")
                if(levels[i] == 25000):
                    amount = 25000
                elif(levels[i] == 500000):
                    amount = 500000
                elif(levels[i] == 70000000):
                    amount = 70000000
                break
            else:
                print(f"Oops, Your Answer is Wrong...!, Correct answer is {question[-1]}")
                print(f"You have Won Rs.{amount}\n")
                print("Thanks For Playing The Game..!\n")
                exit()
print(f"\nCongratulations..! You answered all quesTions.\nYou Have Won Rs.{levels[-1]}.\nThanks For Playing The Game.\n")
