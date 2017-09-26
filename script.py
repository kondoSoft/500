from mxvscorrupcion.models import *



def createCompany(empresa):
    questions = open('preguntas.csv')
    questions = list(questions)
    country = Paises.objects.get(pais=empresa[2])
    sectors = Sectores.objects.get(nombre=empresa[1])
    respuestas = empresa[5:41]
    questionary = Cuestionario()
    questionary.save()
    for i in range(0,36):
        question = Pregunta(text_pregunta = questions[i], respuesta = respuestas[i])
        question.save()
        questionary.preguntas.add(question)

    company = Empresa(nombre = empresa[0], sector = sectors, pais = country, website_corporativo = empresa[3], website_integridad = empresa[4], cuestionario = questionary)
    company.save()