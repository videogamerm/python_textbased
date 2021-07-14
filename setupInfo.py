import yaml 
name = input("What is your name? ")
info = {'name': name}
file = open('info.yml', 'w')
yaml.dump(info, file)
print(yaml.dump(info))
