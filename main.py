import mysql.connector as m

con = m.connect(host="localhost", user="root", password="root", auth_plugin='mysql_native_password')

# CREATING DATABASE AND TABLE
cur = con.cursor()
cur.execute("create database if not exists nursery")
cur.execute("use nursery")
cur.execute("create table if not exists signup(username varchar(20),password varchar(20))")

while True:
    ch = int(input("SIGN UP [1] ; LOGIN [2] : "))
    # SIGNUP
    if ch == 1:
        username = input("USERNAME: ")
        pw = input("PASSWORD: ")
        cur.execute("insert into signup values('" + username + "','" + pw + "')")
        con.commit()
    # LOGIN
    elif ch == 2:
        username = input("USERNAME : ")
        cur.execute("select username from signup where username='" + username + "'")
        pot = cur.fetchone()
        if pot is not None:
            pw = input("PASSWORD 👁 : ")
            cur.execute("select password from signup where password='" + pw + "'")
            a = cur.fetchone()
            if a is not None:
                print("""LOGIN SUCCESSFUL""")

                print("""====================================================================================================================
++++++++++++++++++++++++++++++++++++++++++++++    𝐌𝐘 𝐏𝐋𝐀𝐍𝐓 𝐍𝐔𝐑𝐒𝐄𝐑𝐘     +++++++++++++++++++++++++++++++++++++++++++++
====================================================================================================================""")

                cur.execute(
                    "create table if not exists Available_Plants(Plant_Name varchar(30) primary key,Variety varchar("
                    "20),Quantity int(3),Import_Location varchar(30),Price int(4))")
                cur.execute(
                    "create table if not exists Sell_rec(CustomerName varchar(20),Phone_Number char(10) unique key, "
                    "Plant_Name varchar(30),Quantity int(100),Price int(4),foreign key (Plant_Name) references "
                    "Available_Plants(Plant_Name))")
                cur.execute(
                    "create table if not exists Staff_details(Name varchar(30), Gender varchar(10),Age int(3), "
                    "Phone_Number char(10) unique key , Address varchar(40))")
                con.commit()

                while True:
                    print("""1:Add Plant record
2:Buy Plants 
3:Search Plants
4:Staff Details
5:Sales Record
6:Available Plants
7:Total Income after the Latest Reset 
8:Exit""")

                    a = int(input("Enter your choice:"))

                    # ADD PLANTS
                    if a == 1:
                        plant = str(input("Plant Name: "))
                        variety = str(input("Variety: "))
                        quantity = int(input("Quantity: "))
                        import_location = str(input("Plant import location: "))
                        price = int(input("Enter the price: "))

                        cur.execute("select * from Available_Plants where Plant_Name ='" + plant + "'")
                        row = cur.fetchone()

                        if row is not None:
                            cur.execute("update Available_Plants set quantity=quantity+'" + str(
                                quantity) + "' where Plant_Name='" + plant + "'")
                            con.commit()

                            print("""++++++++++++++++++++++
++SUCCESSFULLY ADDED++
++++++++++++++++++++++""")

                        else:
                            cur.execute(
                                "insert into Available_Plants(Plant_Name,variety,quantity,Import_Location,"
                                "price) values('" + plant + "','" + variety + "','" + str(
                                    quantity) + "','" + import_location + "','" + str(price) + "')")
                            con.commit()

                            print("""++++++++++++++++++++++
++SUCCESSFULLY ADDED++
++++++++++++++++++++++""")

                            # SELL PLANT
                    elif a == 2:

                        print("AVAILABLE PLANTS...")

                        cur.execute("select * from Available_Plants ")
                        for x in cur:
                            print(x)

                        customer_name = str(input("Enter customer name:"))
                        phone_no = int(input("Enter phone number:"))
                        plant = str(input("Enter Plant Name:"))
                        price = int(input("Enter the price:"))
                        n = int(input("Enter quantity:"))

                        cur.execute("select quantity from available_plants where Plant_Name='" + plant + "'")
                        lk = cur.fetchone()

                        if max(lk) < n:
                            print(n, "Plants are not available!!!!")

                        else:
                            cur.execute("select Plant_Name from available_plants where Plant_Name='" + plant + "'")
                            log = cur.fetchone()

                            if log is not None:
                                cur.execute("insert into Sell_rec values('" + customer_name + "','" + str(
                                    phone_no) + "','" + plant + "','" + str(n) + "','" + str(price) + "')")
                                cur.execute("update Available_plants set quantity=quantity-'" + str(
                                    n) + "' where Plant_Name='" + plant + "'")
                                con.commit()

                                print("""++++++++++++++++++++++
++PLANT HAS BEEN SOLD++
++++++++++++++++++++++""")

                            else:
                                print("PLANT IS NOT AVAILABLE!!!!!!!")

                    # SEARCH PLANTS ON THE BASIS OF GIVEN OPTIONS
                    elif a == 3:

                        print("""1:Search by name
2:Search by variety
3:Search by Import Location""")

                        search = int(input("Search by?:"))

                        # BY PLANT NAME
                        if search == 1:
                            plant_search = input("Enter Plant to search:")

                            cur.execute(
                                "select Plant_Name from available_plants where Plant_Name='" + plant_search + "'")
                            tree = cur.fetchone()

                            if tree is not None:
                                print("""++++++++++++++++++++
++PLANT IS IN STOCK++
++++++++++++++++++++""")

                            else:
                                print("PLANT IS NOT IN STOCK!!!!!!!")

                        # BY VARIETY
                        elif search == 2:
                            variety_search = input("Enter variety to search:")

                            cur.execute("select variety from available_plants where variety='" + variety_search + "'")
                            poll = cur.fetchall()

                            if poll is not None:
                                print("""++++++++++++++++++++
++PLANT IS IN STOCK++
++++++++++++++++++++""")

                                cur.execute("select * from available_plants where variety='" + variety_search + "'")

                                for y in cur:
                                    print(y)

                            else:
                                print("PLANTS OF SUCH VARIETY ARE NOT AVAILABLE!!!!!!!!!")

                        # BY IMPORT LOCATION
                        elif search == 3:
                            location_search = input("Enter Import location to search:")

                            cur.execute(
                                "select Import_Location from available_plants where Import_Location='" + location_search + "'")
                            home = cur.fetchall()

                            if home is not None:
                                print("""++++++++++++++++++++
++PLANT IS IN STOCK++
++++++++++++++++++++""")

                                cur.execute(
                                    "select * from available_plants where Import_Location='" + location_search + "'")

                                for z in cur:
                                    print(z)

                            else:
                                print("PLANTS FROM THIS LOCATION ARE NOT AVAILABLE!!!!!!!")
                        con.commit()

                    # STAFF DETAILS
                    elif a == 4:
                        print("1:New staff entry")
                        print("2:Remove staff")
                        print("3:Existing staff details")

                        ch = int(input("Enter your choice:"))

                        # NEW STAFF ENTRY
                        if ch == 1:
                            f_name = str(input("Enter Fullname:"))
                            gender = str(input("Gender(M/F/O):"))
                            age = int(input("Age:"))
                            phone_no = int(input("Staff phone no.:"))
                            add = str(input("Address:"))

                            cur.execute(
                                "insert into Staff_details(name,gender,age,Phone_Number,address) values('" + f_name + "','" + gender + "','" + str(
                                    age) + "','" + str(phone_no) + "','" + add + "')")
                            print("""+++++++++++++++++++++++++++++
+STAFF IS SUCCESSFULLY ADDED+
+++++++++++++++++++++++++++++""")
                            con.commit()

                        # REMOVE STAFF
                        elif ch == 2:
                            nm = str(input("Enter staff name to remove:"))
                            cur.execute("select name from staff_details where name='" + nm + "'")
                            toy = cur.fetchone()

                            if toy is not None:
                                cur.execute("delete from staff_details where name='" + nm + "'")
                                print("""+++++++++++++++++++++++++++++++++
++STAFF IS SUCCESSFULLY REMOVED++
+++++++++++++++++++++++++++++++++""")
                                con.commit()

                            else:
                                print("STAFF DOES NOT EXIST!!!!!!")

                        # EXISTING STAFF DETAILS
                        elif ch == 3:
                            cur.execute("select * from Staff_details")
                            run = cur.fetchone()
                            for t in cur:
                                print(t)
                            if run is not None:
                                print("EXISTING STAFF DETAILS...")
                                for t in cur:
                                    print(t)

                            else:
                                print("NO STAFF EXISTS!!!!!!!")
                            con.commit()

                    # SALES RECORD
                    elif a == 5:
                        print("1:Sales Record")
                        print("2:Reset Sales Record")

                        ty = int(input("Enter your choice:"))

                        if ty == 1:
                            cur.execute("select * from sell_rec")
                            for u in cur:
                                print(u)

                        if ty == 2:
                            bb = input("Are you sure(Y/N): ")

                            if bb == "Y":
                                cur.execute("delete from sell_rec")
                                con.commit()

                            elif bb == "N":
                                pass

                    # AVAILABLE PLANTS
                    elif a == 6:
                        cur.execute("select * from available_plants order by Plant_Name")
                        for v in cur:
                            print(v)

                    # TOTAL INCOME AFTER LATEST UPDATE
                    elif a == 7:
                        cur.execute("select sum(price) from sell_rec")
                        for x in cur:
                            print(x)
                    # EXIT
                    elif a == 8:
                        break

            # LOGIN ELSE PART
            else:
                print("Incorrect Password.")

        else:
            print("Invalid username.")

    else:
        break
