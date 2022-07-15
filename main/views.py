from django.shortcuts import render
from random import *
from random import randint

# Create your views here.
def index(request):
    listTeams = []
    qtdGroups_input = 0
    if request.method == 'POST':
        titulo_input = request.POST['titulo_input']
        nomes_input = request.POST['nomes_input']
        qtdGroups_input = request.POST['qtdGroups_input']

        new_nomes_input = nomes_input.replace(" ", "")
        new_nomes_input = new_nomes_input.split(",")

        qtdGroups_input = int(qtdGroups_input)

        # Definir o tanto de times
        teams = {}
        for i in range(qtdGroups_input):
            teams[i+1] = ""

        members = []
        for i in range(qtdGroups_input):
            members.append([])
        count = 0

        for i in range(len(new_nomes_input)):
            if count < qtdGroups_input:
                members[count].append(new_nomes_input.pop(randint(0,len(new_nomes_input)-1)))
                count += 1
            else:
                count = 0
                members[count].append(new_nomes_input.pop(randint(0,len(new_nomes_input)-1)))
                count += 1
                
        # listTeams = []
        # print("nomes: ",nomes_input)
        # print("inputzinho:",new_nomes_input)
        # print("ESTE SAO OS MEMBROS SO ESSE: ",members)
        count = 0
        for i in range(qtdGroups_input):
            teams[i+1] = members[i].copy()
            
        listTeams.append(teams)
        # print(listTeams)

        #groups(request, variavel=listTeams)
        return render(request, 'groups.html', {"showGrups":listTeams, "qtd": range(1,qtdGroups_input+1), "titulo":titulo_input})
    return render(request, 'index.html')


def groups(request):
    return render(request, 'groups.html')
