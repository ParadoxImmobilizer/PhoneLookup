import regex as re
import inquirer

questions = [
    inquirer.List('searchfor',
                  message="what do you want to search by?",
                  choices=['Name', 'Phone Number', 'Address', 'City', 'Email Address'],
                  ),
    inquirer.Text('search', message="what would you like to search for?")
]
answer = inquirer.prompt(questions)
f = open("data")

if answer["searchfor"] == "Name":
    m = [x.group() for x in re.finditer('^.*(?=(\|.*){4})', f.read(), re.MULTILINE)]
elif answer["searchfor"] == "Phone Number":
    m = [x.group() for x in re.finditer('(?<=(.*\|){1}).*(?=(\|.*){3})', f.read(), re.MULTILINE)]
elif answer["searchfor"] == "Address":
    m = [x.group() for x in re.finditer('(?<=(.*\|){2}).*(?=(\|.*){2})', f.read(), re.MULTILINE)]
elif answer["searchfor"] == "City":
    m = [x.group() for x in re.finditer('(?<=(.*\|){3}).*(?=(\|.*){1})', f.read(), re.MULTILINE)]
elif answer["searchfor"] == "Email Address":
    m = [x.group() for x in re.finditer('(?<=(.*\|){4}).*(?=(\|.*){0})', f.read(), re.MULTILINE)]
else:
    print(":(")

f = open("data")
data = f.readlines()
n = 0
for x in m:
    if answer["search"] in x:
        print(data[n].replace("|", " - "))
    n = n + 1
