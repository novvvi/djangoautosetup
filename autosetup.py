import os
import shutil
import subprocess
import time



class django(): 
    def __init__(self, call, project, app):
        self.local_dir = os.path.dirname(os.path.realpath(__file__)) 
        print (self.local_dir)
        self.call = call
        self.project = project
        self.app = app
        self.final = self.final(self.project)
        self.create_app = self.create_app(self.project, self.call, self.app)
        self.copyurl = self.copyurl(self.local_dir, self.project, self.app)
        self.settings_update = self.settings_update(self.app, self.project)
        self.urls_update = self.urls_update(self.app, self.project)



    def create_app(self, project, python, apps):
        print ("***************************************")
        print(os.getcwd())
        os.chdir(f"{project}/apps")
        for app in apps:
            
            comm1 = f'{python} ../manage.py startapp {app}'
            run1 = os.system(comm1)
            print (f"create {app}",run1)

            os.chdir(f"{app}")

            comm2 = f"mkdir templates & mkdir static"
            run2 = os.system(comm2)
            print (f"create template & static",run2)

            os.chdir("templates")

            comm3 = f"mkdir {app}"
            run3 = os.system(comm3)
            print (f"create template & static",run3)

            os.chdir("../..")
            print(os.getcwd())
        os.chdir("../..")
        print(os.getcwd())


    def copyurl(self, direct, project, apps):
        for app in apps: 
            src = f"{direct}/tmp/urls.py"
            des= f"{direct}/{project}/apps/{app}/urls.py"
            shutil.copyfile(src, des)


    def final(self, project):
        print ("***************************************")
        comm1 = f'django-admin startproject {project}'
        comm2 = f'mkdir apps'
        run1 = os.system(comm1)
        print ("created project",run1)
        print ("wait 3 secs until startproject complated")
        time.sleep(3)
        os.chdir(f"{project}")
        run2 = os.system(comm2)
        print ("created apps folder",run2)
        os.chdir("..")


    def settings_update(self, apps, project):
        print ("***************************************")
        print ("update settings.py")
        setting = "INSTALLED_APPS = ["
        for app in apps:
            setting += (f"\n    'apps.{app}','")
        s = open(f"{project}/{project}/settings.py").read()
        s = s.replace("INSTALLED_APPS = [", setting)
        f = open(f"{project}/{project}/settings.py", 'w')
        f.write(s)
        f.close()


    def urls_update(self, apps, project):
        print ("***************************************")
        print ("update urls.py")
        url = "    url(r'^admin/', admin.site.urls),"
        for app in apps:
            url += (f"\n    #url(r'^', include('apps.{app}.urls'),")
        s = open(f"{project}/{project}/urls.py").read()
        s = s.replace("    url(r'^admin/', admin.site.urls),", url)
        s = s.replace("from django.conf.urls import url", "from django.conf.urls import url, include")
        f = open(f"{project}/{project}/urls.py", 'w')
        f.write(s)
        f.close()


if __name__ == "__main__":
    py = input("Call py in cmd :")
    p_name = input("your project name :")
    app_names = input("your apps name Ex.(app1,app2) :").replace(" ", "").split(",")
    print (app_names)
    django( py, p_name,  app_names)
