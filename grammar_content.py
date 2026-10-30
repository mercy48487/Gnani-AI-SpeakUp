"""
Grammar Book lessons. This is fixed, reviewed content (nothing here is generated live).
To add a lesson, copy one block, give it a new key, and fill in the fields.
"""

LESSONS = {
    "a_an": {
        "title": "A or An",
        "rule": (
            "Rule yaad rakho: 'a' ya 'an' letter se nahi, SOUND (awaaz) se decide hota hai. "
            "Agar word vowel jaisi awaaz (a, e, i, o, u) se shuru hota hai, toh 'an' lagao. "
            "Agar word consonant jaisi awaaz se shuru hota hai, toh 'a' lagao."
        ),
        "points": [
            "an apple, an egg, an umbrella: yahan shuruaat vowel awaaz se hoti hai, isliye 'an'.",
            "an hour, an honest man: 'h' bola nahi jaata (silent h), isliye awaaz vowel se shuru hoti hai.",
            "a university, a user, a one-time offer: spelling vowel se shuru hoti hai, lekin awaaz 'yoo' ya 'wun' jaisi consonant awaaz hai, isliye 'a'.",
        ],
        "examples": [
            ("I ate an apple.", "Maine ek seb khaya."),
            ("I waited for an hour.", "Maine ek ghante tak intezaar kiya."),
            ("She studies at a university.", "Wo ek university mein padhti hai."),
            ("This is a one-time offer.", "Ye sirf ek baar ka offer hai."),
            ("He is an honest man.", "Wo ek imaandaar aadmi hai."),
        ],
        "mistakes": [
            ("an university", "a university"),
            ("a hour", "an hour"),
            ("a umbrella", "an umbrella"),
        ],
        "say_it": [
            "I waited for an hour.",
            "She studies at a university.",
            "He is an honest man.",
            "This is a one-time offer.",
        ],
        "quiz": [
            {"q": "I waited for ___ hour.", "options": ["a", "an"], "answer": 1,
             "why": "'hour' mein 'h' silent hai, awaaz vowel se shuru hoti hai, isliye 'an'."},
            {"q": "She studies at ___ university.", "options": ["a", "an"], "answer": 0,
             "why": "'university' ki awaaz 'yoo' se shuru hoti hai (consonant awaaz), isliye 'a'."},
            {"q": "I need ___ umbrella.", "options": ["a", "an"], "answer": 1,
             "why": "'umbrella' vowel awaaz ('uh') se shuru hota hai, isliye 'an'."},
            {"q": "This is ___ one-time offer.", "options": ["a", "an"], "answer": 0,
             "why": "'one' ki awaaz 'wun' jaisi hai (consonant 'w'), isliye 'a'."},
        ],
    },
    "past_tense": {
        "title": "Past tense (what already happened)",
        "rule": (
            "Jo kaam khatam ho chuka hai, usse batane ke liye past tense use karte hain. "
            "Aksar yesterday, last week, ago jaise words saath aate hain. "
            "Regular verbs mein -ed lagta hai (walk, walked). "
            "Kuch verbs irregular hote hain, unka form badal jaata hai (go, went)."
        ),
        "points": [
            "Regular verbs: walk, walked | play, played | want, wanted. Agar verb 'e' par khatam ho toh sirf -d lagao (like, liked).",
            "Irregular verbs yaad karne padte hain: go, went | eat, ate | see, saw | have, had | buy, bought.",
            "'did' ya 'did not' ke baad verb apne simple form mein rehta hai: Did you go? I did not go. ('went' nahi.)",
        ],
        "examples": [
            ("Yesterday I went to school.", "Kal main school gaya."),
            ("She watched a movie last night.", "Usne kal raat ek movie dekhi."),
            ("We ate dinner two hours ago.", "Humne do ghante pehle dinner kiya."),
            ("He bought a new phone last week.", "Usne pichhle hafte naya phone kharida."),
            ("I did not go to the party.", "Main party mein nahi gaya."),
        ],
        "mistakes": [
            ("Yesterday I go to school.", "Yesterday I went to school."),
            ("I didn't went to school.", "I didn't go to school."),
            ("She eated lunch.", "She ate lunch."),
        ],
        "say_it": [
            "Yesterday I went to school.",
            "She watched a movie last night.",
            "We ate dinner two hours ago.",
            "I did not go to the party.",
        ],
        "quiz": [
            {"q": "Yesterday I ___ to school.", "options": ["go", "went", "goes"], "answer": 1,
             "why": "'Yesterday' ka matlab kaam ho chuka hai, isliye past form 'went'."},
            {"q": "She ___ a movie last night.", "options": ["watch", "watched", "watches"], "answer": 1,
             "why": "'watch' regular verb hai, past mein -ed lagta hai: watched."},
            {"q": "I did not ___ to the party.", "options": ["went", "go", "going"], "answer": 1,
             "why": "'did not' ke baad verb simple form mein rehta hai: go."},
            {"q": "We ___ dinner two hours ago.", "options": ["eat", "ate", "eaten"], "answer": 1,
             "why": "'eat' irregular verb hai, uska past form 'ate' hai."},
        ],
    },
}


