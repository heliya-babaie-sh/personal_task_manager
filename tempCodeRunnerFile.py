load_dotenv()
admin_password = os.getenv("TASK_ADMIN_PASSWORD")
open_admin = input("do you want to open admin mode? yes/no: ")
if open_admin.lower() == "yes":
    entered_password = input("enter admin password: ")

    if entered_password == admin_password:
        print("admin, hello")
    else:
        print("wrong password")
