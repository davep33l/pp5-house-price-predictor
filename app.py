from app_pages.multipage import MultiPage


# load pages scripts
from app_pages.project_summary import project_summary_body
from app_pages.project_hypothesis import project_hypothesis_body


app = MultiPage(app_name= "House Price Predictor") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Project Summary", project_summary_body)
app.add_page("Project Hypothesis", project_hypothesis_body)


app.run()