import string
import keyword

print('Input name which don`t start with number, have big letters, don`t have punctuation despite of "_", is not word from registr')
name = input('Name ')
has_upper = any(char.isupper() for char in name)
punctuation_without_underscore = string.punctuation.replace("_", "")   #Перевірка пунктуації
has_punctuation = any(char in punctuation_without_underscore for char in name)   #Перевірка пунктуації


if (
        not name[0].isdigit()  #Починається не із цифри
        and has_upper             #Має великі літери
        and not has_punctuation   #Перевірка пунктуації
        and not keyword.iskeyword(name)  # Перевірка на ключові слова
):
    my_string = f"Привіт {name}!"
    print(my_string)

else:
    print('Write according to rules')


