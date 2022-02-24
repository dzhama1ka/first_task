name = "Джамал"
print(name)

age = 20
print("Меня зовут", name, ", и мне ", age, "лет.")

name_dzhem = (name + " ") * (5)
print(name_dzhem)

print("Здравствуйте! Давайте знакомиться!")
name_user_str=input("Как вас зовут?" )
if not name_user_str.rfind(" ") == -1:
    print("Так, давайте без пробелов...")
    quit()

sex_user = input("Ваш пол? (М/Ж)" )
sex_user_str = str(sex_user)
if sex_user_str == "М":
    sex_user_str = "Мужской"
elif sex_user_str == "Ж":
    sex_user_str = "Женский"

age_user_str= input("А лет сколько Вам?" )
age_user_int = int(age_user_str)
if age_user_int < 0 or age_user_int > 150:
    print("Врать вот не надо было!")
    quit()

print("Очень приятно," + name_user_str + "!")
print("Ого, да Вам уже " + age_user_str + "? По Вам не скажешь, я бы дал, от силы, лет 14!")



if age_user_int > 60 and age_user_int < 100 and sex_user_str == "Мужской":
    print("Да Вы мне в дедули годитесь!")
if age_user_int > 60 and age_user_int < 100 and sex_user_str == "Женский":
    print("Да Вы мне в бабули годитесь!")

if age_user_int > 18 and age_user_int < 59 and sex_user_str == "Мужской":
    print("Почти ровесник!")
if age_user_int > 18 and age_user_int < 59 and sex_user_str == "Женский":
    print("Почти ровесница!")

print(name_user_str[1:], name_user_str[::-1], name_user_str[-3:], name_user_str[:5])

sum = 0
pro = 1
for i in range(2):
    sum = sum + int(str(age_user_int)[i])
    pro = pro * int(str(age_user_int)[i])
print(len(name_user_str), sum, pro, end="\n", sep="\n")

name_user_str = name_user_str.upper()
print(name_user_str.upper(), name_user_str.lower(), name_user_str.capitalize(), name_user_str[0].lower() + name_user_str[1:].upper() , sep="\n", end="\n")

user_answer = input("Сколько будет 25+4*9? Ответ: ")
if user_answer == "61":
    answer = "Верно!"
else:
    answer = "Вы ошиблись!"
print(answer)