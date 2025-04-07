import time

def greet():
    print("Hei. Olen hoitobotti. Ketä saan hoitaa tänään?")
    name = input("Anna nimesi: ").strip()
    
    if not name:
        print("Et antanut nimeä! Kutsun sinua nimellä 'Potilas'.")
        name = "Potilas"
    
    print(f"Tervetuloa vastaanotolle, {name}!")
    return name







main()
