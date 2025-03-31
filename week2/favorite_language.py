favorite_languages ={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    
}

language = favorite_languages['sarah']
print(f"sarah's favorite language is {language}")

language2 = favorite_languages.get('je','person does not exist')
print(language2.title())