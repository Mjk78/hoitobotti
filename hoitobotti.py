import time

def greet():
    print("Hei. Olen hoitobotti. Ketä saan hoitaa tänään?")
    name = input("Anna nimesi: ").strip()
    
    if not name:
        print("Et antanut nimeä! Kutsun sinua nimellä 'Potilas'.")
        name = "Potilas"
    
    print(f"Tervetuloa vastaanotolle, {name}!")
    return name
    
    def ask_symptoms():
    time.sleep(1)
    symptoms = input("Mitä oireita sinulla on? (esim. yskä, kuume, päänsärky): ").strip().lower()
    
    if not symptoms:
        print("Et maininnut oireita. Seurantaa suositellaan.")
    else:
        analyze_symptoms(symptoms)

ef analyze_symptoms(symptoms):
    time.sleep(1)
    if "kuume" in symptoms or "ysk" in symptoms:
        print("Kuulostaa siltä, että sinulla saattaa olla flunssa. Lepoa ja runsaasti nestettä!")
    elif "päänsärky" in symptoms:
        print("Päänsärky voi johtua stressistä, koulutehtäviin ärsyyntymisestä tai nestehukasta. Muista juoda vettä!")
    else:
        print("Kiinnostavaa! Suosittelen kääntymään lääkärin puoleen lisädiagnoosia varten.")







main()
