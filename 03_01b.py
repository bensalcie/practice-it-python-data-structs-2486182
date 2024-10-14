from collections import namedtuple
def can_take_order(driver,capacity):
    return driver.car_capacity>=capacity


def main():

    Driver = namedtuple("driver",["name","car_type","car_capacity"])
    
    bensalcie = Driver("Ben Salcie","volvoXC60",9)
    charity = Driver("Charity Muia","Demio",5)
    print(can_take_order(bensalcie,capacity=4))
    #add code here
    #create a driver with a name, car type, and car capacity
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    #check if they can take a certain order, given their car's capacity.
    return

if __name__ == "__main__":
    main()