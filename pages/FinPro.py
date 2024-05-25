import streamlit as st
from pages.chat import langchainning
from pages.checker  import checking, f_keywords

# ans = st.button("Back")
# # if ans = 
# Define the URL you want to redirect to
back_url = "https://www.google.com"  # Replace this with your desired URL
# btn = st.button("Back")
# Create a button for "Back"
if st.button("Back"):
    # st.markdown(f'<script>window.location.href="{back_url}"</script>', unsafe_allow_html=True)
    # st.redirect(back_url)
    st.markdown(f'<a href="{back_url}">Click here</a>', unsafe_allow_html=True)

def user_input(user):
   
    ans = langchainning().run(user)
    return ans

st.title("FinPro-AI 🤖")
st.caption("Hi Human, How can I help you today?")

if "messages" not in st.session_state:
    st.session_state.messages = []



q = st.chat_input("Type something here....")

def checking(query):
    flag = False
    list_of_words = query.split(" ")
    for i in list_of_words:
        if i.lower() in f_keywords:
            flag = True
            break
    return flag






# 
if q is not None and len(q.strip()) > 0:  
    if checking(q):
        st.session_state.messages.append(("user", q))
        st.session_state.messages.append(("assistant", user_input(q)))

        for role, message in st.session_state.messages:
            if role == "user":
                st.chat_message("user")
                st.write(message)
            elif role == "assistant":
                st.chat_message("assistant")
                st.write(message)
    else:
        # st.session_state.messages.append(("user", q))
        # st.session_state.messages.append(("assistant", "I'm a medical and health related chatbot. Please ask me about health or medicine."))
        # for role, message in st.session_state.messages:
        #     if role == "user":
        #         st.chat_message("user")
        #         st.write(message)
        #     elif role == "assistant":
        #         st.chat_message("assistant")
        #         # st.write(message)
        st.write("I'm a finance assistant chatbot. Please ask me about finance, Bankings, Investments or realted...")
        

b =  st.button("Clear Chat")
if b:
    st.session_state.messages = []