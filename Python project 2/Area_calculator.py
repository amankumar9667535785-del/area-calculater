
while True:
    print("\n***************** Area Calculator ****************")
    print("""press 1 to get the Area of the Curved Surface of a cone
        presss 2 to get the Area of the Total surface area of a cone
        press 3 to get the Area of the Surface Area of a Sphere 
        press 4 to get the Area of the Curved Surface Area of a Hemisphere
        press 5 to get the Area of the Total Surface Area of a Hemisphere
        press 6  to get  Volume of the Cuboid 
        press 7 to get the Area of the Total surface area of the Cuboid 
        press 8 to get the Area of the Lateral surface area of the Cuboid 
        press 9 to get the Volume of the cube
        press 10 to get the Volume of the cylinder 
        press 11 to get the  curved surface Area  of the cylinder 
        press 12 to get the  Area of the Triangle 
        press 13 to get the Area of the Rectangle 
        press 14 to get the Area of the Parallelogram 
        press 15 to get the Area of the Rhombus
        press 16 to get the Area of the Trapezium 
        press 17 to Exits """)
    
    choice = int(input("number between the (1-17):"))
    if choice == 1:
        radius = float(input("enter the Radius of the Cone "))
        slant_height = float(input("enter the Slant_height of the Cone"))
        area = (22/7)*(radius)*(slant_height)

        print("The area of the Curved surface area of a Cone is",area)

    elif choice == 2:
        radius = float(input("enter the radius of the total surface Radius"))
        slant_height = float(input("enter the slant_height of the total surface"))
        area = (22/7)*(radius)*(slant_height+radius)

        print("The area of the total surface area of the cone is",area)

    elif choice == 3:
        radius = float(input("enter the radius of the Sphere"))
        area = 4*(22/7)*(radius**2)

        print("The area of the Sphere is",area)

    elif choice == 4:
        radius = float(input("enter the radius of the Hemisphere"))
        area = 2*(22/7)*(radius**2)

        print("The area of the Hemisphere is",area)

    elif choice == 5:
        radius = float(input("enter the radius of the total surface of hemisphere"))
        area = 3*(22/7)*(radius**2)

        print("The area of the total surface area of the hemisphere is",area)

    elif choice == 6:
        length = float(input("enter the length of the Cuboid"))
        height = float(input("enter the Height of the Cuboid "))
        wibth = float(input("enter the wibth of the Cuboid"))
        volume = (length*height*wibth)

        print("The volume of the Cuboid is",volume)

    elif choice==7:
        length = float(input("enter the length of the Total surface of cuboid "))
        wibth = float(input("enter the wibth of the total surface of cuboid"))
        height = float(input("enter the height of the total surface of cuboid"))
        total_area = 2*((length*wibth)+(wibth*height)+(length*height))

        print("The Total surface Area of the Cuboid is",total_area)

    elif choice== 8:
        length = float(input("enter the length of the Cuboid"))
        wibth = float(input("enter the wibth of the Cuboid "))
        height=float(input("enter the height of the Cuboid"))
        lateral_area = (2(length+wibth)*height)
        print("The Lateral surface area of the Cuboid is",lateral_area)
    
    elif choice ==9:
        one_side =float(input("enter the one side of the Cube"))
        volume=  one_side**3
        print("The Volume of the Cube is",volume)

    elif choice ==10:
        radius = float(input("enter the radius of the cylinder "))
        height = float(input("enter the height of the cylinder "))
        volume = (22/7)*(radius**2)*(height)
        print("The volume of the Cylinder is",volume)

    elif choice== 11:
        radius = float(input("enter the radius of the cylinder"))
        height = float(input("enter the height of the cylinder"))
        c_area = 2*((22/7)*radius*height)
        print("The curved surface area of the cylinder is",c_area)

    elif choice ==12:
        base = float(input("enter the base of the Triangle "))
        height = float(input("enter the height of the Triangle"))
        area = 1/2*(base*height)
        print("The area of the Triangle is",area)

    elif choice ==13:
        wibth= float(input("enter the wibth of the Rectangle "))
        length = float(input("enter the length of the Rectangle "))
        area = wibth *length
        print("The Area of the Rectangle is",area)

    elif choice ==14:
        base = float(input("enter the base of the Parallelogram"))
        height = float(input("enter the height of the Parallelogram "))
        area = base*height
        print("The Area of the Parallelogram is",area)
        
    elif choice== 15:
        d1 = float(input("enter the length of the first_diagonal of the Rhombus"))
        d2 = float(input("enter the length of the second_)diagonal of the Rhombus"))
        area = 1/2*(d1*d2)
        print("The Area of the Rhombus is",area)

    elif choice == 16:
        p_side1 =float(input("enter the length of the first parallel side of the Trapezium"))
        p_side2 = float(input("enter the length of the second parallel side of the Trapezium"))
        height = float(input("enter the height of the Trapezium "))
        area = 1/2*((p_side2+p_side2)*height)
        print("The Area of the Trapezium is",area)

    elif choice ==17:
        print("Thank You for using Area calculater ")

        break
    else:
        print("Invalid choice! Please try again")
