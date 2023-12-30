import json

bible_books = [
    {"name": "창세기", "english_name": "Genesis", "chapters": 50},
    {"name": "출애굽기", "english_name": "Exodus", "chapters": 40},
    {"name": "레위기", "english_name": "Leviticus", "chapters": 27},
    {"name": "민수기", "english_name": "Numbers", "chapters": 36},
    {"name": "신명기", "english_name": "Deuteronomy", "chapters": 34},
    {"name": "여호수아", "english_name": "Joshua", "chapters": 24},
    {"name": "사사기", "english_name": "Judges", "chapters": 21},
    {"name": "룻기", "english_name": "Ruth", "chapters": 4},
    {"name": "사무엘상", "english_name": "1 Samuel", "chapters": 31},
    {"name": "사무엘하", "english_name": "2 Samuel", "chapters": 24},
    {"name": "열왕기상", "english_name": "1 Kings", "chapters": 22},
    {"name": "열왕기하", "english_name": "2 Kings", "chapters": 25},
    {"name": "역대상", "english_name": "1 Chronicles", "chapters": 29},
    {"name": "역대하", "english_name": "2 Chronicles", "chapters": 36},
    {"name": "에스라", "english_name": "Ezra", "chapters": 10},
    {"name": "느헤미야", "english_name": "Nehemiah", "chapters": 13},
    {"name": "에스더", "english_name": "Esther", "chapters": 10},
    {"name": "욥기", "english_name": "Job", "chapters": 42},
    {"name": "시편", "english_name": "Psalms", "chapters": 150},
    {"name": "잠언", "english_name": "Proverbs", "chapters": 31},
    {"name": "전도서", "english_name": "Ecclesiastes", "chapters": 12},
    {"name": "아가", "english_name": "Song of Solomon", "chapters": 8},
    {"name": "이사야", "english_name": "Isaiah", "chapters": 66},
    {"name": "예레미야", "english_name": "Jeremiah", "chapters": 52},
    {"name": "예레미야애가", "english_name": "Lamentations", "chapters": 5},
    {"name": "에스겔", "english_name": "Ezekiel", "chapters": 48},
    {"name": "다니엘", "english_name": "Daniel", "chapters": 12},
    {"name": "호세아", "english_name": "Hosea", "chapters": 14},
    {"name": "요엘", "english_name": "Joel", "chapters": 3},
    {"name": "아모스", "english_name": "Amos", "chapters": 9},
    {"name": "오바댜", "english_name": "Obadiah", "chapters": 1},
    {"name": "요나", "english_name": "Jonah", "chapters": 4},
    {"name": "미가", "english_name": "Micah", "chapters": 7},
    {"name": "나훔", "english_name": "Nahum", "chapters": 3},
    {"name": "하박국", "english_name": "Habakkuk", "chapters": 3},
    {"name": "스바냐", "english_name": "Zephaniah", "chapters": 3},
    {"name": "학개", "english_name": "Haggai", "chapters": 2},
    {"name": "스가랴", "english_name": "Zechariah", "chapters": 14},
    {"name": "말라기", "english_name": "Malachi", "chapters": 4},
    {"name": "마태복음", "english_name": "Matthew", "chapters": 28},
    {"name": "마가복음", "english_name": "Mark", "chapters": 16},
    {"name": "누가복음", "english_name": "Luke", "chapters": 24},
    {"name": "요한복음", "english_name": "John", "chapters": 21},
    {"name": "사도행전", "english_name": "Acts", "chapters": 28},
    {"name": "로마서", "english_name": "Romans", "chapters": 16},
    {"name": "고린도전서", "english_name": "1 Corinthians", "chapters": 16},
    {"name": "고린도후서", "english_name": "2 Corinthians", "chapters": 13},
    {"name": "갈라디아서", "english_name": "Galatians", "chapters": 6},
    {"name": "에베소서", "english_name": "Ephesians", "chapters": 6},
    {"name": "빌립보서", "english_name": "Philippians", "chapters": 4},
    {"name": "골로새서", "english_name": "Colossians", "chapters": 4},
    {"name": "데살로니가전서", "english_name": "1 Thessalonians", "chapters": 5},
    {"name": "데살로니가후서", "english_name": "2 Thessalonians", "chapters": 3},
    {"name": "디모데전서", "english_name": "1 Timothy", "chapters": 6},
    {"name": "디모데후서", "english_name": "2 Timothy", "chapters": 4},
    {"name": "디도서", "english_name": "Titus", "chapters": 3},
    {"name": "빌레몬서", "english_name": "Philemon", "chapters": 1},
    {"name": "히브리서", "english_name": "Hebrews", "chapters": 13},
    {"name": "야고보서", "english_name": "James", "chapters": 5},
    {"name": "베드로전서", "english_name": "1 Peter", "chapters": 5},
    {"name": "베드로후서", "english_name": "2 Peter", "chapters": 3},
    {"name": "요한일서", "english_name": "1 John", "chapters": 5},
    {"name": "요한이서", "english_name": "2 John", "chapters": 1},
    {"name": "요한삼서", "english_name": "3 John", "chapters": 1},
    {"name": "유다서", "english_name": "Jude", "chapters": 1},
    {"name": "요한계시록", "english_name": "Revelation", "chapters": 22},
]

# JSON 파일로 저장
with open("bible_books.json", "w") as json_file:
    json.dump(bible_books, json_file, indent=2, ensure_ascii=False)

print("bible_books.json 파일이 생성되었습니다.")
