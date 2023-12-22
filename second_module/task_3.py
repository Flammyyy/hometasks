class Car:
    make = 'hyundai'
    model = 'sonata'
    year = 2017
    def display_info(make=make, model=model, year=year):
        print(make, model, year)

Car.display_info()