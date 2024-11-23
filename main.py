from streamlit import *

set_page_config(page_title="My First Web Page Using Python", page_icon=':tada:', layout='wide')

with container:
    subheader('Hi, My Name is Mudit! :wave:')
    title('I am a student from New Delhi, India')
    write('I am a new programmer and I am passionately eager to learn new things.')
    write('[Learn more >](https://www.youtube.com/watch?v=dQw4w9WgXcQ)')
