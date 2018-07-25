person = {'name':'Nick', 'address':'cheonan', 'email':'aa@naver.com'}

print(person['name'])

for key, value in person.items():
    print("\nkey \\ '" + key + "'" )
    print("value \\ '" + value+ "'")

# 역슬래시를 그대로 출력하고 싶으면 \\ 두개 입력해야함