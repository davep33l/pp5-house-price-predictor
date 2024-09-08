from app_pages.multipage import MultiPage


# load pages scripts
from app_pages.project_summary import project_summary_body


app = MultiPage(app_name= "Placeholder Name for App") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", project_summary_body)


app.run()