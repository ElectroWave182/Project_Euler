total = 0

digits = [
	"",
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine",
]

dozens = [
	"",
	"ten",
	"twenty",
	"thirty",
	"forty",
	"fifty",
	"sixty",
	"seventy",
	"eighty",
	"ninety"
]


for number in range (1000):

    writing = ""


    # First part
    writing += digits[number // 100]
    if number >= 100:
        writing += "hundred"
        if number % 100 != 0:
            writing += "and"

    # Second part
    match number % 100:
        case 11:
            writing += "eleven"
        case 12:
            writing += "twelve"
        case 13:
            writing += "thirteen"
        case 15:
            writing += "fifteen"
        case 18:
            writing += "eighteen"
        case other:
            if 11 <= number % 100 <= 19:
                writing += digits[number % 10] + "teen"
            else:
                writing += dozens[number % 100 // 10] + digits[number % 10]


    total += len (writing)

total += len ("onethousand")

print (total)
