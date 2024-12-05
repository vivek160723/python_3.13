class company:
    company_name="vivek_internationals"

    def emp(self,name,post,company1):
        print(name,post,company1)

obj1=company()
obj1.emp("vivek","Founder",company.company_name)
obj1.emp("Gaurav","Manager",company.company_name)