# ---------------------------------------------------------------------------
# Exceptions section: fixed, reviewed content, one topic per entry.
# Each topic: id, title, rule (Hinglish), optional note, optional table, optional mistakes, examples.
# ---------------------------------------------------------------------------
EXCEPTIONS = [
    {
        "id": "a_an_tricky",
        "title": "A or An: tricky cases",
        "rule": "Yaad rakho: sound decide karta hai, letter nahi. Kuch words aur abbreviations mein ye confusing lagta hai.",
        "table": {
            "headers": ["Word", "Use", "Why"],
            "rows": [
                ["hour, honest, heir, honour", "an", "'h' silent hai, awaaz vowel se shuru hoti hai"],
                ["university, unit, user, European", "a", "shuruaat 'yoo' awaaz se hoti hai"],
                ["one-time, one-way", "a", "'one' ki awaaz 'wun' hai (consonant)"],
                ["MBA, SMS, X-ray, FBI", "an", "letter ka naam vowel awaaz se shuru hota hai (em, ess, ex, ef)"],
                ["HR, LED, NRI", "an", "'aitch', 'el', 'en' vowel awaaz se shuru hote hain"],
                ["UK, USA, UN", "a", "'yoo' awaaz se shuru hote hain"],
            ],
        },
        "mistakes": [
            ("an university", "a university"),
            ("a hour", "an hour"),
            ("a MBA", "an MBA"),
            ("an UK visa", "a UK visa"),
        ],
        "examples": [
            ("I am doing an MBA.", "Main MBA kar raha hoon."),
            ("She has a UK visa.", "Uske paas UK ka visa hai."),
            ("We waited for an hour.", "Humne ek ghante tak intezaar kiya."),
        ],
    },
    {
        "id": "irregular_verbs",
        "title": "Irregular verbs (past and past participle)",
        "rule": (
            "Kuch verbs mein -ed nahi lagta, unka form badal jaata hai. V2 simple past mein aata hai (I went). "
            "V3 'have / has / had' ke saath aata hai (I have gone)."
        ),
        "table": {
            "headers": ["Base (V1)", "Past (V2)", "Past participle (V3)"],
            "rows": [
                ["go", "went", "gone"], ["eat", "ate", "eaten"], ["see", "saw", "seen"],
                ["do", "did", "done"], ["have", "had", "had"], ["be", "was / were", "been"],
                ["buy", "bought", "bought"], ["take", "took", "taken"], ["come", "came", "come"],
                ["write", "wrote", "written"], ["give", "gave", "given"], ["know", "knew", "known"],
                ["run", "ran", "run"], ["begin", "began", "begun"], ["speak", "spoke", "spoken"],
                ["bring", "brought", "brought"], ["think", "thought", "thought"], ["make", "made", "made"],
                ["say", "said", "said"], ["put", "put", "put"], ["cut", "cut", "cut"],
                ["read", "read (bola jaata hai 'red')", "read (bola jaata hai 'red')"],
                ["sit", "sat", "sat"], ["drink", "drank", "drunk"], ["teach", "taught", "taught"],
                ["catch", "caught", "caught"], ["sleep", "slept", "slept"], ["feel", "felt", "felt"],
                ["leave", "left", "left"], ["lose", "lost", "lost"], ["meet", "met", "met"],
                ["pay", "paid", "paid"], ["sell", "sold", "sold"], ["tell", "told", "told"],
                ["understand", "understood", "understood"], ["wear", "wore", "worn"],
                ["win", "won", "won"], ["fly", "flew", "flown"], ["drive", "drove", "driven"],
                ["choose", "chose", "chosen"], ["forget", "forgot", "forgotten"],
                ["find", "found", "found"], ["hear", "heard", "heard"], ["keep", "kept", "kept"],
                ["send", "sent", "sent"], ["spend", "spent", "spent"], ["stand", "stood", "stood"],
                ["build", "built", "built"], ["break", "broke", "broken"],
            ],
        },
        "mistakes": [
            ("She eated lunch.", "She ate lunch."),
            ("I have went there.", "I have gone there."),
            ("He buyed a phone.", "He bought a phone."),
            ("We seen it yesterday.", "We saw it yesterday."),
        ],
        "examples": [
            ("I have gone to the market.", "Main market ja chuka hoon."),
            ("She wrote a letter yesterday.", "Usne kal ek letter likha."),
            ("They have eaten lunch.", "Unhone lunch kar liya hai."),
        ],
    },
    {
        "id": "ed_spelling",
        "title": "Spelling rules for -ed (regular past)",
        "rule": "Regular verbs mein -ed lagate waqt spelling kabhi kabhi badalti hai.",
        "table": {
            "headers": ["Rule", "Examples"],
            "rows": [
                ["Verb 'e' par khatam ho: sirf -d lagao", "like, liked | live, lived"],
                ["Consonant + y: y hatao, -ied lagao", "study, studied | cry, cried"],
                ["Vowel + y: sirf -ed lagao", "play, played | enjoy, enjoyed"],
                ["Chhota word (ek vowel + ek consonant): last consonant double karo", "stop, stopped | plan, planned"],
                ["Do syllable ka word jiska stress pehle syllable par ho: double nahi hota", "visit, visited | open, opened"],
            ],
        },
        "mistakes": [
            ("studyed", "studied"),
            ("stoped", "stopped"),
            ("playied", "played"),
        ],
        "examples": [
            ("She studied all night.", "Usne poori raat padhai ki."),
            ("He stopped the car.", "Usne gaadi roki."),
            ("We enjoyed the trip.", "Humein trip mein maza aaya."),
        ],
    },
    {
        "id": "third_person",
        "title": "He / She / It: verbs with -s",
        "rule": "Present tense mein he, she, it ke saath verb mein -s ya -es lagta hai. Kuch verbs ka form alag hota hai.",
        "table": {
            "headers": ["Verb", "He / She / It form", "Rule"],
            "rows": [
                ["have", "has", "irregular"],
                ["do", "does", "-es lagta hai"],
                ["go", "goes", "-es lagta hai"],
                ["watch", "watches", "-ch ke baad -es"],
                ["wash", "washes", "-sh ke baad -es"],
                ["fix", "fixes", "-x ke baad -es"],
                ["study", "studies", "consonant + y: y hatao, -ies lagao"],
                ["play", "plays", "vowel + y: sirf -s"],
            ],
        },
        "mistakes": [
            ("She have a phone.", "She has a phone."),
            ("He go to school.", "He goes to school."),
            ("She studys hard.", "She studies hard."),
            ("Does she likes tea?", "Does she like tea?"),
        ],
        "examples": [
            ("She has a new bag.", "Uske paas ek naya bag hai."),
            ("He goes to college by bus.", "Wo bus se college jaata hai."),
            ("She studies every night.", "Wo har raat padhti hai."),
        ],
    },
    {
        "id": "plurals",
        "title": "Plural nouns: exceptions",
        "rule": "Zyada tar nouns mein -s lagta hai, lekin kuch nouns ke plural alag hote hain.",
        "table": {
            "headers": ["Singular", "Plural", "Rule"],
            "rows": [
                ["child", "children", "irregular"],
                ["man", "men", "irregular"],
                ["woman", "women", "irregular"],
                ["person", "people", "irregular"],
                ["tooth", "teeth", "irregular"],
                ["foot", "feet", "irregular"],
                ["mouse", "mice", "irregular"],
                ["sheep", "sheep", "singular aur plural same"],
                ["fish", "fish", "singular aur plural same"],
                ["leaf", "leaves", "-f / -fe ki jagah -ves"],
                ["knife", "knives", "-f / -fe ki jagah -ves"],
                ["wife", "wives", "-f / -fe ki jagah -ves"],
                ["roof", "roofs", "-ves nahi, sirf -s (exception)"],
                ["city", "cities", "consonant + y: -ies"],
                ["boy", "boys", "vowel + y: sirf -s"],
                ["bus", "buses", "-s / -x / -ch / -sh ke baad -es"],
                ["box", "boxes", "-s / -x / -ch / -sh ke baad -es"],
                ["watch", "watches", "-s / -x / -ch / -sh ke baad -es"],
            ],
        },
        "mistakes": [
            ("two childs", "two children"),
            ("five mans", "five men"),
            ("many sheeps", "many sheep"),
        ],
        "examples": [
            ("There are three children in the room.", "Kamre mein teen bachche hain."),
            ("She has two knives.", "Uske paas do chaaku hain."),
            ("Many people came to the party.", "Party mein bahut log aaye."),
        ],
    },
    {
        "id": "uncountable",
        "title": "Uncountable nouns (no -s, no a / an)",
        "rule": (
            "Kuch nouns ko gin nahi sakte, isliye unka plural nahi hota aur 'a / an' nahi lagta. "
            "Inke saath singular verb aata hai."
        ),
        "table": {
            "headers": ["Word", "Wrong", "Right"],
            "rows": [
                ["information", "informations", "some information"],
                ["advice", "advices, an advice", "some advice, a piece of advice"],
                ["furniture", "furnitures", "some furniture"],
                ["luggage", "luggages", "my luggage, two pieces of luggage"],
                ["homework", "homeworks", "my homework"],
                ["news", "a news, the news are", "the news is, a piece of news"],
                ["equipment", "equipments", "some equipment"],
            ],
        },
        "mistakes": [
            ("She gave me many informations.", "She gave me a lot of information."),
            ("I need an advice.", "I need some advice."),
            ("The news are good.", "The news is good."),
        ],
        "examples": [
            ("I need some advice.", "Mujhe thodi salah chahiye."),
            ("The news is good.", "Khabar achhi hai."),
            ("Please finish your homework.", "Please apna homework khatam karo."),
        ],
    },
    {
        "id": "articles_exc",
        "title": "Articles: when NOT to use 'a' or 'the'",
        "rule": "Kuch jagah article bilkul nahi lagta, aur kuch jagah 'the' zaroori hota hai.",
        "table": {
            "headers": ["Situation", "Rule", "Example"],
            "rows": [
                ["Meals", "article nahi", "I had breakfast at eight."],
                ["go to school / college / bed / work (normal use)", "article nahi", "She goes to college. I go to bed at ten."],
                ["Languages and subjects", "article nahi", "I speak Hindi. She studies physics."],
                ["Most countries and cities", "article nahi", "He lives in India."],
                ["Names like the UK, the USA, the Netherlands", "'the' lagta hai", "She is from the UK."],
                ["Rivers, oceans, mountain ranges", "'the' lagta hai", "the Ganges, the Pacific Ocean, the Himalayas"],
                ["Sirf ek hi cheez", "'the' lagta hai", "the sun, the moon, the sky"],
            ],
        },
        "mistakes": [
            ("I had the breakfast.", "I had breakfast."),
            ("He lives in the India.", "He lives in India."),
            ("I speak the Hindi.", "I speak Hindi."),
        ],
        "examples": [
            ("I had breakfast at eight.", "Maine aath baje nashta kiya."),
            ("She lives in India.", "Wo India mein rehti hai."),
            ("The sun rises in the east.", "Suraj poorab mein nikalta hai."),
        ],
    },
    {
        "id": "no_continuous",
        "title": "Verbs we don't use in -ing form",
        "rule": (
            "Kuch verbs feelings, thinking ya owning batate hain. Inhe aam taur par -ing form mein nahi bolte. "
            "'I am knowing' galat hai, 'I know' sahi hai."
        ),
        "note": "Dhyan rakho: 'think' -ing mein aa sakta hai jab matlab 'soch raha hoon' ho: I am thinking about my future.",
        "table": {
            "headers": ["Verb", "Wrong", "Right"],
            "rows": [
                ["know", "I am knowing the answer.", "I know the answer."],
                ["want", "I am wanting water.", "I want water."],
                ["like", "She is liking this song.", "She likes this song."],
                ["need", "We are needing help.", "We need help."],
                ["understand", "I am understanding it.", "I understand it."],
                ["believe", "I am believing you.", "I believe you."],
            ],
        },
        "examples": [
            ("I understand the rule.", "Mujhe rule samajh aata hai."),
            ("She likes this song.", "Use ye gaana pasand hai."),
            ("We need help.", "Humein madad chahiye."),
        ],
    },
    {
        "id": "subject_verb",
        "title": "Subject and verb: tricky cases",
        "rule": "Kuch words dekhne mein plural lagte hain par singular hote hain, aur kuch plural hote hain par singular jaise lagte hain.",
        "table": {
            "headers": ["Word", "Verb", "Example"],
            "rows": [
                ["news, mathematics, physics", "is (singular)", "The news is good. Mathematics is my favourite subject."],
                ["everyone, everybody, someone, nobody", "is (singular)", "Everyone is here."],
                ["police, people", "are (plural)", "The police are outside. People are waiting."],
                ["jeans, trousers, scissors", "are (plural)", "My jeans are blue."],
            ],
        },
        "mistakes": [
            ("The news are good.", "The news is good."),
            ("Everyone are here.", "Everyone is here."),
            ("The police is here.", "The police are here."),
        ],
        "examples": [
            ("Everyone is here.", "Sab log yahan hain."),
            ("The police are outside.", "Police bahar hai."),
            ("My jeans are blue.", "Meri jeans neeli hai."),
        ],
    },
    {
        "id": "comparatives",
        "title": "Comparing: better, worse and more",
        "rule": "Chhote adjectives mein -er / -est lagta hai; bade adjectives mein more / most. Kuch words irregular hain.",
        "table": {
            "headers": ["Word", "Comparative", "Superlative"],
            "rows": [
                ["good", "better", "best"],
                ["bad", "worse", "worst"],
                ["far", "farther / further", "farthest / furthest"],
                ["little", "less", "least"],
                ["many / much", "more", "most"],
                ["happy", "happier", "happiest"],
                ["beautiful", "more beautiful", "most beautiful"],
            ],
        },
        "mistakes": [
            ("more better", "better"),
            ("He is more taller than me.", "He is taller than me."),
            ("This is the most best movie.", "This is the best movie."),
        ],
        "examples": [
            ("This phone is better than that one.", "Ye phone us wale se behtar hai."),
            ("She is taller than her brother.", "Wo apne bhai se lambi hai."),
            ("This is the best day of my life.", "Ye meri zindagi ka sabse achha din hai."),
        ],
    },
    {
        "id": "prepositions_exc",
        "title": "Verbs that don't need a preposition",
        "rule": (
            "Hindi mein 'ke baare mein', 'tak' jaise words aate hain, isliye English mein bhi preposition laga dete hain. "
            "In verbs ke baad preposition nahi lagta."
        ),
        "note": "Dhyan rakho: 'enter into an agreement' sahi hai (alag matlab), lekin 'enter the room' mein 'into' nahi lagta.",
        "table": {
            "headers": ["Verb", "Wrong", "Right"],
            "rows": [
                ["discuss", "discuss about the plan", "discuss the plan"],
                ["reach", "reach to Delhi", "reach Delhi"],
                ["enter", "enter into the room", "enter the room"],
                ["marry", "marry with her", "marry her"],
                ["explain", "explain me the rule", "explain the rule to me"],
            ],
        },
        "examples": [
            ("Let's discuss the plan.", "Chalo plan ke baare mein baat karte hain."),
            ("We reached Delhi at noon.", "Hum dopahar mein Delhi pahunche."),
            ("She entered the room.", "Wo kamre mein aayi."),
        ],
    },
    {
        "id": "modals",
        "title": "Modal verbs: can, must, should",
        "rule": (
            "Modal verbs ke baad verb simple form mein aata hai. Unke baad 'to', -s ya -ing nahi lagta, "
            "he / she ke saath bhi nahi."
        ),
        "note": "Exception: 'have to', 'need to' aur 'ought to' mein 'to' aata hai.",
        "table": {
            "headers": ["Wrong", "Right"],
            "rows": [
                ["She can swims.", "She can swim."],
                ["He must to go.", "He must go."],
                ["You should to study.", "You should study."],
                ["I can speaking English.", "I can speak English."],
            ],
        },
        "examples": [
            ("She can swim.", "Wo tair sakti hai."),
            ("You should study every day.", "Tumhe roz padhna chahiye."),
            ("We have to leave now.", "Humein abhi nikalna hoga."),
        ],
    },
]

PASS_MARK = 3  # correct answers needed (out of 4) to complete a lesson
LESSON_XP = 30
