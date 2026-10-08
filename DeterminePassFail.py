#La nota sera sobre 100
#La asistencia sera un porcentaje que se calculara con el total de calses y el numero de clases a las que hayas asistido.
exam_score = int(input ("¿Cual es tu nota en el exámen?: "))
total_classes = int(input ("¿Cuantas clases has tenido?: "))
attended_classes = int(input ("¿A cuantas clases has asistido?: "))
attended = attended_classes / total_classes * 100
if exam_score > 100 or attended > 100:

    print("Tu me estas vacilando")
else:
    if exam_score >= 70 and attended >=80:
        nota_final = exam_score /10
        if nota_final >= 8:
            print("Eres un maquina, has aprobado la asignatura con un", str(nota_final))
        else:
            print("Aprobado pero has ido justillo, has sacado un", float(nota_final))

    else:
        print("Has suspendido la asignatura")
        if exam_score < 70:
            nota_final_s = exam_score / 10
            print("Tu examen ha sido una mierda has sacado un", str(nota_final_s))
        else:
            print("Te ha faltado venir a clase")


