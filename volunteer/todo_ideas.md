# Assignments Page
Create a class with key
If User get the key right
add his token to the list of Students
  class_model: (teacher_admin)
    class_name, teacher_username, students_username
  assignment_model: (teacher)
    class_name_foreignkey, assignment_id, title, description, date_assigned, date_due
  assignment_turnin_model: (student)
    assignment_id_foreignkey, assignment_content(with linebreak, like text docs), comment, students_username

Else user doesn't get the page right
reload page
