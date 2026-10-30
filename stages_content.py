"""
Stages: a step-by-step path from words to essays. Stages 1 to 3 are built; the rest are shown as coming soon.
This is fixed, reviewed content (nothing here is generated live).
"""

STAGE_XP = 40
PASS_MARK = 3  # correct answers needed (out of 4) to finish a stage

COMING_SOON = [
    (4, "Joining ideas (and, but, because, if)"),
    (5, "Storytelling"),
    (6, "Emails"),
    (7, "Essays"),
]

STAGES = {
    1: {
        "title": "Words",
        "mode": "word",
        "goal": "Pehle chhote, roz ke words seekho: suno, bolo, aur matlab yaad rakho.",
        "rule": "Har word ko pehle suno, phir khud bolo. Ek chhota sentence bhi dekho, taaki word ka use samajh aaye.",
        "points": [
            "Ek baar mein 12 words. Dhire dhire bolo, saaf awaaz mein.",
            "Har word ke saath ek chhota example sentence hai.",
        ],
        "items": [
            {"en": "water", "hi": "paani", "ex": "I drink water.", "ex_hi": "Main paani peeta hoon."},
            {"en": "book", "hi": "kitaab", "ex": "This is my book.", "ex_hi": "Ye meri kitaab hai."},
            {"en": "friend", "hi": "dost", "ex": "He is my friend.", "ex_hi": "Wo mera dost hai."},
            {"en": "house", "hi": "ghar", "ex": "My house is big.", "ex_hi": "Mera ghar bada hai."},
            {"en": "school", "hi": "school", "ex": "I go to school.", "ex_hi": "Main school jaata hoon."},
            {"en": "teacher", "hi": "shikshak", "ex": "She is a teacher.", "ex_hi": "Wo ek teacher hai."},
            {"en": "food", "hi": "khaana", "ex": "The food is hot.", "ex_hi": "Khaana garam hai."},
            {"en": "milk", "hi": "doodh", "ex": "I like milk.", "ex_hi": "Mujhe doodh pasand hai."},
            {"en": "phone", "hi": "phone", "ex": "My phone is new.", "ex_hi": "Mera phone naya hai."},
            {"en": "market", "hi": "bazaar", "ex": "I go to the market.", "ex_hi": "Main bazaar jaata hoon."},
            {"en": "happy", "hi": "khush", "ex": "I am happy.", "ex_hi": "Main khush hoon."},
            {"en": "tired", "hi": "thaka hua", "ex": "I am tired.", "ex_hi": "Main thaka hua hoon."},
        ],
        "say_it": ["water", "friend", "teacher", "market", "happy"],
        "quiz": [
            {"q": "'doodh' in English is:", "options": ["water", "milk", "food"], "answer": 1,
             "why": "'milk' ka matlab doodh hota hai."},
            {"q": "'ghar' in English is:", "options": ["house", "market", "school"], "answer": 0,
             "why": "'house' ka matlab ghar hota hai."},
            {"q": "Which word means 'khush'?", "options": ["tired", "happy", "teacher"], "answer": 1,
             "why": "'happy' ka matlab khush hota hai; 'tired' ka matlab thaka hua."},
            {"q": "'dost' in English is:", "options": ["friend", "book", "phone"], "answer": 0,
             "why": "'friend' ka matlab dost hota hai."},
        ],
    },
    2: {
        "title": "Phrases",
        "mode": "phrase",
        "goal": "Ab 2 ya 3 words ke chhote groups seekho, jo hum roz bolte hain.",
        "rule": "Phrase ek chhota group hota hai jo saath mein bola jaata hai. Poora sentence nahi hota, lekin bahut kaam aata hai.",
        "points": [
            "Phrase ko ek unit ki tarah yaad rakho: 'a cup of tea', 'right now'.",
            "Word order mat badlo: 'a cup of tea' sahi hai, 'a tea of cup' galat.",
        ],
        "items": [
            {"en": "good morning", "hi": "suprabhat", "ex": "Good morning, teacher.", "ex_hi": "Suprabhat, teacher."},
            {"en": "thank you", "hi": "shukriya", "ex": "Thank you for your help.", "ex_hi": "Aapki madad ke liye shukriya."},
            {"en": "excuse me", "hi": "maaf kijiye (dhyan kheenchne ke liye)", "ex": "Excuse me, where is the station?", "ex_hi": "Maaf kijiye, station kahan hai?"},
            {"en": "a cup of tea", "hi": "ek cup chai", "ex": "I want a cup of tea.", "ex_hi": "Mujhe ek cup chai chahiye."},
            {"en": "a glass of water", "hi": "ek glass paani", "ex": "Please give me a glass of water.", "ex_hi": "Please mujhe ek glass paani dijiye."},
            {"en": "right now", "hi": "abhi", "ex": "I am busy right now.", "ex_hi": "Main abhi busy hoon."},
            {"en": "every day", "hi": "har din", "ex": "I study every day.", "ex_hi": "Main har din padhta hoon."},
            {"en": "at home", "hi": "ghar par", "ex": "She is at home.", "ex_hi": "Wo ghar par hai."},
            {"en": "on time", "hi": "sahi samay par", "ex": "Please come on time.", "ex_hi": "Please sahi samay par aana."},
            {"en": "next to", "hi": "ke bagal mein", "ex": "The bank is next to the school.", "ex_hi": "Bank school ke bagal mein hai."},
        ],
        "say_it": ["good morning", "thank you", "a cup of tea", "right now", "on time"],
        "quiz": [
            {"q": "Which phrase means 'ek cup chai'?", "options": ["a cup of tea", "a tea of cup", "cup tea a"], "answer": 0,
             "why": "Sahi order hai 'a cup of tea'."},
            {"q": "'Abhi' in English is:", "options": ["every day", "right now", "on time"], "answer": 1,
             "why": "'right now' ka matlab abhi hota hai; 'every day' ka matlab har din."},
            {"q": "Which phrase means 'sahi samay par'?", "options": ["on time", "at time", "in the time"], "answer": 0,
             "why": "'on time' ka matlab sahi samay par hota hai."},
            {"q": "Which phrase do we use to get someone's attention politely?",
             "options": ["excuse me", "thank you", "good morning"], "answer": 0,
             "why": "'Excuse me' se hum kisi ka dhyan politely apni taraf kheenchte hain."},
        ],
    },
    3: {
        "title": "Simple sentences",
        "mode": "sentence",
        "goal": "Ab words aur phrases jodkar poore chhote sentences banao.",
        "rule": (
            "Hindi mein kriya (verb) aakhir mein aata hai: 'Main chai peeta hoon'. "
            "English mein order alag hai: Subject + Verb + Object. Jaise: 'I drink tea.'"
        ),
        "points": [
            "Subject = kaun (I, you, he, she, we, they). Verb = kya kar raha hai (drink, read, play). Object = kisko ya kya (tea, a book, cricket).",
            "Order yaad rakho: pehle Subject, phir Verb, phir Object.",
            "He / she / it ke saath present tense mein verb mein -s lagta hai: She reads a book. (Exceptions section mein aur dekho.)",
        ],
        "items": [
            {"en": "I drink tea.", "hi": "Main chai peeta hoon.", "ex": "", "ex_hi": ""},
            {"en": "She reads a book.", "hi": "Wo kitaab padhti hai.", "ex": "", "ex_hi": ""},
            {"en": "They play cricket.", "hi": "Wo log cricket khelte hain.", "ex": "", "ex_hi": ""},
            {"en": "We eat lunch at one.", "hi": "Hum ek baje lunch karte hain.", "ex": "", "ex_hi": ""},
            {"en": "He likes music.", "hi": "Use music pasand hai.", "ex": "", "ex_hi": ""},
            {"en": "You know the answer.", "hi": "Tum jawab jaante ho.", "ex": "", "ex_hi": ""},
        ],
        "mistakes": [
            ("I tea drink.", "I drink tea."),
            ("We lunch eat.", "We eat lunch."),
            ("He play cricket.", "He plays cricket."),
        ],
        "say_it": ["I drink tea.", "She reads a book.", "They play cricket.", "He likes music."],
        "quiz": [
            {"q": "Which sentence has the correct word order?",
             "options": ["I tea drink.", "I drink tea.", "Drink I tea."], "answer": 1,
             "why": "English mein order hai Subject + Verb + Object: I (subject) drink (verb) tea (object)."},
            {"q": "She ___ a book.", "options": ["reads", "reading", "readed"], "answer": 0,
             "why": "She ke saath present tense mein verb mein -s lagta hai: reads."},
            {"q": "He ___ cricket.", "options": ["plays", "play", "playing"], "answer": 0,
             "why": "He ke saath verb mein -s lagta hai: plays."},
            {"q": "They ___ lunch at one.", "options": ["eat", "eats", "eating"], "answer": 0,
             "why": "They ke saath -s nahi lagta: They eat."},
        ],
    },
}


def heard_has_word(heard, target):
    """Lenient check for single words: true if the target word appears anywhere in what was heard."""
    import re

    clean = lambda t: re.sub(r"[^a-z' ]", "", t.lower()).split()
    return target.lower() in clean(heard)
