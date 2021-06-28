import os, time
from codestats import api
from termcolor import colored

def progressBar(amount, ratio=0.4):
    amount = round(amount * ratio)
    return (colored("#", attrs=['bold']) * amount) + "-" * round(100 * ratio)

currentLanguage = "None"; currentMachine = "None"
previousLanguageXP = {}; previousMachineXP = {}
username = input("Username: ")

while True:
    time.sleep(1); user = api.User(username); os.system("clear")
    print(f"{colored(user.name, attrs=['bold'])}: [{progressBar(user.progress, ratio=0.46)}] {colored(str(round(user.progress)) + '%', attrs=['bold'])} ({colored(str(user.total_xp) + ' XP', attrs=['bold'])}, {colored('Level ' + str(user.level), attrs=['bold'])})")
    languages = {}; topLanguages = []; index = 0
    for language in user.languages:
        try:
            if language.experience > previousLanguageXP[language.name]:
                currentLanguage = language.name
        except:
            pass
        previousLanguageXP[language.name] = language.experience
        languages[language.name] = language.experience
    languages = dict(sorted(languages.items(), key=lambda item: item[1]))
    for language in languages:
        if len(languages) - index <= 3:
            for userLanguage in user.languages:
                if userLanguage.name == language:
                    topLanguages.append(f"{language} ({colored(str(languages[language]) + ' XP', attrs=['bold'])}, {colored('Level ' + str(userLanguage.level), attrs=['bold'])})")
        index += 1
    print(colored("Top Languages: ", attrs=["bold"]), end=""); print(f"{', '.join(reversed(topLanguages))}")

    machines = {}; topMachines = []; index = 0
    for machine in user.machines:
        try:
            if machine.experience > previousMachineXP[machine.name]:
                currentMachine = machine.name
        except:
            pass
        previousMachineXP[machine.name] = machine.experience
        machines[machine.name] = machine.experience
    machines = dict(sorted(machines.items(), key=lambda item: item[1]))
    for machine in machines:
        if len(machines) - index <= 3:
            for userMachine in user.machines:
                if userMachine.name == machine:
                    topMachines.append(f"{machine} ({colored(str(machines[machine]) + ' XP', attrs=['bold'])}, {colored('Level ' + str(userMachine.level), attrs=['bold'])})")
        index += 1
    print(colored("Top Machines: ", attrs=["bold"]), end=""); print(f"{', '.join(reversed(topMachines))}")
    print(colored("Current Language: ", attrs=["bold"]), end=""); print(currentLanguage, end=", ")
    print(colored("Current Machine: ", attrs=["bold"]), end=""); print(currentMachine, end=", ")
    print(colored("New Experience: ", attrs=["bold"]), end=""); print(str(user.new_xp) + " XP")
