while True:
    print("===============================\n WELCOME TO MYHOSPITAL\n===============================")

    import mysql.connector

    passwd = str(input("ENTER THE DATABASE PASSWORD: "))

    mysql = mysql.connector.connect(host="localhost", user="root", passwd=passwd)
    mycursor = mysql.cursor()

    mycursor.execute("create database if not exists my_hospitals")
    mycursor.execute("use my_hospitals")

    mycursor.execute(
        "create table if not exists patient_details(puid int(10) primary key,name varchar(30) not null,age int(3),address varchar(50),doctor_recommended varchar(30))"
    )
    mycursor.execute(
        "create table if not exists doctor_details(name varchar(30) primary key,specialisation varchar(40),age int(2),address varchar(30),contact varchar(15),fees int(10),monthly_salary int(10))"
    )
    mycursor.execute(
        "create table if not exists nurse_details(name varchar(30) primary key,age int(2),address varchar(30),contact varchar(15),monthly_salary int(10))"
    )
    mycursor.execute(
        "create table if not exists other_workers_details(name varchar(30) primary key,age int(2),address varchar(30),contact varchar(15),monthly_salary int(10))"
    )

    mycursor.execute(
        "create table if not exists user_data(username varchar(30) primary key,password varchar(30) default'000')"
    )

    while True:
        print("1. SIGN IN (LOGIN)\n2. SIGN UP (REGISTER)")
        r = int(input("enter your choice: "))

        if r == 2:
            print(
                "=======================================\n!!!!!!!PLEASE REGISTER YOURSELF!!!!!!!!\n======================================="
            )
            u = input("ENTER YOUR PREFERRED USERNAME!!: ")
            p = input("ENTER YOUR PREFERRED PASSWORD (PASSWORD SHOULD BE STRONG!!!): ")

            mycursor.execute("insert into user_data values('" + u + "','" + p + "')")
            mysql.commit()

            print(
                "=======================================\n!!!!!!!REGISTERED SUCCESSFULLY!!!!!!!!\n======================================="
            )
            x = input("enter any key to continue: ")

        elif r == 1:
            print(
                "========================================\n!!!!!!!  {{SIGN IN }}  !!!!!!!!!!\n========================================"
            )
            un = input("ENTER THE USERNAME!!: ")
            ps = input("ENTER THE PASSWORD!!: ")

            mycursor.execute(
                "select password from user_data where username='" + un + "'"
            )
            row = mycursor.fetchall()

            for i in row:
                a = list(i)
                if a[0] == str(ps):
                    while True:
                        print(
                            "1.ADMINISTRATION\n2.PATIENT (ADMISSION NAD DISCHARGE PROCESS)\n3.SIGN OUT"
                        )
                        a = int(input("ENTER YOUR CHOICE: "))

                        if a == 1:
                            print(
                                "1. SHOW DETAILS\n2. ADD NEW MEMBER\n3. DELETE EXISTING ONE\n4. EXIT"
                            )
                            b = int(input("ENTER YOUR CHOICE: "))

                            if b == 1:
                                print(
                                    "1. DOCTOR DETAILS\n2. NURSE DETAILS\n3. OTHER WORKERS"
                                )
                                c = int(input("ENTER YOUR CHOICE: "))

                                if c == 1:
                                    mycursor.execute("select * from doctor_details")
                                    row = mycursor.fetchall()
                                    for i in row:
                                        b = 0
                                        v = list(i)
                                        k = [
                                            "NAME",
                                            "SPECIALISATION",
                                            "AGE",
                                            "ADDRESS",
                                            "CONTACT",
                                            "FEES",
                                            "MONTHLY_SALARY",
                                        ]
                                        d = dict(zip(k, v))
                                        print(d)

                                elif c == 2:
                                    mycursor.execute("select * from nurse_details")
                                    row = mycursor.fetchall()
                                    for i in row:
                                        v = list(i)
                                        k = [
                                            "NAME",
                                            "SPECIALISATION",
                                            "AGE",
                                            "ADDRESS",
                                            "CONTACT",
                                            "MONTHLY_SALARY",
                                        ]
                                        d = dict(zip(k, v))
                                        print(d)

                                elif c == 3:
                                    mycursor.execute(
                                        "select * from other_workers_details"
                                    )
                                    row = mycursor.fetchall()
                                    for i in row:
                                        v = list(i)
                                        k = [
                                            "NAME",
                                            "SPECIALISATION",
                                            "AGE",
                                            "ADDRESS",
                                            "CONTACT",
                                            "MONTHLY_SALARY",
                                        ]
                                        d = dict(zip(k, v))
                                        print(d)

                            elif b == 2:
                                print(
                                    "1. DOCTOR DETAILS\n2. NURSE DETAILS\n3. OTHER WORKERS"
                                )
                                c = int(input("ENTER YOUR CHOICE: "))

                                if c == 1:
                                    name = input("ENTER DR. NAME: ")
                                    spe = input("ENTER SPECIALISATION: ")
                                    age = input("ENTER AGE: ")
                                    add = input("ENTER ADDRESS: ")
                                    cont = input("ENTER CONTACT NO.: ")
                                    fees = input("ENTER FEES: ")
                                    ms = input("ENTER MONTHLY_SALARY: ")

                                    mycursor.execute(
                                        "insert into doctor_details values('"
                                        + name
                                        + "','"
                                        + spe
                                        + "','"
                                        + age
                                        + "','"
                                        + add
                                        + "','"
                                        + cont
                                        + "','"
                                        + fees
                                        + "','"
                                        + ms
                                        + "')"
                                    )
                                    mysql.commit()
                                    print("SUCCESSFULLY ADDED")

                                elif c == 2:
                                    name = input("ENTER NURSE NAME: ")
                                    age = input("ENTER AGE: ")
                                    add = input("ENTER ADDRESS: ")
                                    cont = input("ENTER CONTACT NO.: ")
                                    ms = int(input("ENTER MONTHLY_SALARY: "))

                                    mycursor.execute(
                                        "insert into nurse_details values('"
                                        + name
                                        + "','"
                                        + age
                                        + "','"
                                        + add
                                        + "','"
                                        + cont
                                        + "','"
                                        + str(ms)
                                        + "')"
                                    )
                                    mysql.commit()
                                    print("SUCCESSFULLY ADDED")

                                elif c == 3:
                                    name = input("ENTER WORKER NAME: ")
                                    age = input("ENTER AGE: ")
                                    add = input("ENTER ADDRESS: ")
                                    cont = input("ENTER CONTACT NO.: ")
                                    ms = input("ENTER MONTHLY_SALARY: ")

                                    mycursor.execute(
                                        "insert into other_workers_details values('"
                                        + name
                                        + "','"
                                        + age
                                        + "','"
                                        + add
                                        + "','"
                                        + cont
                                        + "','"
                                        + ms
                                        + "')"
                                    )
                                    mysql.commit()
                                    print("SUCCESSFULLY ADDED")

                            elif b == 3:
                                print(
                                    "1. DOCTOR DETAILS\n2. NURSE DETAILS\n3. OTHER WORKERS"
                                )
                                c = int(input("ENTER YOUR CHOICE: "))

                                if c == 1:
                                    name = input("ENTER DOCTOR'S NAME: ")
                                    mycursor.execute(
                                        "select * from doctor_details where name=='"
                                        + name
                                        + "'"
                                    )
                                    row = mycursor.fetchall()
                                    print(row)
                                    p = input(
                                        "you really wanna delete this data? (y/n): "
                                    )

                                    if p == "y":
                                        mycursor.execute(
                                            "delete from doctor_details where name='"
                                            + name
                                            + "'"
                                        )
                                        mysql.commit()
                                        print("SUCCESSFULLY DELETED!!")
                                    else:
                                        print("NOT DELETED")

                                elif c == 2:
                                    name = input("ENTER NURSE NAME: ")
                                    mycursor.execute(
                                        "select * nurse_details where name=='"
                                        + name
                                        + "'"
                                    )
                                    row = mycursor.fetchall()
                                    print(row)
                                    p = input(
                                        "you really wanna delete this data? (y/n): "
                                    )

                                    if p == "y":
                                        mycursor.execute(
                                            "delete from nurse_details where name='"
                                            + name
                                            + "'"
                                        )
                                        mysql.commit()
                                        print("SUCCESSFULLY DELETED!!")
                                    else:
                                        print("NOT DELETED")

                                elif c == 3:
                                    name = input("ENTER THE WORKER NAME: ")
                                    mycursor.execute(
                                        "select * from workers_details where name=='"
                                        + name
                                        + "'"
                                    )
                                    row = mycursor.fetchall()
                                    print(row)
                                    p = input(
                                        "you really wanna delete this data? (y/n): "
                                    )

                                    if p == "y":
                                        mycursor.execute(
                                            "delete from other_workers_details where name='"
                                            + name
                                            + "'"
                                        )
                                        mysql.commit()
                                        print("SUCCESSFULLY DELETED!!")
                                    else:
                                        print("NOT DELETED")

                            elif b == 4:
                                break

                        elif a == 2:
                            print(
                                "1. SHOW PATIENT DETAILS\n2. ADD NEW PATIENT\n3. DISCHARGE PATIENT\n4. EXIT"
                            )
                            b = int(input("ENTER YOUR CHOICE: "))

                            if b == 1:
                                mycursor.execute("select * from patient_details")
                                row = mycursor.fetchall()
                                for i in row:
                                    b = 0
                                    v = list(i)
                                    k = ["NAME", "SEX", "AGE", "ADDRESS", "CONTACT"]
                                    d = dict(zip(k, v))
                                    print(d)

                            elif b == 2:
                                name = str(input("ENTER NAME: "))
                                sex = str(input("ENTER SEX: "))
                                age = str(input("ENTER AGE: "))
                                address = str(input("ADDRESS: "))
                                contact = str(input("CONTACT NUMBER: "))

                                mycursor.execute(
                                    "insert into patient_details values('"
                                    + str(name)
                                    + "','"
                                    + str(sex)
                                    + "','"
                                    + str(age)
                                    + "','"
                                    + str(address)
                                    + "','"
                                    + str(contact)
                                    + "')"
                                )
                                mysql.commit()

                                mycursor.execute("select * from patient_details")
                                for i in mycursor:
                                    v = list(i)
                                    k = ["NAME", "SEX", "AGE", "ADDRESS", "CONTACT"]
                                    print(dict(zip(k, v)))
                                    print(
                                        "=======================================\n!!!!!!!REGISTERED SUCCESSFULLY!!!!!!!!\n======================================="
                                    )

                            elif b == 3:
                                name = input("ENTER THE PATIENT NAME: ")
                                mycursor.execute(
                                    "select * from patient_details where name='"
                                    + name
                                    + "'"
                                )
                                row = mycursor.fetchall()
                                print(row)
                                bill = input("HAS HE PAID ALL THE BILLS ? (y/n): ")

                                if bill == "y":
                                    mycursor.execute(
                                        "delete from patient_details where name='"
                                        + name
                                        + "'"
                                    )
                                    mysql.commit()

                            elif b == 4:
                                break

                        elif a == 3:
                            break

                else:
                    break
